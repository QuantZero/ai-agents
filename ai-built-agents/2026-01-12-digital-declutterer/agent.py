import os
import sys
import logging
from dotenv import load_dotenv
from schemas import FileOrganizationInput, EmailOrganizationInput
from graph import declutter_flow

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()

# Main function
def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError("Please provide a task to perform: 'file' or 'email'.")

        task = sys.argv[1].lower()

        if task == 'file':
            directory = sys.argv[2] if len(sys.argv) > 2 else '.'
            input_data = FileOrganizationInput(directory=directory)
            declutter_flow.organize_files(input_data)
        elif task == 'email':
            email_data = EmailOrganizationInput(email_account=os.getenv('EMAIL_ACCOUNT'),
                                                email_password=os.getenv('EMAIL_PASSWORD'))
            declutter_flow.organize_emails(email_data)
        else:
            raise ValueError("Invalid task provided. Use 'file' or 'email'.")

    except Exception as e:
        logging.error(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
