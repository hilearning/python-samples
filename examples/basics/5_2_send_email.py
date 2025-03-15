# 使用smtplib发送邮件
import smtplib

def send_email(subject, body, to_email):
    from_email = "your_email@example.com"
    password = "your_password"
    message = f"Subject: {subject}\n\n{body}"
    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, message)

send_email("Test Subject", "Hello, this is a test email.", "recipient@example.com")
