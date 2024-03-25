from django.db import models
from django.contrib.auth.models import User


# Model for documents
class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_documents')
    shared_with = models.ManyToManyField(User, related_name='shared_documents', through='DocumentShare')

    def __str__(self):
        return f"{self.id} - {self.title} - {self.owner}"

# Model for document shares
class DocumentShare(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    can_edit = models.BooleanField(default=False)

    def __str__(self):
        return f"Document {self.document.id} shared with {self.user.username}"
