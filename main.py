import random
from male_first_names import male_first_names
from female_first_names import female_first_names
from last_names import last_names


def generate_realistic_name(existing_names):
    """Generates a unique realistic Indian name with a chance of having no last name"""
    while True:
        # Choose a male or female first name randomly
        if random.choice([True, False]):
            first_name = random.choice(male_first_names)
        else:
            first_name = random.choice(female_first_names)
        
        # 50% chance of not having a last name
        if random.choice([True, False]):
            last_name = random.choice(last_names)
            full_name = f"{first_name} {last_name}"
        else:
            full_name = first_name
        
        # Ensure the name is unique
        if full_name not in existing_names:
            existing_names.add(full_name)
            return full_name

def generate_mobile_number():
    """Generates a realistic Indian mobile number"""
    first_digit = random.choice([6, 7, 8, 9])
    remaining_digits = ''.join(random.choices('0123456789', k=9))
    mobile_number = f"+91{first_digit}{remaining_digits}"
    return mobile_number

def generate_contact(existing_names):
    """Generates a single unique contact with a realistic name and mobile number"""
    name = generate_realistic_name(existing_names)
    mobile_number = generate_mobile_number()
    
    # Create vCard format with mobile number only
    vcard = (
        f"BEGIN:VCARD\n"
        f"VERSION:3.0\n"
        f"FN:{name}\n"
        f"TEL;TYPE=CELL:{mobile_number}\n"
        f"END:VCARD\n"
    )
    
    return vcard

def generate_vcf_file(filename, num_contacts):
    """Generates a VCF file with a specified number of unique contacts"""
    existing_names = set()
    with open(filename, 'w') as file:
        while len(existing_names) < num_contacts:
            vcard = generate_contact(existing_names)
            file.write(vcard)

# Specify the number of contacts to generate
num_contacts = 10  # Change this value as per requirement
filename = 'random_indian_contacts.vcf'

# Generate the VCF file
generate_vcf_file(filename, num_contacts)

print(f"{num_contacts} unique contacts have been generated and saved to {filename}")