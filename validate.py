#validate id and password
userId=input("Enter user id:")
password=input("Enter password:")
users={'user1':'pass1','user2':'pass2','user3':'pass3'}
if userId in users and users[userId]==password:
    print("Login successful!")
else:
    print("Invalid user id or password.")