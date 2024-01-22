# 8. Dictionaries Exercise:
# Create a dictionary of book titles and their authors. Write a function to search for a book
# by its title and return the author's name.
def search_author_titles_book(books, title):
    if title in books:
        return books[title]
    
books_dictionary = {
    "The Great Gatsby": "F. Scott Fitzgerald",
    "To Kill a Mockingbird": "Harper Lee",
    "1984": "George Orwell",
}

title_search = "The Great Gatsby"
author = search_author_titles_book(books_dictionary, title_search)
print(f"The author of '{title_search}' is {author}.")
