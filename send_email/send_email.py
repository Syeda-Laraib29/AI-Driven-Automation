"""
send_email.py

This script sends an email using SMTP. It constructs an email message with a subject and body,
then connects to an SMTP server (such as Gmail), authenticates, and sends the email to the specified recipient.

Requirements:
- Python 3.x
- Internet connection (for external SMTP servers)
- SMTP credentials (for authenticated servers like Gmail)

Usage:
- Update the sender_email, sender_password, and receiver_email variables with your information.
- For Gmail, you may need to use an app password if 2FA is enabled.

Functions:
    None. The script runs as a standalone program.
"""



import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Email Settings
smtp_server = "smtp.gmail.com"
smtp_port = 587  # Use 587 for TLS
sender_email = "sender_email@gmail.com"
sender_password = "your password"
receiver_email = "	receiver_email@gmail.com"

#Email Content

subject = "Test Email"
body = "This is a test email sent from sender."

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

#Send Email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")