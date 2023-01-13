from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class AccountManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, nickname, password, *args,**kwargs):
        user = self.model(
            nickname=nickname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser, PermissionsMixin):
    nickname = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )
    
    objects = AccountManager()
    
    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['']