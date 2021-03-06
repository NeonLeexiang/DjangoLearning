from django.urls import path

from . import views


"""
注意
在 blogproject 目录下（即 settings.py 所在的目录），原本就有一个 urls.py 文件，这是整个工程项目的 URL 配置文件。
而我们这里新建了一个 urls.py 文件，且位于 blog 应用下。这个文件将用于 blog 应用相关的 URL 配置，这样便于模块化管理。
不要把两个文件搞混了。
"""


app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('archives/<int:year>/<int:month>/', views.ArchiveView.as_view(), name='archive'),
    path('categories/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('tags/<int:pk>/', views.TagView.as_view(), name='tag'),
    # path('search/', views.search, name='search'),
]


"""
绑定关系的写法是把网址和对应的处理函数作为参数传给 path 函数（第一个参数是网址，第二个参数是处理函数），
另外我们还传递了另外一个参数 name，这个参数的值将作为处理函数 index 的别名，这在以后会用到。
注意这里我们的网址实际上是一个规则，django 会用这个规则去匹配用户实际输入的网址，如果匹配成功，就会调用其后面的视图函数做相应的处理。

比如说我们本地开发服务器的域名是 http://127.0.0.1:8000，那么当用户输入网址 http://127.0.0.1:8000 后，
django 首先会把协议 http、域名 127.0.0.1 和端口号 8000 去掉，
此时只剩下一个空字符串，而 '' 的模式正是匹配一个空字符串，
于是二者匹配，django 便会调用其对应的 views.index 函数。
"""




