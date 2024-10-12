from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import RegisterView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('videos.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name="sign_up"),
    path('api/login/', LoginView.as_view(), name='login'),



        
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)