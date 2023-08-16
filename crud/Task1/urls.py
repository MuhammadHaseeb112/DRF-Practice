
from django.contrib import admin
from django.urls import path,include
from API import views

from rest_framework.routers import DefaultRouter


# creating Router object
router = DefaultRouter()
# Register StudentViewSet with Router
router.register('ProductAPI', views.ProductModelViewSet, basename='product')
# router.register('tecAPI', views.TeacherModelViewSet, basename='Teacher')

# now join our program with Router using URLS


urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include(router.urls)),
    path('', include('home.urls')),
]
from django.conf.urls.static import static
from django.conf import settings
if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL,
							document_root=settings.MEDIA_ROOT)