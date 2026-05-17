from django.urls import path
from portfolio.views import *

urlpatterns = [
    path('current_user/dashboard', dashboard, name='dashboard'),
    
    path('', profile, name='profile'),
    path('<str:username>', profile, name='profile'),
    path('<str:username>/contact', contact, name='contact'),
    path('<str:username>/projects', projects, name='projects'),
    path('<str:username>/resume', resume, name='resume'),

    path('dashboard/edit_profile', edit_profile, name='edit_profile'),
    path('dashboard/add_tags', add_tags, name='add_tags'),
    path('dashboard/project', project, name='project'),
    path('dashboard/project/<int:id>', project, name='project'),
    path('dashboard/project_delete/<int:id>', project_delete, name='project_delete'),
    path('dashboard/skill', skill, name='skill'),
    path('dashboard/skill/<int:id>', skill, name='skill'),
    path('dashboard/skill_delete/<int:id>', skill_delete, name='skill_delete'),
    path('dashboard/experience', experience, name='experience'),
    path('dashboard/experience/<int:id>', experience, name='experience'),
    path('dashboard/experience_delete/<int:id>', experience_delete, name='experience_delete'),
    path('dashboard/education', education, name='education'),
    path('dashboard/education/<int:id>', education, name='education'),
    path('dashboard/education_delete/<int:id>', education_delete, name='education_delete'),
    path('dashboard/certificate', certificate, name='certificate'),
    path('dashboard/certificate/<int:id>', certificate, name='certificate'),
    path('dashboard/certificate_delete/<int:id>', certificate_delete, name='certificate_delete'),
    path('dashboard/testimonial', testimonial, name='testimonial'),
    path('dashboard/testimonial/<int:id>', testimonial, name='testimonial'),
    path('dashboard/testimonial_delete/<int:id>', testimonial_delete, name='testimonial_delete'),
    path('dashboard/reference', reference, name='reference'),
    path('dashboard/reference/<int:id>', reference, name='reference'),
    path('dashboard/reference_delete/<int:id>', reference_delete, name='reference_delete'),
]
