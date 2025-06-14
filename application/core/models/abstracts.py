from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AuditDetailsModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_%(class)s_set')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_%(class)s_set')
    updated_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True