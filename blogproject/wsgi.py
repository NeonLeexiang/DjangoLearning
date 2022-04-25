"""
WSGI config for blogproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogproject.settings')

"""
我们可以通过设置环境变量，来指定 django 使用的配置文件。
对于 manage.py，通常在开发环境下执行，
因此将这里的 DJANGO_SETTINGS_MODULE 的值改为 blogproject.settings.local，
这样运行开发服务器时 django 会加载 blogproject/settings/local.py 这个配置文件。
另外看到 wsgi.py 文件中，这个文件中有一个 application，是在线上环境时 Gunicorn 加载运行的，
将这里面的 DJANGO_SETTINGS_MODULE 改为 blogproject.settings.production
这样，在使用 manage.py 执行命令时，加载的是 local.py 的设置，而使用 gunicorn 运行项目时，使用的是 production.py 的设置。
"""


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogproject.settings.production')

application = get_wsgi_application()
