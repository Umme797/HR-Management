from django.urls import path
from DM_app import views
from django.conf import settings
from django.conf.urls.static import static 
from department_management import settings
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_department/', views.create_department, name='create_department'),
    path('update_department/<did>/', views.update_department, name='update_department'),
    path('delete_department/<did>/', views.delete_department, name='delete_department'),
    path('register', views.register, name='register'),
    path('login', views.ulogin, name='ulogin'),
    path('ulogout', views.ulogout, name='ulogout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



