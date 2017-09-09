name = input("Enter your first and last name: ")
firstName = name.split(" ")[0]
lastName = name.split(" ")[1].replace(".","")


print(lastName + ',',firstName,lastName + '.')