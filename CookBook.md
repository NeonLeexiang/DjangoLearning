# CookBook

---
## Step1. 建立环境 
类似其他 python project 一样，需要对整个项目建立一个虚拟环境，虚拟环境的建立在这里不再过度累述。
* 建立 `django` 工程  
> `django-admin startproject` 命令用来初始化一个 django 项目，它接收两个参数，第一个是项目名 blogproject，第二个指定项目生成的位置，因为之前我们为了使用 Pipenv 创建了项目根目录，所以将项目位置指定为此前创建的位置。

* 目录结构为：

[//]: # (TODO: 目录结构)

* 启动服务器
> `python manage.py runserver`

## Step2. 建立博客应用

* 建立博客应用
> `python manage.py startapp blog`
* `setting.py` 中添加对应的 app names.
* 编写 `blog` apps 的数据类型 `models.py`
* 编写了博客数据库模型的代码之后我们需要 `django` 将其翻译成数据库语言，在数据库中创建对应的数据库表。
> `python manage.py makemigrations` then `python manage.py migrate`  

> 当我们执行了 python manage.py makemigrations 后，django 在 blog 应用的 migrations 目录下生成了一个 0001_initial.py 文件，这个文件是 django 用来记录我们对模型做了哪些修改的文件。目前来说，我们在 models.py 文件里创建了 3 个模型类，django 把这些变化记录在了 0001_initial.py 里。 
  
> 不过此时还只是告诉了 django 我们做了哪些改变，为了让 django 真正地为我们创建数据库表，接下来又执行了 python manage.py migrate 命令。django 通过检测应用中 migrations 目录下的文件，得知我们对数据库做了哪些操作，然后它把这些操作翻译成数据库操作语言，从而把这些操作作用于真正的数据库。

## Step3. Django 处理 HTTP 请求
* 编写 `urls.py`
* 编写 视图函数 `views.py`
* 配置项目 URL `blogproject/urls.py`

## Step4. 使用 Django 模版系统
* 编写 `./templates`
* `settings.py` 中添加对应的 templates.

## Step5. 给博客应用穿上皮肤
* 编写 `./blog/static`
  
_这里一系列的知识可以补一下前端知识库_  

## Step6. 编写后台
* 编写 admin 后台。

## Step7. 开发博客文章详情页
一系列的前端内容以及views视图编写。以及一系列功能完善

## Step8. 开启评论功能
这个评论功能需要创建成为应用。`python manage.py startapp comments`

## Step9. 分离 `settings.py` 文件并为开发做准备
`settings.py` 中很多设置本地和开发环境是不一样，为了方便后续的开发以及对应改动，我们分离设置文件为3个部分：
- `common.py`
- `local.py`
- `production.py`