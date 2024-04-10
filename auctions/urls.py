from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting", views.createListing, name="createlisting"),
    path('listing/<int:listing_id>/', views.listing_detail, name='listing_detail'),
    path("watchlist", views.watchList, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path('category/<int:category_id>/', views.category_detail, name='category_detail')
]
