#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


"""
我们可以通过设置环境变量，来指定 django 使用的配置文件。
对于 manage.py，通常在开发环境下执行，
因此将这里的 DJANGO_SETTINGS_MODULE 的值改为 blogproject.settings.local，
这样运行开发服务器时 django 会加载 blogproject/settings/local.py 这个配置文件。
另外看到 wsgi.py 文件中，这个文件中有一个 application，是在线上环境时 Gunicorn 加载运行的，
将这里面的 DJANGO_SETTINGS_MODULE 改为 blogproject.settings.production
这样，在使用 manage.py 执行命令时，加载的是 local.py 的设置，而使用 gunicorn 运行项目时，使用的是 production.py 的设置。
"""


def main():
    """Run administrative tasks."""
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogproject.settings')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogproject.settings.local')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
