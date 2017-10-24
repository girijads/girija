information_1={'First_name':'Rithika','Last_name':'Valishekkagari','Age':'28','City':'Sunnyvale'}
information_2={'First_name':'Raju','Last_name':'Valishekka','Age':'35','City':'Sunny'}
information_3={'First_name':'Rithurajeswar','Last_name':'gari','Age':'32','City':'vale'}
people=[information_1,information_2,information_3]

for username, user_info in people.items():
    print("\nUsername: " + username)
    full_name = user_info['First_name'] + " " + user_info['Last_name']
    Age=user_info['Age']
    location = user_info['city']

print("\tFull name: " + full_name.title()) 
print("\tLocation: " + location.title())
print("\tAge:" + Age.title())

