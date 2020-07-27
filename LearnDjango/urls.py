"""LearnDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

# urlpatterns为固定名称的列表
# 列表中的一个元素，就代表一条路由
# 从上到下进行匹配，如果能匹配上，Django会导入和调用path函数第二个参数指定的视图(或子路由)
# 如果匹配不上会自动抛出404异常
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("projects.urls")),
    path('',include("summary.urls")),
    path('',include("traffic.urls")),
    # path('docs/', include_docs_urls(title='接口文档')),
    path('api/', include('rest_framework.urls')),
]
#     path('index/',include('projects.url'))
# ]
