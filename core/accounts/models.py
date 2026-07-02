from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy

# Create your models here.

class UserManager(BaseUserManager):
    """
    custom user model manager
    """
    def create_user(self, email, password, **kwargs):
        """
        create and save a user
        """
        if not email:
            raise ValueError(gettext_lazy("the email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        """
        create and save a super user
        """
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError(gettext_lazy("superuser must have a is_staff = True"))
        if kwargs.get("is_superuser") is not True:
            raise ValueError(gettext_lazy("superuser must have a is_superuser = True"))
        
        return self.create_user(email, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    """
    custom user model for our app
    """
    email = models.EmailField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.email