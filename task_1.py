title_1 = "Tale of two cities"
print(title_1)

author_1 = "Charles Dickens"
print(author_1)

publication_year_1 = 1853
print(publication_year_1)

is_newer_than_2000_1 = publication_year_1 > 2000
print(is_newer_than_2000_1)

characters_1 = ["Jarvis Lory" , "Alexandre Manette"]
print(characters_1)

title_2 = "Inferno"
print(title_2)

author_2 = "Dante Alighieri"
print(author_2)

publication_year_2 = 2013
print(publication_year_2)

is_newer_than_2000_2 = publication_year_2 > 2000
print(is_newer_than_2000_2)

characters_2 = ["Robert Langdon" , "Elizabeth"]
print(characters_2)

favourite_books = [{"title": title_1, "author" : author_1, "year": publication_year_1, "is_newer_than_2000": is_newer_than_2000_1, "characters": characters_1},
{"title": title_2, "author" : author_2, "year": publication_year_2, "is_newer_than_2000": is_newer_than_2000_2, "characters": characters_2}]
print(favourite_books[1]["title"])


