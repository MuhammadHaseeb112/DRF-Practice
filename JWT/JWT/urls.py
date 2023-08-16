
from django.contrib import admin
from django.urls import path,include
from API import views
from rest_framework.routers import DefaultRouter

# for JWT 
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView


# creating Router object
router = DefaultRouter()
# Register StudentViewSet with Router
router.register('stuAPI', views.StudentModelViewSet, basename='Student')
router.register('tecAPI', views.TeacherModelViewSet, basename='Teacher')

# now join our program with Router using URLS


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('home.urls')),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('getJWTToken/', TokenObtainPairView.as_view()), # this class get the access token and refresh token for us
    path('refreshJWTToken/', TokenRefreshView.as_view()), # this class refresh token for us
    path('verifyJWTToken/', TokenVerifyView.as_view()), # this class Verify token for us

]
