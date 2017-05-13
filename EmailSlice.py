#get email address
email = input("What is your email address? ")
#slice out username
user = email[:email.index("@")]
#slice domain name
domain = email[email.index("@")+1:]
#format message
output = "User name: {}\nDomain name: {}".format(user, domain)
#display message
print(output)
