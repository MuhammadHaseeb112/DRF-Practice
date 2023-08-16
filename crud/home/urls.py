from django.contrib import admin
from django.urls import path, include
from . import views 
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home, name='home'),
    path('post_data/', views.post, name='post_data'),
    path('edit_data/<int:id>', views.edit, name='edit_data'),
    path('delete_data/<int:id>', views.delete, name='delete_data'),

    
]
# from django.conf.urls.static import static
# from django.conf import settings
# if settings.DEBUG:
# 		urlpatterns += static(settings.MEDIA_URL,
# 							document_root=settings.MEDIA_ROOT)