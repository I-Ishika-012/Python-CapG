'''
create a form function using kwargs, taking user input
'''

def form(**fields):
    print("Enter your details:")
    for key in fields:
        fields[key] = input(f"Enter your {key}: ")
    return fields

user_info = form(name="", age="", country="")
print("User Information:", user_info)