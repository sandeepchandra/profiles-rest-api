from django.contrib import admin
from .models import UserProfile, UserProfileFeed
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserProfileFeed)