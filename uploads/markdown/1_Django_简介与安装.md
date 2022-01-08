# 1 Django 简介与安装



## 1.1 Django 的 MTV 模型

本质上，MTV（Model，Template，View）模型是和 MVC 模型一样的，是一种保持各组件间的松耦合关系的模型。

* M表示模型（Model）：编写程序应有的功能，负责业务对象与数据库的映射。
* T表示模板（Template）：负责把页面（html）展示给用户。
* V表示视图（View）：负责业务逻辑，并在适当时候调用 Model 和 Template。

除了上述三层之外，还需要一个URL分发器，其作用是将 URL 请求分发给不同的 View 处理。

__业务流程图__

![](C:\Users\61440\OneDrive\Markdown笔记\Django\Ref\Pic1_1.png)



***



## 1.2 Django 项目创建

使用 django-admin 来创建 HelloWorld 项目：

```python
django-admin startproject HelloWorld
```

django 目录结构：

```python
.
|-- HelloWorld
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
`-- manage.py
```

目录说明：

* HelloWorld：项目的容器
* manage.py：命令行工具，用于与 Django 项目进行交互
* \__init__.py：一个空文件，告诉 python 该目录是一个 python 包
* asgi.py：一个 ASGI 兼容的 Web 服务器入口
* settings.py：该 Django 项目的设置/配置
* __urls.py：该 Django 项目的 URL 声明__

* wsgi.py：一个 WSGI 兼容的 Web 服务器入口

启动服务器：

```python
python3 manage.py runserver 0.0.0.0:8000
```



***



## 1.3 Path()函数

urls.py 中的 path() 函数，用于声明项目的 URL 索引。

__示例代码__

```python
from django.urls import path
 
from . import views
 
urlpatterns = [
    path('hello/', views.hello),
]
```

path() 函数结构：

```python
path(route, view, kwargs=None, name=None)
```

* route：字符串，表示 URL 规则，与之匹配的 URL 会执行对应的第二个参数 View
* view：用于执行与正则表达式匹配的 URL 请求
* kwargs：视图使用的字典类型的参数
* name：用于反向获取 URL