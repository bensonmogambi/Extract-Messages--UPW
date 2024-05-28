from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, MessageViewSet, receive_whatsapp_message

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('receive_whatsapp_message/', receive_whatsapp_message, name='receive_whatsapp_message'),
]
