import requests
import csv

response = requests.get('https://jsonplaceholder.typicode.com/todos').json()
completed_todos = []
fields = ['id', 'title']
for item in response:
    if item.get('completed'):
        temp_item = {}
        for key in fields:
            temp_item[key] = item[key]
        completed_todos.append(temp_item)

with open('completed_todos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fields)
    writer.writeheader()
    writer.writerows(completed_todos)