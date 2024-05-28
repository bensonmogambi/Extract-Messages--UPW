from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    folder_id = models.CharField(max_length=100)  # Google Drive Folder ID

class Message(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    content = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
