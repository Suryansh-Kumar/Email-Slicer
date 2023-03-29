# Collect email from user
# spliting email using @, the first part s username, second part is gonna saved as domain
# spliting domain using .

def main():
    print("Welcome to the email slicer")
    print("")
    email_input = input("Input your email address: ")
    (username,domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    print("Username: ", username)
    print("domain: ", domain)
    print("extension: ", extension)

while True:
    main()