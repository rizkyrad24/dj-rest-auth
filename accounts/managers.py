from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email"))
        
    def create_user(self, email, first_name, last_name=None, password=None, **extra_fields):
        if not first_name:
            raise ValueError(_("User must submit first Name"))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Email address is required"))
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            email = email,
            **extra_fields
        )
        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save()
        return user
    
    def create_superuser(self, email, first_name, last_name=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have True value in is_superuser"))
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have True value in is_staff"))
        if not password:
            raise ValueError(_("Superuser must have password"))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Superuser must have email address"))
        
        user = self.create_user(email, first_name, last_name, password, **extra_fields)
        user.save()
        return user
