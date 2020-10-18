from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLE = [
        (USER, "user"),
        (MODERATOR, "moderator"),
        (ADMIN, "admin"),
    ]

    role = models.CharField(max_length=40, choices=ROLE,
                            default=ROLE,
                            verbose_name='Роль', )
    bio = models.TextField(max_length=250, blank=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=250, blank=True, null=True,
                                unique=True)
    confirm_code = models.CharField(max_length=5)

    class Meta:
        ordering = ["username"]

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_admin

    @property
    def is_moderator(self):
        return self.role == 'moderator' or self.is_moderator
