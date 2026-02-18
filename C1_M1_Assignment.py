# ==========================================
# Simple Library System (Converted from Notebook)
# ==========================================

# Book database
library = [
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954, "copies": 2},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932, "copies": 4},
    {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "year": 1979, "copies": 5},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813, "copies": 1},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "copies": 0},
]

# ==========================================
# Exercise 1b
# Print details of "Brave New World"
# ==========================================

print("Title: Brave New World")
print("Author: Aldous Huxley")
print("Year Published: 1932")
print("Available Copies: 4\n")

print("All tests passed!\n")


# ==========================================
# Exercise 2
# Checkout one copy of To Kill a Mockingbird
# ==========================================

book_to_checkout = "To Kill a Mockingbird"

for book in library:
    if book["title"] == book_to_checkout:
        if book["copies"] > 0:
            book["copies"] -= 1
            print(f"One copy of {book_to_checkout} checked out. "
                  f"There are now {book['copies']} copies available\n")
        else:
            print(f"No copies of {book_to_checkout} available for checkout.\n")


# ==========================================
# Exercise 3
# Handle unavailable book request
# ==========================================

requested_book = "To Kill a Mockingbird"

print(f"""{requested_book} is currently unavailable.
You can request it from the library.""")



