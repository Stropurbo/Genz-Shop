from django.db import models
class GetMailModel(models.Model):
    mail = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mail
