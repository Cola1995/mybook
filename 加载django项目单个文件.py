import os

if __name__ == '__main__':
    # 加载django项目配置信息
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mybook.settings")
    # 导入django并启动项目
    import django

    django.setup()

    from app01 import models

    # books = models.Book.objects.all()
    # print(books)

    # 添加数据
    # models.Person.objects.create(name="天津李四",age=32)
    # models.Person.objects.create(name="巴扎黑",age=26)
    # models.Person.objects.create(name="仙阳",age=26)
    # print('ok')

    # persons = models.Person.objects.filter(id__gt=1, id__lt=3)  # 查询id大于1小于三的数据，不包括1，3，注意双下划线
    # print(persons)
    #
    # pp = models.Person.objects.filter(id__range=[1, 3])       # 查询id大于1小于三的数据， 包括1，3，注意双下划线
    # print(pp)
    # p1 = models.Person.objects.filter(bithday__year=2019)
    # print(p1)

    # 外键的查询操作
    # 正向查询
    # book_obj=models.Book.objects.all().first()
    # p=book_obj.p
    # print(p)
    # # 双下划线跨表查询
    # p2=models.Book.objects.filter(id=1).values("p__plisher")
    # # p3=models.Book.objects.filter(id=1).values_list("p__plisher")
    # print(p2)
    # # print(p3)
    # # 反向查询
    # #类名_set。all()
    # p_obj=models.Plisher.objects.all().first()
    # # p4 = p_obj.book_set.all()
    # p5 = p_obj.books.all()
    # print(p5)
    #
    # #基于双下划线
    # p6=models.Plisher.objects.filter(id=1).values("books__title")
    # print(p6)
    #通过作者创建一本书，会自动保存
    #1.在book表里创建一本书 2.在作者和关系表中添加关联记录
    # pp=models.Author.objects.first().book.create(title="爬虫实战22",p_id=22)
    # print(pp)

    # add 添加关联关系
    # 添加对象
    # book_obj=models.Book.objects.get(id=5)
    # models.Author.objects.get(id=7).book.add(book_obj)

    #添加id
    # models.Author.objects.get(id=7).book.add(*[1,2])

    #set
    # models.Author.objects.get(id=7).book.set([5,6])
    #聚合函数
    from django.db.models import Avg,Sum,Count,Max,Min

    # ret=models.Book.objects.all().aggregate(a=Avg("price"), b=Max("price"), c=Min("price"))  #设置key值
    # print('价格最高的是：%s,价格最低的是：%s,价格平均值是：%s'%(ret['b'],ret['c'],ret['a']))

    #分组查询
    # book_list = models.Book.objects.all().annotate(author_num=Count("author"))
    # print(book_list)
    # for i in book_list:
    #     print(i.title,i.author_num)

    # ret=models.Plisher.objects.all().annotate(min_pri=Min('book__price'))
    # # print(ret)
    # for i in ret:
    #     print(i.name,i.min_pri)
    # print(models.Book.objects.values_list('p__name'))
    titles = models.Plisher.objects.values_list("book__title",'name')
    print(titles)