import csv
import json

response = []
books = []

with open('books.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
git
    for row in reader:
        books.append({
            'title': row[0],
            'author': row[1],
            'pages': row[3],
            'genre': row[2],
        })

with open("users.json", "r") as json_file:
    users = json.loads(json_file.read())

    books_count = len(books)
    users_count = len(users)

    current_user = 0
    offset = books_count // users_count
    books_remains = books_count - users_count * offset

    for i, user in enumerate(users):
        start = current_user * offset
        stop = start + offset

        if books_remains > 0 and i < int(books_remains):
            stop += 1

        response.append({
            'name': user['name'],
            'gender': user['gender'],
            'address': user['address'],
            'age': user['age'],
            'books': books[int(start):int(stop)]
        })
        current_user += 1

with open("result.json", "w") as result_json:
    result_json.write(json.dumps(response, indent=4))
