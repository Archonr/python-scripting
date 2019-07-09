import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path, time
import os
import tarfile

for exists in os.listdir('/tmp'):
    if exists.startswith('core-gameserver'):
    # Store configuration file values
        time = time.strftime('%Y-%m-%d', time.gmtime(os.path.getmtime('/data/gameserver_logs')))
        with tarfile.open('core-dump.tar.gz', mode='w:gz') as tf:
            logdir = ['/data/gameserver_logs', '/data/gameserver_logs/install', '/data/gameserver_logs/msg', '/data/gameserver_logs/site', '/data/gameserver_logs/wrn', '/data/gameserver_logs/db', '/data/gameserver_logs/debug', '/data/gameserver_logs/err']
            for lgdir in logdir:
                pathlog = lgdir
                #print(pathlog)
            #print (lgdir)
                for game in os.listdir(pathlog):
                    if game.startswith(time):
                        #print(pathlog + game)
                        tf.add(pathlog + '/' + game)
            for core in os.listdir('/tmp'):
                if core.startswith('core-gameserver'):
                    tf.add('/tmp/' + core)
        tf.close()

        email = 'phptest@pls.life'
        password = 'ooLLueeE7rcv'
        send_to_emails = ['v.korkach@pls.life', 'y.kosinskiy@pls.life', 'd.mosnenko@pls.life', 's.yarmak@pls.life', 's.lakhovets@pls.life'] # List of email addresses
        subject = 'This is core dump from gameserver'
        message = 'Archive in attachment'
        file_location = '/data/core-dump.tar.gz'

# Create the attachment file (only do it once)
        filename = os.path.basename(file_location)
        attachment = open(file_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# Connect and login to the email server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)

# Loop over each email to send to
        for send_to_email in send_to_emails:
    # Setup MIMEMultipart for each email address (if we don't do this, the emails will concat on each email sent)
            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = send_to_email
            msg['Subject'] = subject

    # Attach the message to the MIMEMultipart object
            msg.attach(MIMEText(message, 'plain'))
    # Attach the attachment file
            msg.attach(part)
    # Send the email to this specific email address
            server.sendmail(email, send_to_email, msg.as_string()) 

# Quit the email server when everything is done
        server.quit()
        os.remove("core-dump.tar.gz")
        for corerm in os.listdir('/tmp'):
            if corerm.startswith('core-gameserver'):
                os.remove('/tmp/' + corerm)
else:
    print("Not exist file")
