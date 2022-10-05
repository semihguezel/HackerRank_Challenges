phone_book = {}

def save_contact(name, number):
    phone_book[name] = number
    
n = int(input())
contacts = [list(map(str, input().split())) for _ in range(n)]

for i in range(len(contacts)):
    save_contact(contacts[i][0], contacts[i][1])

try:    
    while True:
        query = input()
        if query in phone_book.keys():
            print(f"{query}={phone_book[query]}")
        else:    
            print("Not found")
except: EOFError
