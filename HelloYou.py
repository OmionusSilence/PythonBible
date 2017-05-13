#Ask user for name
name = input("What is your name? ")
#Ask user for age
age = input("What is your age? ")
#Ask user for city
city = input("What city do you live in? ")
#Ask user for what they enjoy
hobby = input("What do you enjoy? ")
#Create output text
output = "Hello {0}, from {2}. You are {1} years old and enjoy {2}".format(name, age, city, hobby)
#Print output to screen
print(output)
