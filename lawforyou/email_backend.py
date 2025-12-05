"""
Custom email backend using Brevo (Sendinblue) API instead of SMTP.
This bypasses port blocking issues on platforms like Render.
"""
import os
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail import EmailMessage
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException


class BrevoAPIBackend(BaseEmailBackend):
    """
    Email backend that uses Brevo API instead of SMTP.
    """
    
    def __init__(self, fail_silently=False, **kwargs):
        super().__init__(fail_silently=fail_silently, **kwargs)
        
        # Configure API key authorization
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = os.environ.get('BREVO_API_KEY')
        
        # Create an instance of the API class
        self.api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
            sib_api_v3_sdk.ApiClient(configuration)
        )
    
    def send_messages(self, email_messages):
        """
        Send one or more EmailMessage objects and return the number of sent emails.
        """
        if not email_messages:
            return 0
        
        num_sent = 0
        for message in email_messages:
            try:
                sent = self._send(message)
                if sent:
                    num_sent += 1
            except Exception as e:
                if not self.fail_silently:
                    raise
        
        return num_sent
    
    def _send(self, email_message):
        """
        Send a single EmailMessage using Brevo API.
        """
        if not email_message.recipients():
            return False
        
        try:
            # Determine content type
            is_html = getattr(email_message, 'content_subtype', 'plain') == 'html'
            
            # Prepare the email
            send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
                to=[{"email": recipient} for recipient in email_message.to],
                sender={"email": email_message.from_email or os.environ.get('EMAIL_HOST_USER', 'byzantium1988@gmail.com')},
                subject=email_message.subject,
                html_content=email_message.body if is_html else None,
                text_content=email_message.body if not is_html else None,
            )
            
            # Add CC if present
            if email_message.cc:
                send_smtp_email.cc = [{"email": recipient} for recipient in email_message.cc]
            
            # Add BCC if present
            if email_message.bcc:
                send_smtp_email.bcc = [{"email": recipient} for recipient in email_message.bcc]
            
            # Send the email
            api_response = self.api_instance.send_transac_email(send_smtp_email)
            return True
            
        except ApiException as e:
            print(f"Brevo API Error: {e}")  # Log error
            if not self.fail_silently:
                raise
            return False
        except Exception as e:
            print(f"Email sending error: {e}")  # Log error
            if not self.fail_silently:
                raise
            return False
