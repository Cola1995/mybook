from django.db import models

# Create your models here.
#出版社
class Plisher(models.Model):
    id = models.AutoField(primary_key=True)  # 创建主键字段id
    name = models.CharField(null=False, max_length=20)  # name字段不能为空

    def __str__(self):
        return self.plisher


#图书
class Book(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,null=False,unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2,default=99.9)
    p = models.ForeignKey(to="Plisher",on_delete=models.SET_NULL,null=True)   #创建外键
    #related_name 反向查找
    def __str__(self):
        return self.title
#作者
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False)
    # 告诉ORM 我这张表和book表是多对多的关联关系,ORM自动帮我生成了第三张表
    book = models.ManyToManyField(to="Book")


#person
class Person(models.Model):
    name=models.CharField(max_length=50,null=False)
    age=models.IntegerField()
    bithday=models.DateField(default='1995-01-05')
    create_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name