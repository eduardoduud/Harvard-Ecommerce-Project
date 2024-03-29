# Django Auctions Project

This Django project, named "Commerce," serves as an auction site allowing users to create listings, bid on items, comment on listings, manage watchlists, and explore various categories of listings.

## Features

### Models

- **User**: Represents each user of the application.
- **Auction Listing**: Stores information about each auction listing, including title, description, starting bid, image URL, category, etc.
- **Bid**: Records bids made on auction listings.
- **Comment**: Stores comments made on auction listings.

### Create Listing

- Users can create new listings specifying title, description, starting bid, optional image URL, and category.

### Active Listings Page

- Displays all currently active auction listings.
- Shows essential details such as title, description, current price, and listing photo (if available).

### Listing Page

- Provides detailed information about a specific listing, including current price.
- Allows signed-in users to add/remove the listing from their watchlist.
- Enables signed-in users to place bids (if criteria are met).
- Allows listing creators to close auctions, declaring the highest bidder as the winner.

### Watchlist

- Signed-in users can view listings they've added to their watchlist.
- Clicking on a listing takes the user to its respective page.

### Categories

- Users can explore listings based on categories.
- Clicking on a category name displays all active listings in that category.

### Django Admin Interface

- Site administrators can manage listings, comments, and bids through the Django admin interface.
- Functions include viewing, adding, editing, and deleting.

## Technologies Used

- **Django**: Python web framework for rapid development and clean design.
- **HTML**: Used for structuring the website's content.
- **CSS**: Styling language to enhance the visual presentation.
- **JavaScript**: Provides interactivity, especially for dynamic elements.
- **SQLite**: Embedded database for storing application data.
- **Bootstrap**: Front-end framework for responsive and mobile-first development.

## Getting Started

1. Clone this repository.
2. Install Python and Django if not already installed.
3. Navigate to the project directory in your terminal.
4. Run `python manage.py runserver` to start the Django server.
5. Visit the website in your browser and explore the features.
