from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/entities/', include('entities.urls')),
]

admin.site.site_header = "TL-Group Admin"
admin.site.site_title = "TL-Group Admin Portal"
admin.site.index_title = "Административная панель TL-Group"
