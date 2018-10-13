from django.shortcuts import render, HttpResponse

from app01.models import Book


# Create your views here.
def index(request):
    '''
    模板语法：

    变量： {{ }}
        1 深度查询  句点符
        2 过滤器  {{ val｜filter_name: 参数 }}
    标签： {% %}
    :param request:
    :return:
    '''
    name = "yuan"
    i = 10
    l = [111, 222, 333]
    info = {"name": "yuan", "age": 222}

    b = True

    class Person(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age

    alex = Person("alex", 35)
    egon = Person("alex", 33)

    person_list = [alex, egon]

    # person_list = []

    # ######################过滤器

    import datetime

    now = datetime.datetime.now()
    file_size = 1234345236

    text = "hello python hi luffycity go java linux"

    link = "<a href=''>hello...</a>"

    # ######################标签
    user = "yes"

    # return render(request, "index.html", {"name": name})
    return render(request, "index.html", locals())


def login(request):
    if request.method == "POST":
        return HttpResponse("OK")
    return render(request, "login.html")


def order(request):
    return render(request, "order.html")


def sql(request):
    # ######################################################### 添加表记录 ###########################################

    # 方式1：
    # book_obj = Book(id=1, title="python红宝书", state='0', price=100, pub_date="2012-12-12", publish="人民")
    # book_obj.save()

    # 方式2：
    # book_obj = Book.objects.create(title="js", state='0', price=220, pub_date="2018-10-12", publish="人民")
    # print(book_obj.title)
    # print(book_obj.price)
    # print(book_obj.pub_date)

    # ######################################################### 查询表记录 ###########################################
    '''
    1 方法的返回值
    2 方法的调用这

    '''

    # (1) all方法： 返回值一个queryset 对象
    # book_list = Book.objects.all()
    # # print(book_list)
    # for obj in book_list:
    #     print(obj.title, obj.price)

    # （2） first, last: 调用者： queryset 对象  返回值: model对象
    # book=Book.objects.all().first()
    # book=Book.objects.all()[0]

    # （3） filter() 返回值： queryset 对象
    # book_list = Book.objects.filter(price=100)
    # print(book_list)
    # book_obj = Book.objects.filter(price=100).first()

    # （4） get() 有且只有一个查询结果时才有意义 返回值： model对象

    # book_obj = Book.objects.get(title="go")
    # book_obj = Book.objects.get(price=100)
    # print(book_obj.price)

    # （5）排除 exclude 返回值： queryset 对象
    # ret=Book.objects.exclude(title="go")

    # (6) order_by 调用者： queryset 对象  返回值： queryset对象
    # ret = Book.objects.all().order_by("id")

    # (7) count() 调用者： queryset 对象 返回值： int
    # ret = Book.objects.all().count()

    # (8) exist() 有数据就True 没有数据就False
    # ret = Book.objects.all().exists()
    # if ret:
    #     print("ok")

    # (9) values方法 调用者： queryset 对象  返回值： queryset对象
    # ret = Book.objects.all().values("price")
    # print(ret)

    # (10) values方法 调用者： queryset 对象  返回值： queryset对象

    # ret = Book.objects.all().values_list("price", "title")
    # print(ret)
    #
    # (11) distinct
    # ret = Book.objects.all().values_list("price").distinct()
    # print(ret)

    # ######################################################### 查询表记录之模糊查询 ###################################

    # ret = Book.objects.filter(price__gt=10, price__lt=200)
    # print(ret)
    #
    # ret = Book.objects.filter(title__startswith="py")
    # 只要有的就写出来
    # ret = Book.objects.filter(title__contains="h")
    # 不分大小写
    # ret = Book.objects.filter(title__icontains="h")
    #
    # print(ret)

    # ######################################################### 删除表记录和修改记录 ###################################

    # Book.objects.filter(price=220).delete()

    Book.objects.filter(title="php").update(title="php2")

    return HttpResponse('OK')


def query():
    # 查询出版社出版过价格大于200 的书箱
    ret = Book.objects.filter(publish="出版社", price__gt=200)

    # 查询2017年8月出版的以py开头的书籍名称
    ret = Book.objects.filter(title__startswith="py", pub_date=2017, pub_date__month=8).values("title")

    # 查询价格为50，100或者150的所有书籍名称及期出版社名称
    ret = Book.objects.filter(price__in=[50, 100, 150]).values("title", "publish")

    # 查询价格在100 到200之间的所有书箱名称及其价格
    ret = Book.objects.filter(price__range=[100,200]).values("title", "publish")

    # 查询所有人民出版社出版的书籍的价格（从高到低排序，去重）
    ret = Book.objects.filter(publish="人民出版社").values("price").distinct().order_by()
    return HttpResponse("OK")
