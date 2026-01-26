import os
import logging

# Tool to organize files
def organize_files_tool(input_data):
    directory = input_data.directory
    logging.info(f"Organizing files in directory: {directory}")
    # Example logic for organizing files
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            extension = os.path.splitext(filename)[1].lower()
            target_dir = os.path.join(directory, extension[1:]) if extension else 'others'
            os.makedirs(target_dir, exist_ok=True)
            os.rename(filepath, os.path.join(target_dir, filename))
    logging.info("File organization complete.")

# Tool to organize emails
def organize_emails_tool(input_data):
    email_account = input_data.email_account
    email_password = input_data.email_password
    logging.info(f"Organizing emails for account: {email_account}")
    # Placeholder for email organization logic
    # Here you would connect to the email server and categorize emails based on predefined rules
    logging.info("Email organization complete.")
