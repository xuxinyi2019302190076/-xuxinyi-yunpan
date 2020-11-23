# <font face="黑体" size=20>分布式作业</font>


# <font face="楷体">作业要求
##使用Django，并仿照百度盘，编写一个具有秒传功能的云盘系统。

# 作业完成过程
## 一.建立了本地仓库`*-XUXINYI-YUNPAN*`,创建了项目的主题文件，并且完成了与github远程仓库的联动。

## 二.第十周课程内容：跟随着老师的步骤，建立一个新应用`news`。在仓库中里添加了news应用，并在`setting.py`中配置news。
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news'
]
```
### <font face="楷体">建立news的`model`模型，*并将`reporter`也纳入后台管理*
```python
from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
```   
### 配置news中的用户`admin`,然后再创建一个超级用户
    py manage.py createsuperuser
### 新建一个`urls.py`文件，并根据教程进行配置
```python

from django.urls import path

from . import views

urlpatterns = [
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]
```
### 根据教程在`view.py`中配置
```python
from django.shortcuts import render

from .models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)
```
### 然后配置`templates`文件，新建`year_archive.html`和`base.html`
先新建文件夹templates，再在其中新建文件夹news，最后在news文件夹中新建文件year_archive.html
```python
{% extends "base.html" %}

{% block title %}Articles for {{ year }}{% endblock %}

{% block content %}
<h1>Articles for {{ year }}</h1>

{% for article in article_list %}
    <p>{{ article.headline }}</p>
    <p>By {{ article.reporter.full_name }}</p>
    <p>Published {{ article.pub_date|date:"F j, Y" }}</p>
{% endfor %}
{% endblock %}
```
### news应用大致设计配置完成，将所有在本地仓库所做的更改全部保存并git到远程仓库
  git add .
  git commit -m "备注"
  git push

## 三.第三次作业，添加homework应用
### 在`news/models.py`中更改之前的Report，Article，将其更改为Student和Homework
```python
from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=70)
    #age = models.IntegerField()
    class Sex(models.IntegerChoices):
        MALE = 1, '男'
        FEMALE = 2, '女'
        OTHER = 3, '其他'

    sex = models.IntegerField(choices=Sex.choices)

    def __str__(self):
        return self.full_name

class Homework(models.Model):
    commit_date = models.DateField()
    headline = models.CharField(max_length=200)
    attach = models.FileField()
    remark = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
```
### 在`news/admin`中以及urls.py以及views.py也进行相应更改覆盖
```python
admin.site.register(models.Student)

urlpatterns = [
    path('hw/create/',views.HomeworkCreate.as_view())

from .models import Student, Homework

from django.views.generic.edit import CreateView

class HomeworkCreate(CreateView):
    model = Homework
    template_name = 'homework_form.html'
    fields = ['headline','attach','remark', 'student']

```
### 在`templates`中新建一个文件`homework_form.html``
```python

<html>
<body>
<form method="post" enctype="multipart/form-data" >{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save">
</form>
</body>
</html>
```
### 
# 主要问题和解决方法：
## 问题1：在git克隆仓库时，没有访问权限

解决方法:使用ssh-keygen命令生成密钥，将生成的公钥文件 id_ras.pub内容拷贝e值到服务器端ssh公钥

## 问题2：在github建立好仓库之后，本地也新增了ssh key，同时也在本地新增了远程仓库， 但是在git push的时候出现错误 The authenticity of host 'github.com (192.30.255.113)' can't be established.

解决方法：直接回车的话会出现验证失败
Host key verification failed.
fatal: Could not read from remote repository.
百度后得知原来是本地少了 know_host文件，只要在刚刚那个位置输入yes就可以了，而不是回车。

## 问题3：在转入建好的本地仓库时，因为仓库名以-开头 使用cd语句无法转入

解决方法：百度学习后得知可以用cd /.-xxxxxxxx转入，转入成功

## 问题4：在news应用的homework界面中，输入上传时间时显示时间无效

解决方法:对model.py进行一下更改
 将`commit_date = models.DateField()`
 更改为`commit_date = models.DateField(auto_now=True)` 自动获取时间戳







# 作业结果展示
