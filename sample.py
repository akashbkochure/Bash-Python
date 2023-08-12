import os

# Accessing environment variables
home_directory = os.environ.get('HOME')
username = os.environ.get('USER')

current_working_directory = os.getcwd()
operating_system = os.environ.get('OSTYPE')

# Displaying environment variable values
print("Home directory:", home_directory)
print("Username:", username)
print("Current working directory:", current_working_directory)
print("Operating system:", operating_system)

