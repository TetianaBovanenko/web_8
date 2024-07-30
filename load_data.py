import json
from models import Author, Quote


with open('authors.json', 'r') as f:
    authors_data = json.load(f)
    for author in authors_data:
        new_author = Author(
            fullname=author['fullname'],
            born_date=author['born_date'],
            born_location=author['born_location'],
            description=author['description']
        )
        new_author.save()


with open('qoutes.json', 'r') as f:
    quotes_data = json.load(f)
    for quote in quotes_data:
        author = Author.objects(fullname=quote['author']).first()
        if author:
            new_quote = Quote(
                tags=quote['tags'],
                author=author,
                quote=quote['quote']
            )
            new_quote.save()
