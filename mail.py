import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import datetime
import pytz
from icalendar import Calendar, Event

# Set up the SMTP connection to Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'stckshr@gmail.com'
smtp_password = 'vsfulimyjlxttuwr'
smtp_conn = smtplib.SMTP(smtp_server, smtp_port)
smtp_conn.ehlo()
smtp_conn.starttls()
smtp_conn.login(smtp_username, smtp_password)

# Set up the email message
msg = MIMEMultipart()
msg['From'] = 'stckshr@gmail.com'
msg['To'] = 'testhg310@gmail.com'
msg['Subject'] = 'Meeting Invitation'

# Create the ICS file and attach it to the email message
event = Event()
event.add('summary', 'Meeting Title')
event.add('location', 'Meeting Location')
start_time = datetime.datetime(2023, 4, 28, 10, 0, tzinfo=pytz.utc)
end_time = datetime.datetime(2023, 4, 28, 12, 0, tzinfo=pytz.utc)
event.add('dtstart', start_time)
event.add('dtend', end_time)
event.add('description', 'Meeting Description')
cal = Calendar()
cal.add_component(event)
ical = cal.to_ical()
attachment = MIMEApplication(ical, 'octet-stream', Name='meeting.ics')
attachment['Content-Disposition'] = 'attachment; filename="meeting.ics"'
msg.attach(attachment)

# Send the email message
smtp_conn.sendmail(msg['From'], msg['To'], msg.as_string())

# Close the SMTP connection
smtp_conn.quit()
