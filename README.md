This script allows you to send an email using Python's built-in smtplib and email libraries.

**How it works**
Setup:
The script defines SMTP server settings, sender and receiver email addresses, and the email content (subject and body).

**Message Construction:**
It creates a MIME email message with the specified subject and body.

**Sending:**
The script connects to the SMTP server, starts TLS encryption, logs in with the sender's credentials, and sends the email.

**Usage**

Edit the following variables in the script:

- sender_email
- sender_password
- receiver_email
Run the script:
  `Python send_email.py`

**Notes**
- For Gmail, you may need to enable "App Passwords" if you have 2-Step Verification enabled.
- This script is for educational purposes. Do not share your credentials.
- If you want to use a local SMTP server for testing, change smtp_server to "localhost" and adjust the port as needed. Remove authentication lines if your local server does not require them.
