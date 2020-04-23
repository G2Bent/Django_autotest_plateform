from django.db import models

# Create your models here.
import django.utils.timezone as tz
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import time


class Project(models.Model):
    name = models.CharField(max_length=50,null=False)
    remark = models.TextField(null=True)
    creator = models.CharField(max_length=50,null=False,default="Jack Ma")
    createTime = models.DateTimeField(default=tz.now)

    class Meta:
        db_table="project"

    def clean(self):
        name = self.name.strip() if self.name else ""
        if 0 >= len(name) or len(name) > 20:
            raise  ValidationError({"name":"无效的项目名称"})

