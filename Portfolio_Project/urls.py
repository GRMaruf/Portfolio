from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from portfolio.views import *
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('auth/', include('authentication.urls')),
    path('u-', include('portfolio.urls')),
    path('', home, name='home'),
    
    path('dashboard/edit_profile', edit_profile, name='edit_profile'),
    path('dashboard/project', project, name='project'),
    path('dashboard/project/<int:id>', project, name='project'),
    path('dashboard/project_delete/<int:id>', project_delete, name='project_delete'),
    path('dashboard/experience', experience, name='experience'),
    path('dashboard/experience/<int:id>', experience, name='experience'),
    path('dashboard/experience_delete/<int:id>', experience_delete, name='experience_delete'),
    path('dashboard/education', education, name='education'),
    path('dashboard/education/<int:id>', education, name='education'),
    path('dashboard/education_delete/<int:id>', education_delete, name='education_delete'),
    path('dashboard/certificate', certificate, name='certificate'),
    path('dashboard/certificate/<int:id>', certificate, name='certificate'),
    path('dashboard/certificate_delete/<int:id>', certificate_delete, name='certificate_delete'),
    path('dashboard/reference', reference, name='reference'),
    path('dashboard/reference/<int:id>', reference, name='reference'),
    path('dashboard/reference_delete/<int:id>', reference_delete, name='reference_delete'),
    
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
