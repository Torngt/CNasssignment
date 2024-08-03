import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, from_email, to_email, smtp_server, smtp_port):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body text
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Establish connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        
        # Send the email
        server.sendmail(from_email, to_email, msg.as_string())
        
        print("Email sent successfully!")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        # Quit the SMTP server connection
        server.quit()

# User inputs
subject = "Test Email"
body = input("Enter the message to send: ")
from_email = "santoshbarai2058@gmail.com"
to_email = "pikman0123@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 25  # Unencrypted SMTP port

send_email(subject, body, from_email, to_email, smtp_server, smtp_port)
