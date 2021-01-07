from django.contrib import admin
from django.urls import path, include
from users.views import RegisterUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('forum.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('register/', RegisterUserView.as_view(), name='register')
]
