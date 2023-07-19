import whois


user_domain = input("Enter the domain name: ")
user_parameter = input("Enter the parameter: ")
p = whois.whois(user_domain)
user_output = p[user_parameter]
print(user_output)