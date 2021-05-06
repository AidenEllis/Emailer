from email.message import EmailMessage
from HTMLTemplateRender.renderer import render_template
import smtplib
from Emailer import template_types as tp_types


class EmailSender:
    def __init__(self, HOST_USER, HOST_PASSWORD):
        self.HOST_USER = HOST_USER
        self.HOST_PASSWORD = HOST_PASSWORD

    def send(self, receiver, subject, template, context=None, template_type=tp_types.TEMPLATE_TYPE_PATH, SERVER='smtp.gmail.com', PORT=465):
        if template_type == tp_types.TEMPLATE_TYPE_PATH:
            if context is None:
                context = {}

            template = render_template(template_path=template, context=context)

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.HOST_USER
        msg['To'] = receiver
        msg.add_header('Content-Type', 'text/html')
        msg.set_content(template, subtype='html')

        with smtplib.SMTP_SSL(SERVER, PORT) as smtp:
            smtp.login(self.HOST_USER, self.HOST_PASSWORD)
            smtp.send_message(msg)
