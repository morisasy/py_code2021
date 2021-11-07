# prompt to enter any email

email = input('Enter your email: ')

# remove white space
email = email.strip()

# get the index of '@'
slicer_index = email.index('@')

# fetch the user name by string slicing
username = email[:slicer_index]

# fetch the domain name by string slicing
domain_name = email[slicer_index+1:]

# print the result seperately

print(f'Your user name is {username} and your domain namae is {domain_name}')