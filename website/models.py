from django.db import models

class Email_Data(models.Model):
    EMAIL_ID = models.EmailField(max_length=100, unique=True)
    stored = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Email Data'
        verbose_name_plural = "Email Data"

    def __str__(self):
        return self.EMAIL_ID
