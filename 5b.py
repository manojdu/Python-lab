import re

def search_contacts(file_name):
    with open(file_name, 'r') as file:
        text = file.read()

    phone_numbers = re.findall(r'\+\d{12}', text)
    email_addresses = re.findall(r'\S+@\S+', text)

    print("Phone Numbers:")
    for number in phone_numbers:
        print(number)
    
    print("\nEmail Addresses:")
    for email in email_addresses:
        print(email)

search_contacts('5b.txt')
