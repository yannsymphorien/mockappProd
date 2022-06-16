from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class AccountManager(BaseUserManager):
    def create_user(self,email,username,password,**other_fields):
        if not email:
            raise ValueError(_("Users must have an email address"))
        if not username:
            raise ValueError(_("Users must have an unique username"))
        email=self.normalize_email(email)
        user=self.model(email=email,username=username,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,username,password,**other_fields):
            other_fields.setdefault('is_staff',True)
            other_fields.setdefault('is_superuser',True)
            other_fields.setdefault('is_active',True)
            if other_fields.get('is_staff') is not True:
                raise ValueError('is_staff is set to False')
            if other_fields.get('is_superuser') is not True:
                raise ValueError('is_superuser is set to False')
            return self.create_user(email,username,password,**other_fields)


class client(AbstractBaseUser, PermissionsMixin):

    # Relationships
    type = models.ForeignKey("type.type", on_delete=models.DO_NOTHING)

    # Fields
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True, db_index=True, )
    username = models.CharField(max_length=255, unique=True)
    date_of_birth = models.DateField()
    REQUIRED_FIELDS = ['username', 'firstname']
    USERNAME_FIELD = 'email'
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    objects = AccountManager()

    class Meta:
        pass

    def __str__(self):
        return str(self.username)

    def get_absolute_url(self):
        return reverse("client_client_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("client_client_update", args=(self.pk,))
