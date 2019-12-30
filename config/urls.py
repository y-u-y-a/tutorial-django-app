from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 第一引数で指定した文字列を第二引数で指定したファイルへ渡す
    path("", include("polls.urls")),
    path("blog/", include("blog.urls")),
    path("admin/", admin.site.urls),
]
