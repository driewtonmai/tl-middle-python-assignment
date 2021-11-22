from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.site_header = "TL-Group Admin"
admin.site.site_title = "TL-Group Admin Portal"
admin.site.index_title = "Административная панель TL-Group"
