from django.shortcuts import render, redirect, HttpResponse
from app01 import models


# Create your views here.

# 展示所有出版社页面
def plisher_list(request):
    ret = models.Plisher.objects.all()
    return render(request, "plisher_list.html", {'plisher_list': ret})


def add_plisher(request):
    if request.method == "POST":
        new_name = request.POST.get('plisher_name')
        models.Plisher.objects.create(plisher=new_name)
        return redirect('/plisher_list/')
    return render(request, 'add_plisher.html')


# 删除出版社
def delete_plisher(request):
    del_id = request.GET.get('id', None)
    if del_id:
        models.Plisher.objects.get(id=del_id).delete()
        return redirect('/plisher_list/')
    else:
        return HttpResponse('传入参数错误')



# 删除出版社   #网址传参数的第二种写法
def delete_plisher2(request,del_id):
    # del_id = request.GET.get('id', None)
    if del_id:
        models.Plisher.objects.get(id=del_id).delete()
        return redirect('/plisher_list/')
    else:
        return HttpResponse('传入参数错误')

def edit_plisher(request):
    if request.method == "POST":  # 判断是那种提交方式
        e_id = request.POST.get('id')
        new_name = request.POST.get('plisher_name')
        edit_obj = models.Plisher.objects.get(id=e_id)  # 找到要修改的对象
        edit_obj.plisher = new_name  # 修改出版社名字
        edit_obj.save()  # 提交到数据库
        return redirect("/plisher_list/")
    edit_id = request.GET.get('id')  # 将前一个页面的信息传递到当前页面
    edit_object = models.Plisher.objects.get(id=edit_id)
    return render(request, 'edit_plisher.html', {"plisher": edit_object})


def book_list(request):
    '''
    #book列表页
    :param request:
    :return:
    '''
    ret = models.Book.objects.all()
    return render(request, "book_list.html", {'book_list': ret})


def add_book(request):
    '''
    #添加书籍
    :param request:
    :return:
    '''
    if request.method == "POST":
        new_book_name = request.POST.get('book_name')
        new_plisher = request.POST.get('plisherq')
        models.Book.objects.create(title=new_book_name, p_id=new_plisher)  # 注意外键
        return redirect('/book_list/')
    ret = models.Plisher.objects.all()
    return render(request, "add_book.html", {"plisher_list": ret})


def edit_book(request):
    '''
    #编辑书籍
    :param request:
    :return:
    '''
    if request.method == "POST":
        new_id = request.POST.get('id')
        new_book = request.POST.get('bookname')
        new_pl = request.POST.get('pl')
        res = models.Book.objects.get(id=new_id)  # 获取要修改的对象
        res.title = new_book  # 替换titie值
        res.p_id = new_pl  # 替换option_id
        res.save()
        return redirect('/book_list/')

    edit_id = request.GET.get('id')
    ret = models.Book.objects.get(id=edit_id)
    all_pl_obj = models.Plisher.objects.all()
    return render(request, 'edit_book.html', {"book_obj": ret, "pl_obj": all_pl_obj})


def author_list(request):
    '''
    #作者列表
    :param request:
    :return:
    '''

    author_list_obj = models.Author.objects.all()
    # models.Author.objects.get(id=1).book.all()   author id为1 出品所有的书籍
    return render(request,'author_list.html',{"author_list_obj":author_list_obj})

def add_author(request):
    '''

    :return:
    '''

    if request.method=="POST":
        new_name=request.POST.get('name')
        new_books=request.POST.getlist('books')
        new_author_obj=models.Author.objects.create(name=new_name) #创建对象
        new_author_obj.book.set(new_books)  #设置书籍对应id
        return redirect('/author_list')
    book_list_obj=models.Book.objects.all()

    return render(request,'add_author.html',{"book_list_obj":book_list_obj})

def del_author(request):
    '''
    #删除作者
    :param request:
    :return:
    '''
    del_id=request.GET.get('id')
    models.Author.objects.get(id=del_id).delete()
    return redirect('/author_list/')

def edit_author(request):
    '''
    #编辑作者
    :param request:
    :return:
    '''
    if request.method=='POST':
        id=request.POST.get('id')
        new_a_name=request.POST.get('a_name')
        new_books=request.POST.getlist('zp')
        new_edit_obj=models.Author.objects.get(id=id)
        new_edit_obj.name=new_a_name
        new_edit_obj.book.set(new_books)
        new_edit_obj.save()
        return redirect('/author_list/')
    edit_id=request.GET.get('id')
    edit_obj=models.Author.objects.get(id=edit_id)
    all_zp=models.Book.objects.all()
    return render(request,'edit_author.html',{"edit_obj":edit_obj,"all_zp":all_zp})

def test(request):
    name='Ma'
    return render(request,'test.html',{"name":name})

def upload(request):
    if request.method == "POST":
        # 从请求的FILES中获取上传文件的文件名，file为页面上type=files类型input的name属性值
        filename = request.FILES["file"].name
        # 在项目目录下新建一个文件
        with open(r"C:\Users\Administrator\PycharmProjects\mybook\static\pic\%s"%filename, "wb") as f:
            # 从上传的文件对象中一点一点读
            for chunk in request.FILES["file"].chunks():
                # 写入本地文件
                f.write(chunk)
        return HttpResponse("上传OK")


def json_test(request):
    data={"name":"MA","age":"24"}
    data1=["MA",12]

    # import json                     #json格式的两种返回方式
    # data_str = json.dumps(data1)
    # return HttpResponse(data_str)


    from django.http import JsonResponse
    return JsonResponse(data,safe=False)


def title(request,year,month):
    print("年：%s"%year)
    print("月：%s"%month)
    return HttpResponse("ok")

def home(request):
    return render(request, 'car/home.html')

