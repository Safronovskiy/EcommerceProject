from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager




class AuthUserManager(UserManager):

    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, username, password, **extra_fields)


class AuthUserModel(AbstractUser):
    res = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True,verbose_name='Электронная почта')
    phone = models.CharField(max_length=100)

    objects = AuthUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']              #required when superuser is registered, not for users

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email} ({self.username})'

class AuthUserProfileModel(models.Model):
    user = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    image = models.ImageField(upload_to='userprofile/%Y/%m/')
    first_name = models.CharField(max_length=100, verbose_name='Имя пользователя', blank=True, null=True)
    second_name = models.CharField(max_length=100, verbose_name='Фамилия пользователя', blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    hobby = models.CharField(max_length=100, blank=True, null=True)
    res = models.CharField(max_length=100, blank=True, null=True)
    res1 = models.CharField(max_length=100, blank=True, null=True)
    res2 = models.CharField(max_length=100, blank=True, null=True)
    res3 = models.CharField(max_length=100, blank=True, null=True)
    res4 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили Пользователей'

    def __str__(self):
        return f'Профиль пользвателя: {self.user}'

class AuthUserContacts(models.Model):
    userprofile = models.OneToOneField(AuthUserProfileModel, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    telegramm = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    viber = models.CharField(max_length=100, blank=True, null=True)
    zoom = models.CharField(max_length=100, blank=True, null=True)
    instagramm = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Контакты пользователя'
        verbose_name_plural = 'Контакты пользователей'

    def __str__(self):
        return f'контакты для - {self.userprofile}'