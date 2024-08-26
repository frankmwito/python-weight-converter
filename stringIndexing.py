# String indexing

email = input("Enter your email: ")

index = email.index("@")
user_name = email[:index]
domain = email[index + 1:]

print(f"your username is {user_name} and domain is {domain}")