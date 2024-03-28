from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import ListingForm
from .models import User, Listing, Bid, Comment


def index(request):
    active_listings = Listing.objects.filter(is_active=True)
    return render(request, "auctions/index.html", {"active_listings": active_listings})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required(login_url='/login')
def createListing(request):
    context ={}
    context['form'] = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.creator = request.user
            listing.save()
            return HttpResponseRedirect(reverse("index"))
            #return redirect('listing_detail', pk=listing.pk)
        else:
            return HttpResponseRedirect(reverse("index"))
    else:
        form = ListingForm()
        return render(request, "auctions/newListing.html", context)
    
def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    user = request.user
    is_owner = user == listing.creator
    has_won = False

    if listing.is_active:
        highest_bid = listing.bids.order_by('-amount').first()
        if highest_bid:
            has_won = highest_bid.bidder == user

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add_to_watchlist':
            user.watchlist.add(listing)
        elif action == 'remove_from_watchlist':
            user.watchlist.remove(listing)
        elif action == 'place_bid':
            bid_amount = float(request.POST.get('bid_amount'))
            if bid_amount >= listing.starting_bid and (not listing.bids.exists() or bid_amount > listing.current_price):
                bid = Bid(listing=listing, bidder=user, amount=bid_amount)
                bid.save()
            else:
                # Handle error message for invalid bid
                pass
        elif action == 'close_auction':
            if is_owner:
                highest_bid = listing.bids.order_by('-amount').first()
                if highest_bid:
                    listing.winner = highest_bid.bidder
                listing.is_active = False
                listing.save()
            else:
                # Handle error message for unauthorized closure attempt
                pass
        elif action == 'add_comment':
            comment_content = request.POST.get('comment_content')
            comment = Comment(listing=listing, commenter=user, content=comment_content)
            comment.save()

    return render(request, 'auctions/listing_detail.html', {'listing': listing, 'is_owner': is_owner, 'has_won': has_won})

@login_required(login_url='/login')
def watchList(request):
    return HttpResponseRedirect(reverse("index"))

def categories(request):
    return HttpResponseRedirect(reverse("index"))