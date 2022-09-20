from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from app import apis
from django.conf import settings
from django.conf.urls import static

router = routers.DefaultRouter()
router.register(r'posts', apis.PostViewSet, 'posts')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    ]
