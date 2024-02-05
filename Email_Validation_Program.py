
import re

def has_at_symbol(email):
    return '@' in email

def consecutive_at_symbols(email):
    return '@@' not in email

# Function to check if there is more than one '@' symbol
def more_than_one_at_symbol(email):
    return email.count('@') <= 1

# Function to check for consecutive quotes
def consecutive_quotes(email):
    return not ("'" in email and email.count("'@'") > 1)

# Function to validate the local part of the email address
def valid_local_part(local_part):
    return re.match(r'^[a-zA-Z0-9!#$%&\'*+\-/=?^_`{|}~.][a-zA-Z0-9!#$%&\'*+\-/=?^_`{|}~.]{0,62}[a-zA-Z0-9!#$%&\'*+\-/=?^_`{|}~.]$', local_part)

# Function to validate the domain part of the email address
def valid_domain_part(domain_part):
    return re.match(r'^[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$', domain_part)

# Function to check if the total length does not exceed 254 characters
def total_length_not_exceeds_254(email):
    return len(email) <= 254

# Function to check if '@' symbol position is valid
def at_symbol_position(email):
    return email.rfind('@') >= len(email) - 6

# Function to validate IPv4 address in the domain part
def ipv4_address_validation(domain_part):
    return re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', domain_part) or \
           re.match(r'^\[\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\]$', domain_part)

# Function to validate the entire email address
def ValidateEmail(email):
    if '@' not in email:
        return False  # Email must contain an '@' symbol

    local_part, domain_part = email.split('@', 1)

    return (
        has_at_symbol(email) and
        consecutive_at_symbols(email) and
        more_than_one_at_symbol(email) and
        consecutive_quotes(email) and
        valid_local_part(local_part) and
        valid_domain_part(domain_part) and
        total_length_not_exceeds_254(email) and
        at_symbol_position(email) and
        ipv4_address_validation(domain_part)
    )

# Test your function with provided inputs
test_inputs = [
    "ethna@gmail.com", "susmi@gmail.com", "susmi_1@gmail.com", ".ethna@gmail.com", "@susmi@gmail.com",
    "ethna@gmail,com", "ethna@gmail.con", "email@example.com", "firstname.lastname@example.com",
    "email@subdomain.example.com", "firstname+lastname@example.com", "email@123.123.123.123",
    "email@[123.123.123.123]", "ethna@123.123.123", "susmi@[123.123.123.123]", "ethna@192.27.230.255",
    "ethna@193.23.0.256", "email@example-one.com", "plainaddress", "#@%^%#$@#$@#.com",
    "@example.com", "Joe Smith <email@example.com>", "email.example.com", "email@example@example.com",
    ".email@example.com", "email.@example.com", "email..email@example.com", "email@example",
    "email@-example.com", "email@example.web", "email@111.222.333.44444", "email@example..com"
]

for email in test_inputs:
    result = ValidateEmail(email)
    print(f"The email address '{email}' is {'VALID' if result else 'INVALID'}.")

