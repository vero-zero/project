from django.db import models

# Create your models here.

class itmes(models.Model):
    nickname = models.CharField(max_length=20)
    class Meta:
        db_table = "Items_List"  # 연결할 테이블 명
        managed = False  # 데이터 추가 유무