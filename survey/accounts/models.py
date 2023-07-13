
from django.db import models
from django.contrib import auth


# Create your models here.
# PermissionMixin добавляет функциональность связанную
# с управлением правами доступа и разрешениями пользователей
# auth.models.User передает основные данные имя, фамилия, почта
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)




