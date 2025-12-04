import csv
import os

def read_contacts(file_path):
    contacts = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            contacts.append(row)
    return contacts

def read_template(file_path):
    with open(file_path, 'r') as file:
        template = file.read()
    return template

def merge_emails(contacts, template): 
    merged_emails = []
    for contact in contacts:
        merged_email = template
        for key, value in contact.items():
            placeholder = f'[{key}]'
            merged_email = merged_email.replace(placeholder, value)
        merged_emails.append(merged_email)
    return merged_emails

def save_emails(merged_emails, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for i, email in enumerate(merged_emails):
        file_name = f'email_{i+1}.txt'
        file_path = os.path.join(output_folder, file_name)
        with open(file_path, 'w') as file:
            file.write(email)

# Read contacts from 'contacts.csv'
contacts = read_contacts('contacts.csv')

# Read template files from 'templates' folder
template_folder = 'templates'
template_files = os.listdir(template_folder)
templates = []
for file_name in template_files:
    file_path = os.path.join(template_folder, file_name)
    template = read_template(file_path)
    templates.append(template)

# Merge emails for each contact using the templates
merged_emails = []
for template in templates:
    merged_emails.extend(merge_emails(contacts, template))

# Save merged emails to separate files
output_folder = 'merged_emails'
save_emails(merged_emails, output_folder)