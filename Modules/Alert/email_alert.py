import smtplib
from email.message import EmailMessage
import csv

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to    

    user = " " #mail_address
    msg['from'] = user
    password = " " #App_password

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

def to_email_address(file, department_name):
    #add department details in the Modules/Alert/dept_details.csv file, currently empty
    with open(file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['dept.name'] == department_name:
                return row['dept.mail.address']
    return None

def main():
    department_name = input("Enter Department Name: ")
    department_name = department_name.lower()
    file = 'Modules/Alert/dept_details.csv'

    subject = "Confirm the news"
    body = "The following news is negative about you"
    to = to_email_address(file, department_name)

    if to:
        print(f"Email address for {department_name}: {to}")
    else:
        print(f"Department {department_name} not found.")

    email_alert(subject, body, to)


if __name__ == '__main__':
    main()
    