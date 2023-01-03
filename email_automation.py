# SENDING EMAIL TO ONLY ONE USER


# import smtplib
# from email.message import EmailMessage

# email = EmailMessage()
# email['from']= 'mrb218748@gmail.com'
# email['to']= ['lcb2021043@iiitl.ac.in','anshuverma.av2187@gmail.com']
# email['subject']='You won 1,000,000,000 dollors!'
# email.set_content('fuck u bro for this act u are not understanding urself')
# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login('mrb218748@gmail.com','9838656201')
#     print('hello')
#     smtp.send_message(email)
#     print ('all the good boss')




# SENDING EMAIL TO MULTIPLE USERS BY TEMPLETING STRING NAME AND OTHER VARIABLES WHICH ARE USED IN EMAIL FROM



import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template



with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('mrb218748@gmail.com','9838656201')
    print('hello')
    
    html=Template(Path('index.html').read_text())
    email = EmailMessage()

    email['from'] = 'anshu verma'
    email['to'] = 'lcb2021043@gmail.com'

    email['subject']=f'You won 1,000,000,000 dollors!'
    email.set_content(html.substitute({'name':'mr_B'}),'_html_')

    smtp.send_message(email)
    print ('all the good boss')

    