import re

filename = "/content/phoneandemail"
phone_pattern = r"\+\d{12}"
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

with open(filename, 'r') as file:
  content = file.read()

phone_matches = re.findall(phone_pattern, content)
email_matches = re.findall(email_pattern, content)

print("Phone Numbers:",phone_matches)
print("\nEmail Addresses:",email_matches)