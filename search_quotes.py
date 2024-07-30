from models import Author, Quote

def find_quotes_by_author(name):
    author = Author.objects(fullname=name).first()
    if author:
        quotes = Quote.objects(author=author)
        return [quote.quote for quote in quotes]
    return []

def find_quotes_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    return [quote.quote for quote in quotes]

def find_quotes_by_tags(tags):
    tags_list = tags.split(',')
    quotes = Quote.objects(tags__in=tags_list)
    return [quote.quote for quote in quotes]

def main():
    while True:
        command = input("Enter command (name, tag, tags, exit): ")
        if command.startswith("name:"):
            name = command[len("name:"):].strip()
            quotes = find_quotes_by_author(name)
            for quote in quotes:
                print(quote.encode('utf-8'))
        elif command.startswith("tag:"):
            tag = command[len("tag:"):].strip()
            quotes = find_quotes_by_tag(tag)
            for quote in quotes:
                print(quote.encode('utf-8'))
        elif command.startswith("tags:"):
            tags = command[len("tags:"):].strip()
            quotes = find_quotes_by_tags(tags)
            for quote in quotes:
                print(quote.encode('utf-8'))
        elif command == "exit":
            break

if __name__ == "__main__":
    main()
