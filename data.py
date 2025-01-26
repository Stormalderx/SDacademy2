favourite_books = [
    {
        "title": "Book one",
        "author": "Author one",
        "is_published_after_2000": True,
        "year": 2005
    },
    {
        "title": "Book Two",
        "author": "Author Two",
        "is_published_after_2000": False,
        "year": 1995
    }
]

#display_titles_using_for_loop
for book in favourite_books:
    print(book["title"])

#display_authors_using_for_loop
for book in favourite_books:
    print(book["author"])

#check the age of book using if
if favourite_books[0]["is_published_after_2000"]:
    print(favourite_books[0]["title"])

#check the age of books using if else
if book["is_published_after_2000"]:
    print(f"{book['title']} is newer than 2000")
else:
    print(f"{book['title']} is older than 2000")


#check the age of books switched
for book in favourite_books:
    if book["is_published_after_2000"] != False:
        print(f"{book['title']} is newer than 2000")
else: 
    print(f"{book['title']} is older than 2000")

#compare the publishing year
for book in favourite_books:
    if book["year"] > 2000:
        print(f"{book['title']} is newer than 2000")
    else: 
        print(f"{book['title']} is older than 2000")

