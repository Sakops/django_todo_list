from datetime import date
import email
from django.db import models
from django.contrib.auth.models import User
# from django.conf import settings


# Create your models here.
class Task(models.Model):
    # Символьный тип данных (<= 500 символов)
    title = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="header",
        verbose_name="description",
        help_text='<small class="text-muted">это наш заголовок</small><hr><br>',

        max_length=254,
    )
    description = models.TextField(
        unique=False,
        editable=True,
        null=True, 
        primary_key=False,
    )
    is_completed = models.BooleanField(
        default=False,
        
        # editable=
    )
    datetime = models.DateTimeField(
        auto_now_add=True, 
        blank=True
    )
    user = models.ForeignKey(
        User, 
        blank=True, 
        null=True, 
        on_delete=models.SET_NULL, 
        auto_created=True,
    )
    def __str__(self): 
        return self.title
    
        

    # title = models.