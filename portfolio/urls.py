from django.urls import path
from portfolio.views import *

urlpatterns = [
    # path('test', test, name='test'),
    path('<str:username>', profile, name='profile'),
    path('', profile, name='profile'),
    path('profile/<str:id>', profile, name='profile'),
    path('projects', projects, name='projects'),
    path('resume', resume, name='resume'),
    path('dashboard', dashboard, name='dashboard'),

    path('edit_profile', edit_profile, name='edit_profile'), # That's all
    path('add_tags', add_tags, name='add_tags'),
    
    path('project', project, name='project'),
    path('project/<int:id>', project, name='project'),
    path('project_delete/<int:id>', project_delete, name='project_delete'),
    path('skill', skill, name='skill'),
    path('skill/<int:id>', skill, name='skill'),
    path('skill_delete/<int:id>', skill_delete, name='skill_delete'),
    path('experience', experience, name='experience'),
    path('experience/<int:id>', experience, name='experience'),
    path('experience_delete/<int:id>', experience_delete, name='experience_delete'),
    path('education', education, name='education'),
    path('education/<int:id>', education, name='education'),
    path('education_delete/<int:id>', education_delete, name='education_delete'),
    path('certificate', certificate, name='certificate'),
    path('certificate/<int:id>', certificate, name='certificate'),
    path('certificate_delete/<int:id>', certificate_delete, name='certificate_delete'),
    path('testimonial', testimonial, name='testimonial'),
    path('testimonial/<int:id>', testimonial, name='testimonial'),
    path('testimonial_delete/<int:id>', testimonial_delete, name='testimonial_delete'),

    path('contact', contact, name='contact'),

    # Public username portfolio URLs. Keep these last so fixed routes above win.
    path('<str:username>/projects', username_projects, name='username_projects'),
    path('<str:username>/resume', username_resume, name='username_resume'),
    path('<str:username>', username_profile, name='username_profile'),
]
