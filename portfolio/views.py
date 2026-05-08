from django.shortcuts import render, redirect, get_object_or_404
from portfolio.models import *
from portfolio.forms import *

from django.contrib.auth.decorators import login_required
# for sending email
from django.core.mail import send_mail
from django.conf import settings

def public_profile(request):
    if request.user.is_authenticated:
        try:
            return request.user.profile
        except Profile.DoesNotExist:
            pass
    return Profile.objects.first()

def test(request):
    return render(request, 'test.html')

def contact(request):
    profile = public_profile(request)
    context = {'profile': profile}
    subject = "Important! Someone has contacted you through your portfolio."
    recipient_list = [profile.email] if profile and profile.email else [settings.EMAIL_HOST_USER]

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        message = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            recipient_list,
            fail_silently=False,
        )
        context['success_message'] = 'Your message has been sent successfully.'
        return render(request, 'contact.html', context)
    return render(request, 'contact.html', context)

def profile(request, id = None): # perfected

    if id:
        profile = Profile.objects.get(id=id)
    elif request.user.is_authenticated:
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            profile = None
    else:
        profile = Profile.objects.first()

    context = {
        "profile": profile,
    }
    return render(request, 'profile.html', context)

def projects(request):
    profile = public_profile(request)
    context = {
        "profile": profile,
        "projects": profile.projects.all() if profile else Project.objects.none(),
    }
    return render(request, 'projects.html', context)

def resume(request):
    profile = public_profile(request)
    context = {
        "profile": profile,
    }
    return render(request, 'resume.html', context)

def username_profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    context = {
        "profile": profile,
        "profile_username": username,
    }
    return render(request, 'profile.html', context)

def username_projects(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    context = {
        "profile": profile,
        "profile_username": username,
        "projects": profile.projects.all(),
    }
    return render(request, 'projects.html', context)

def username_resume(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    context = {
        "profile": profile,
        "profile_username": username,
    }
    return render(request, 'resume.html', context)

@login_required
def dashboard(request): # perfected, only redirection will ok
    return redirect('edit_profile')

@login_required
def edit_profile(request): # perfected
    context = {
        'heading': 'Profile',
        'action': 'Update'
    }
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None
        context['action'] = 'Create'
    context['profile'] = profile
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
        else:
            context['form'] = form
            return render(request, 'dashboard.html', context)
    
    form = ProfileForm(instance = profile)
    context['form'] = form
    return render(request, 'dashboard.html', context)

def add_tags(request, id = None): # perfected
    context = {
        'heading': 'Tags',
        'action': 'Add',
        'profile': public_profile(request),
    }
    
    if id:
        object = Project.objects.get(id=id)
    else:
        object = None
        context['action'] = 'Create'

    if request.method == 'POST':
        form = TagForm(request.POST, instance = object)
        if form.is_valid():
            form.save()
        else:
            context['form'] = form
            return render(request, 'dashboard.html', context)

    form = TagForm(instance = object)
    context['form'] = form
    context['tags'] = Tag.objects.all()
    return render(request, 'dashboard.html', context)

@login_required
def project(request, id=None): # perfected
    try:
        profile = request.user.profile
    except:
        return redirect('edit_profile')
    
    context = {
        'projects': profile.projects.all(),
        'heading': 'Project',
        'action': 'Update',
        'profile': profile,
    }
    
    if id:
        project = Project.objects.get(id=id)
    else:
        project = None
        context['action'] = 'Create'
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance = project)
        if form.is_valid():
            print(form)
            form = form.save(commit=False)
            form.profile = profile
            form.save()
            tags = request.POST.getlist('tags')
            form.tags.clear()
            form.tags.set(tags)
            print('Project successfully saved!')
        else:
            print('failed to save project!')
            context['form'] = form
            return render(request, 'dashboard.html', context)
    
    form = ProjectForm(instance = project)
    context['form'] = form
    return render(request, 'dashboard.html', context)

@login_required
def project_delete(request, id):
    profile = request.user.profile
    project = Project.objects.get(id=id)
    if project.profile == profile:
        print('User verified.. True')
        project.delete()
        return redirect('project')

@login_required
def skill(request, id=None):
    try:
        profile = request.user.profile
    except:
        print('profile does not found')
        return redirect('edit_profile')
    
    context = {
        'skills': profile.skills.all(),
        'heading': 'Skill',
        'action': 'Update',
        'profile': profile,
    }

    if id:
        skill = Skill.objects.get(id=id)
    else:
        skill = None
        context['action'] = 'Create'
    
    if request.method == 'POST':
        form = SkillForm(request.POST, instance = skill)
        if form.is_valid():
            form = form.save(commit=False)
            form.profile = profile
            form.save()
        else:
            context['form'] = form
            return render(request, 'dashboard.html', context)
    
    form = SkillForm(instance = skill)
    context['form'] = form
    return render(request, 'dashboard.html', context)

@login_required
def skill_delete(request, id):
    profile = request.user.profile
    skill = Skill.objects.get(id=id)
    if skill.profile == profile:
        print('User verified.. True')
        skill.delete()
        return redirect('skill')

@login_required
def experience(request, id=None):
    try:
        profile = request.user.profile
    except:
        return redirect('edit_profile')
    
    context = {
        'experiences': profile.experiences.all(),
        'heading': 'Experience',
        'action': 'Update',
        'profile': profile,
    }

    if id:
        object = Experience.objects.get(id=id)
    else:
        object = None
        context['action'] = 'Create'
    
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance = object)
        if form.is_valid():
            form = form.save(commit=False)
            form.profile = profile
            form.save()
        else:
            context['form'] = form
            return render(request, 'dashboard.html', context)
    
    form = ExperienceForm(instance = object)
    context['form'] = form
    return render(request, 'dashboard.html', context)

@login_required
def experience_delete(request, id):
    profile = request.user.profile
    experience = Experience.objects.get(id=id)
    if experience.profile == profile:
        print('User verified.. True')
        experience.delete()
        return redirect('experience')

@login_required
def education(request, id=None):
    try:
        profile = request.user.profile
    except:
        return redirect('edit_profile')
    
    context = {
        'educations': profile.education.all(),
        'heading': 'Education',
        'action': 'Update',
        'profile': profile,
    }

    if id:
        object = Education.objects.get(id=id)
    else:
        object = None
        context['action'] = 'Create'
    
    if request.method == 'POST':
        form = EducationForm(request.POST, instance = object)
        if form.is_valid():
            form = form.save(commit=False)
            form.profile = profile
            form.save()
        else:
            context['form'] = form
            return render(request, 'dashboard.html', context)
    
    form = EducationForm(instance = object)
    context['form'] = form
    return render(request, 'dashboard.html', context)

@login_required
def education_delete(request, id):
    profile = request.user.profile
    education = Education.objects.get(id=id)
    if education.profile == profile:
        print('User verified.. True')
        education.delete()
        return redirect('education')

@login_required
def certificate(request, id=None):
    try:
        profile = request.user.profile
    except:
        return redirect('edit_profile')
    
    context = {
        'certificates': profile.certificates.all(),
        'heading': 'Certificate',
        'action': 'Update',
        'profile': profile,
    }

    if id:
        object = Certificate.objects.get(id=id)
    else:
        object = None
        context['action'] = 'Create'
    
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES, instance = object)
        if form.is_valid():
            form = form.save(commit=False)
            form.profile = profile
            form.save()
        else:
            context['form'] = form
            return render(request, 'dashboard.html', context)
    
    form = CertificateForm(instance = object)
    context['form'] = form
    return render(request, 'dashboard.html', context)

@login_required
def certificate_delete(request, id):
    profile = request.user.profile
    certificate = Certificate.objects.get(id=id)
    if certificate.profile == profile:
        print('User verified.. True')
        certificate.delete()
        return redirect('certificate')

@login_required
def testimonial(request, id=None):
    try:
        profile = request.user.profile
    except:
        return redirect('edit_profile')
    
    context = {
        'testimonials': profile.testimonials.all(),
        'heading': 'Testimonial',
        'action': 'Update',
        'profile': profile,
    }

    if id:
        object = Testimonial.objects.get(id=id)
    else:
        object = None
        context['action'] = 'Create'
    
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES, instance = object)
        if form.is_valid():
            form = form.save(commit=False)
            form.profile = profile
            form.save()
        else:
            context['form'] = form
            return render(request, 'dashboard.html', context)
    
    form = TestimonialForm(instance = object)
    context['form'] = form
    return render(request, 'dashboard.html', context)

@login_required
def testimonial_delete(request, id):
    profile = request.user.profile
    testimonial = Testimonial.objects.get(id=id)
    if testimonial.profile == profile:
        print('User verified.. True')
        testimonial.delete()
        return redirect('testimonial')
