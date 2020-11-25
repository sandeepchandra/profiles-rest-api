from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for User Profiles"""

    def create_user(self, email, name, password):

        if not email:
            raise ValueError("The Email ID is not Specified")
        

        email = self.normalize_email(email)
        user = self.model(email = email, name = name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):

        user = create_user(email, name, password)

        user._is_superuser = True
        user.isstaff = True

        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model fro users in the system"""

    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Retrieves User full name"""
        return self.name

    def get_short_name(self):
        """ Retrieves User short name"""
        return self.name

    def __str__(self):
        """ Return string representation of the class object"""
        return self.email