## Emailer


* `Send Email easily with python.`

<br>

## Installation

* Install Package Using `pip`
   ```shell script
   python3 pip install Emailer
   ```
  
<br>

### How to use:

* How to send Email
    ```python
    from Emailer.core import EmailSender

    # Configuring HOST
    HOST_USER = 'example@gmail.com'
    HOST_PASSWORD = 'secretpassword'
    sender = EmailSender(HOST_USER, HOST_PASSWORD)
    
    # Lets send the email
  
    # This is out email content (a html file) You can also refer
    # to variables like jinja template
    html_file_path = '/some/path/name.html' # <h1>Hey {{ name }}<h1>
    context = {'name': 'Anonymous'} # The value of variable in html {{ name }}
    receiver = 'someone@gmail.com'
    subject = 'Nothing Special'
  
    sender.send(
      receiver=receiver,
      subject=subject,
      template=html_file_path,
      context=context
    )
  
    # And done.Email sent 🎊🎉
    ```

* You can also send text instead of html file
`Defaultly its set to TEMPLATE_TYPE_PATH to use html file path`
    ```python
    from Emailer import template_types
  
    sender.send(
      receiver=receiver,
      subject=subject,
      template='Just a text',
      template_type=template_types.TEMPLATE_TYPE_TEXT
    )
    
    # Just change the template type to text.
    ```

* Changing Server, Port
`defaultly its set to Gmail server:'smtp.gmail.com', port:465`
    ```python
    sender.send(
      receiver=receiver,
      subject=subject,
      template='Just a text',
      template_type=template_types.TEMPLATE_TYPE_TEXT,
      
      SERVER='Email server',
      PORT='Email servers port'
    )
    ```