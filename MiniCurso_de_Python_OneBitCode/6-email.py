import smtplib
import ssl
import mimetypes
from email.message import EmailMessage

# Dados do E-mail
password = open('password.txt', 'r').read()
from_email = 'tiago.s.e4@gmail.com'
to_email = 'tiago.s.e3@gmail.com'
subject = 'Automação Planilha'

body = """
Olá Tiago,

Segue em anexo a planilha de vendas por fabricante.

Att,
"""

# Criando o e-mail
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject
message.set_content(body)
safe = ssl.create_default_context()

# Anexando a planilha
anexo = 'datapivot_table.xlsx'
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split('/')
with open(anexo, 'rb') as attach:
    message.add_attachment(
        attach.read(), 
        maintype=mime_type, 
        subtype=mime_subtype, 
        filename=anexo
)
    

# Enviando o e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.send_message(message)