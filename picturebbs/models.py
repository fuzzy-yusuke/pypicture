from django.db import models

# Create your models here.
class Pictures(models.Model):
    id = models.AutoField #自動採番
    user_name = models.CharField(max_length=200, null = True)
    content = models.CharField(max_length=200)

    #テーブル名の定義
    class Meta:
        db_table = 'pictures'