from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import random, uuid, os


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone=phone, password=password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        if password is None:
            raise TypeError(
                'Superuser must have a password'
            )
        user = self.create_user(phone=phone, password=password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


def get_avatar(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('account', filename)


class User(AbstractUser):
    CHOICE_TYPE = (
        (1, "Begin"),
        (2, "Check Sms"),
        (3, "Succes")
    )
    GENDER_TYPE = (
        (1, "Man"),
        (2, "Woman")
    )
    middle_name = models.CharField(blank=True, null=True, max_length=250)
    username = models.CharField(blank=True, null=True, max_length=50)
    phone = models.CharField(max_length=13, unique=True)
    # region = models.ForeignKey(Region, blank=True, null=True, related_name='region_users', on_delete=models.DO_NOTHING)
    # city = models.ForeignKey(Region, blank=True, null=True, related_name='city_users', on_delete=models.DO_NOTHING)
    address = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to=get_avatar, default='default__images/user.png', null=True, blank=True)
    # birthday = models.DateField(null=True, blank=True)
    # gender = models.IntegerField(choices=GENDER_TYPE, default=1)
    verified = models.IntegerField(choices=CHOICE_TYPE, default=1)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=10, null=True, blank=True)
    firebase_token = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    USERNAME_FIELD = 'phone'
    objects = UserManager()
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return 'User — ' + self.phone

class Condition(models.Model):
    name = models.CharField(default='salom', max_length=50)
    desc = models.TextField(default='salom', blank=True)

    def __str__(self):
        return self.name
