from django.db import models

# Create your models here.
from django.db import models
from utils.base_models import BaseModel


# Create your models here.
class Traffic(BaseModel):
    '''车辆信息表'''
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    serialnumber = models.CharField(max_length=30,help_text="任务号")
    urls = models.CharField(max_length=30,help_text="背景图地址")
    params=models.TextField(max_length=5000,help_text="具体参数")
    Accuracy=models.FloatField(help_text="准确率")
    plate_number=models.CharField(help_text="车牌号码",max_length=20)


    class Meta:
        db_table = "tb_traffic"
        verbose_name = "车辆信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.__doc__