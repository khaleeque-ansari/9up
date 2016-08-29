from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    score = models.IntegerField(default=0)

    @classmethod
    def create(cls, name):
        user = cls(name=name)
        return user
