from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import save_incoming_message, auto_respond
from .drive_service import upload_to_drive
import os

@api_view(['POST'])
def receive_whatsapp_message(request):
    from_ = request.data.get('from')
    body = request.data.get('body')
    media_url = request.data.get('media_url')

    message = save_incoming_message(from_, body, media_url)

    if media_url:
        # Assuming media_url is downloaded to a local path
        file_path = download_media(media_url)
        customer = message.customer
        upload_to_drive(file_path, customer.folder_id)
        auto_respond(from_, 'attachment_received')
    else:
        auto_respond(from_)

    return Response({'status': 'message received'})

def download_media(media_url):
    # Logic to download media from the URL
    pass
