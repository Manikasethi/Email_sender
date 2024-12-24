import smtplib

try:
    # Set up SMTP connection
    ob = smtplib.SMTP('smtp.gmail.com', 587)
    ob.ehlo()
    ob.starttls()

    # Login credentials
    ob.login('your_email@gmail.com', 'your_app_password')

    # Email details
    subject = "Test Python"
    body = "I Love Python"
    message = "Subject:{}\n\n{}".format(subject, body)

    # Recipient list
    listadd = ['valid_recipient1@gmail.com', 'valid_recipient2@gmail.com']

    # Send the email
    ob.sendmail('your_email@gmail.com', listadd, message)
    print("Email sent successfully")
except Exception as e:
    print("Error:", e)
finally:
    # Quit the SMTP connection
    ob.quit()
