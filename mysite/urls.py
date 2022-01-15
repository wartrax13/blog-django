from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mysite.blog.urls', namespace='home')),
    path('blog/', include('mysite.blog.urls', namespace='blog'))
]
