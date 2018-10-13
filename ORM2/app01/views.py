from django.shortcuts import render, HttpResponse

# Create your views here.

from app01.models import *


def add(request):
    '''
    # 绑定关系视图
    :param request:
    :return:
    '''
    # pub = Publish.objects.create(name="人民出版社", email="123@qq.com", city="北京")

    # ###############################################绑定一对多的关系######################
    # 方式 1
    # 为book表绑定关系: publish
    # book_obj=Book.objects.create(title="红楼梦", price=100, publishDate="2012-12-12", publish_id=1)

    # # 方式 2：
    # pub_obj = Publish.objects.filter(nid=1).first()
    # book_obj = Book.objects.create(title="红楼梦", price=100, publishDate="2012-12-12", publish=pub_obj)
    # print(book_obj.title)
    # print(book_obj.price)
    # print(book_obj.publish)
    # print(book_obj.publish_id)
    # print(book_obj.publishDate)

    # 查询title 出版社对应的邮箱
    # book_obj = Book.objects.filter(title="红楼梦").first()
    # print(book_obj.publish.email)

    # ###############################################绑定多对多的关系######################
    book_obj = Book.objects.create(title="天天", price=100, publishDate="2012-12-02", publish_id=1)

    egon = Author.objects.get(name="egon")
    alex = Author.objects.get(name="alex")

    # 绑定多对多关系的API
    book_obj.authors.add(egon, alex)
    # book_obj.authors.add(1, 2, 3)
    # book_obj.authors.add(*[1, 2, 3])

    # 解除多对多关系

    # book = Book.objects.filter(nid=6).first()
    # book.authors.remove(2)
    # # book.authors.remove(*[1, 2])
    #
    # book.authors.clear()

    # print(book.authors.all())
    # ret = book.authors.all().values('name')
    # print(ret)

    return HttpResponse("OK")


def query(request):
    '''
    跨表查询：
        1 基于对象查询
        2 基于双下划线查询
        3 聚合和分组查询
        4 F 与 Q 查询
    :param request:
    :return:
    '''

    # －－－－－－－－－－－－－－－－－－－－－－－－－－基于对象的跨表查询（子查询）－－－－－－－－－－－－－

    # 一对多查询

    # book_obj = Book.objects.filter(title="三国").first()
    # print(book_obj.publish)  # 与这本书关联的出版社对象
    # print(book_obj.publish.name)
    #
    # # 一对多查询的反向查询: 查询人民出版社出版过的书籍名称
    #
    # publish_obj = Publish.objects.filter(name='人民出版社').first()
    # ret = publish_obj.book_set.all()
    # print(ret)

    # 正向查询
    # 查询主键为1 的书籍的出版社所在的城市

    # book_obj = Book.objects.filter(nid=1).first()
    # print(book_obj.publish.city)
    #
    # '''
    #
    # '''
    # --------------------------基于双下划线的跨表查询（join查询）---------------------
    '''
    正向查询按字段，反向查询按表名小写用来告诉ORM引擎join哪张表
    '''
    # 一对多查询的正向查询：查询三国这本书的出版社的名字

    # 方式1
    # ret = Book.objects.filter(title="三国").values("publish__name")
    # print(ret)

    # 方式2
    # ret = Publish.objects.filter(book__title='三国').values("name")
    # print(ret)

    # 查询红楼梦这本书的所有的作者的名字

    # 方式1
    # 需求： 通过Book表join与关联的Author表  正向查询 按字段 authors通知 ORM引擎 join book__authors 与 author
    # ret = Book.objects.filter(title="红楼梦").values("authors__name")
    # print(ret)

    # 方式2:
    # 需求： 通过Author表join与关联的Author表
    # ret = Author.objects.filter().values("name")
    # print(ret)

    # -------------------------- 一对一查询的查询 ： 查询alex的手机号---------------------
    # alex = Author.objects.filter(name='alex').first()
    # print(alex.authordetail.telephone)

    # 方式1
    # 需求  通过Author表join与关联的AuthorDetail表  正向查询 按字段 authordetail通知 ORM引擎 join

    # ret = Author.objects.filter(name="alex").values("authordatail__telephone")
    # print(ret)

    # ad = AuthorDetail.objects.filter(telephone="110").first()
    # print(ad.author.name)
    # print(ad.author.age)

    '''
    正向查询按字段，反向查询按表名小写用来告诉ORM引擎join那张表
    '''
    # 一对多查询的正向查询 ： 查询中国这本书的出版社的名字

    # ret = Book.objects.filter(title='三国').values("publish__name")
    # print(ret)

    # 查询三国这本书的所有作者的名字

    # 方式1：
    # 需求： 通过Book表join与其关联的Author表， 属于反向查询： 按表名小写book通知ORM引擎join book_authors

    # ret = Book.objects.filter(title='三国').values("authors__name")
    # print(ret)

    # 方式1：
    # 需求： 通过author表join与其关联的Book表， 属于反向查询： 按表名小写book通知ORM引擎join book_authors
    # ret = Author.objects.filter(book__title='三国').values("name")
    # print(ret)

    # 一对一查询的查询 ： 查询alex 的手机号

    # 方式1：
    # 需求： 通过author表join 与其关联的AuthorDetail表， 属于正向查询： 按字段authordetail通知ORM引擎join Authordetail

    # ret = Author.objects.filter(name='alex').values("authorDatail__telephone")
    # print(ret)

    # 方式2 ：通过AuthorDetail表join 与其关联的Author表， 属于反向查询： 按表名小写author通知ORM引擎join Author表
    # ret = AuthorDetail.objects.filter(author__name="alex").values("telephone")
    # print(ret)

    # 进阶练习
    # 练习： 手机号以110开阔大的作者出版过的所有的书籍名称以及书籍出版社名称

    # 方式1：
    # 需求： 通过Book表join Authordetail表, Book与AuthorDetail无关联，所以必须连续跨表
    # ret = Book.objects.filter(authors__authordatail__telephone__startswith='110').values("title", "publish__name")
    # print(ret)
    #
    # ret = Author.objects.filter(authordatail__telephone__startswith='110').values("book__title", "book__publish__name")
    # print(ret)

    # －－－－－－－－－－－－－－－－聚合与分组查询－－－－－－－－－－－－－－－－－－－－－－－－－－

    # －－－－－－－－－－－－－－－－聚合 oggregate:返回值是一个字典，

    # 查询所有书籍的平均价格
    from django.db.models import Avg, Max, Min, Count

    # ret = Book.objects.all().aggregate(avg_price=Avg("price"), max_price=Max("price"))
    #
    # print(ret)
    # ------------------> 分组查询 annotate, 返回值依然是queryset

    # 单表分组查询：

    # 示例 1
    # 查询每一个部门的名称以及员工的平均薪水

    # select dep,Avg(salary) from emp group by dep

    # ret = Emp.objects.values("dep").annotate(avg_salary=Avg("salary"))
    # print(ret)

    # 示例2
    # 查询每一个省份的名称以及员工数

    # ret = Emp.objects.values("province").annotate(c=Count("id"))
    # print(ret)

    # 补充知识点
    ret = Emp.objects.all()
    print(ret)  # select * from emp
    ret = Emp.objects.values("name")
    print(ret)   # select name from emp

    Emp.objects.values("id").annotate(avg_salary=Avg("salary"))


    return HttpResponse('OK')


'''
正向查询： 关联属性 A－－－－〉B
反向查询： 关联属性 B－－－－〉A 
# 一对多查询
    正向查询：按字段
    反向查询：按表名小写_set.all()
    Book ------->  Publish
    
'''
'''
# 多对多查询
        正向查询：按字段
        反向查询：表名小写_set.all()
        
                                        book_obj.authors.all()
        Book(关联属性：authors)对象   -------------------------〉 Author对象
                                     <-------------------------
                                     author_obj.book_set.all()  # queryset
                                     
# 一对一查询
            正向查询：按字段
        反向查询：表名小写
                                              book_obj.authordetail
        Author(关联属性：authordetail)对象   -------------------------〉 AuthorDetail对象
                                     <-------------------------
                                      authordetail.author
        
基于双下划线的跨表查询（join查询）
    key: 
        

'''



