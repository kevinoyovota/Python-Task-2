import random

def collect_details():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    return [first_name,last_name, email]

def generate_password(f_name, l_name):
    random_string = ""
    for i in range(5):
        random_string += random.choice("_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return f_name[:2] + l_name[-2:] + random_string
        

def employee_dict(f_name, l_name, e_mail, password): # This function creates a dictionary of each user's info
    employee = {
        "first name": f_name,
        "last name": l_name,
        "email": e_mail,
        "password": password
    }
    return employee

workers = [] # This creates a list to store each individual dictionary of user info
while True:    
    user_details = collect_details()
    f_name = user_details[0] # Retrieves the first name
    l_name = user_details[1] # Retrieves the last name
    e_mail = user_details[2] # Retrieves email address
    password = generate_password(f_name, l_name)

    prompt = input(f"Would you like to have '{password}' as your password? (y/n) ")
    if prompt.lower() == "y":
        employee_data = employee_dict(f_name, l_name, e_mail, password)
    else:
        password = input("Enter a password of more than 7 characters: ")
        while True:
            if len(password) > 7:
                employee_data = employee_dict(f_name, l_name, e_mail, password)
                break
            else:
                password = input(f"'{password}' is not more than 7 characters. Try again: ")

    print(f"\nFirst name: {f_name}")
    print(f"Last name: {l_name}")
    print(f"Email: {e_mail}")
    print(f"Password: {password}")
    
    workers.append(employee_data)
    prompt = input("\nDo you want to enter another employee's data? (y/n) ")
    if prompt.lower() == 'n':
        break
    print("-----------------------------------------------------\n")

print("-----------------------------------------------------")
for worker in workers:
    print(f"\nEmployee {workers.index(worker) + 1}")
    print("First name: " + worker.get("first name"))
    print("Last name: " + worker.get("last name"))
    print("Email: " + worker.get("email"))
    print("Password: " + worker.get("password"))
