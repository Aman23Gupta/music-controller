# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import string
import random


def generate_unique_code():
    length = 6

    while True:
        code = ''.join((random.choice(string.ascii_uppercase) for x in range(length)))
        if Room.objects.filter(code=code).count() == 0:
            break

    return code


class Room(models.Model):
    code = models.CharField(
        max_length=8, default=generate_unique_code, unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
