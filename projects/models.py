from django.db import models
from utils.base_models import BaseModel


# Create your models here.
class Person(BaseModel):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = "tb_person"
        verbose_name = "人员信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Teacher(models.Model):
    '''老师表'''
    teacher_name = models.CharField(max_length=30, verbose_name="老师", default="")
    tel = models.CharField(max_length=30, verbose_name="电话", default="")
    mail = models.CharField(max_length=30, verbose_name="邮箱", default="")

    class Meta:
        verbose_name = "老师"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.teacher_name

class Student(models.Model):
    '''学生表'''
    student_id = models.CharField(max_length=30, verbose_name="学号", default="")
    name = models.CharField(max_length=30, verbose_name="姓名", default="")
    age = models.IntegerField(verbose_name="年龄",  default="")
    # 多对多
    teachers = models.ManyToManyField(Teacher, verbose_name="老师")

    class Meta:
        verbose_name = "学生"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name