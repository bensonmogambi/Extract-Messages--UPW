from twilio.rest import Client
from .models import Customer, Message
from .config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(to, body, media_url=None):
    message = client.messages.create(
        from_=f'whatsapp:{TWILIO_WHATSAPP_NUMBER}',
        body=body,
        to=f'whatsapp:{to}',
        media_url=media_url
    )
    return message.sid

def save_incoming_message(from_, body, media=None):
    customer, _ = Customer.objects.get_or_create(phone=from_)
    message = Message.objects.create(customer=customer, content=body, attachment=media)
    return message
