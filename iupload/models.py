# -*- coding: utf-8 -*-
from django.db import models


class Images(models.Model):
    file = models.FileField(upload_to='%Y/%m/%d')