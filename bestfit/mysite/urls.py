from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from mysite.core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('test/', views.test_page, name= 'test'),
    path('test/<int:myid>', views.test_page, name= 'test'),
    path('result/', views.result, name= 'result'),
    path('profile/', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
