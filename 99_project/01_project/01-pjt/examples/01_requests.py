import requests
from pprint import pprint

response = requests.get('https://jsonplaceholder.typicode.com/todos').json()
# print(response)
user_response = requests.get('https://jsonplaceholder.typicode.com/users').json()
# print(user_response)

completed_todos = []
fields = ['id', 'title']
for item in response:
    # if item['completed'] == True:
    #     print(item)
    if item.get('completed'):
        # print(item)
        temp_item = {}
        for key in fields:
            temp_item[key] = item[key]
        for user in user_response:
            if user['id'] == item['userId']:
                user_info = {
                    'id': user['id'],
                    'name': user['name'],
                    'username': user['username'],
                    'email': user['email'],
                }
                temp_item['user'] = user_info
        completed_todos.append(temp_item)
#print(completed_todos)
pprint(completed_todos)