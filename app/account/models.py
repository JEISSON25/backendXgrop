from model_utils.models import TimeStampedModel
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class TypeAccount(TimeStampedModel):
    name = models.CharField('Nombre', max_length=50)

    def __str__(self):
        return f'{self.name}'


class CustomAccountManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        # if not email:
        #     raise ValueError('El campo de correo electrónico es obligatorio')
        # email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    # email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    # phone = models.BigIntegerField('Teléfono', blank=True, null=True)
    # direction = models.CharField(
    #     'Dirección',  max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomAccountManager()

    type_account = models.ForeignKey(
        TypeAccount,
        verbose_name="Type Account",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.username} - {self.type_account}'
