from django.shortcuts import render, redirect
from portfolio.models import *
from portfolio.forms import *
from portfolio.utils import *
from django.contrib.auth.decorators import login_required
# for sending email
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def render_dashboard_panel(request, context):
    """Return only the editable workspace panel for HTMX requests."""
    template = 'dashboard/_form_panel.html' if request.headers.get('HX-Request') else 'dashboard.html'
    return render(request, template, context)


def home(request):
    return render(request, 'home.html')

# Always pass a profile context while rendering html with nav and footer
def profile(request, username=None):
    context = {}

    if username:
        profile = get_user_profile(username)
        if profile is None:
            context['no_profile_error'] = True
    elif request.user.is_authenticated:
        return redirect('profile', username=get_current_username(request))
    else:
        profile = None

    context['profile'] = profile
    context['username'] = username
    
    if profile and profile.resume_skills:
        skills = []
        lines = profile.resume_skills.splitlines()
        for x in lines:
            skills.extend(x.split(":", 1)[1].split(','))
        context['skill_count'] = len(skills)

    return render(request, 'profile.html', context)

@login_required
def dashboard(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return redirect('edit_profile')

    return render(request, 'dashboard.html', {
        'profile': profile,
        'projects': profile.projects.all(),
        'experiences': profile.experiences.all(),
        'educations': profile.education.all(),
        'certificates': profile.certificates.all(),
        'references': profile.references.all(),
    })


@login_required
def edit_profile(request):
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
            profile = form
            context['profile'] = profile
            context['success_message'] = 'Profile saved successfully.'
        else:
            context['form'] = form
            return render_dashboard_panel(request, context)
    
    form = ProfileForm(instance = profile)
    context['form'] = form
    return render_dashboard_panel(request, context)

def contact(request, username=None):
    profile = get_user_profile(username)
    context = {
        'profile': profile
    }

    subject = "[Portfolio] Please Contact"
    recipient_list = [profile.user.email] if profile else []

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        html_message = render_to_string(
            'contact_email.html',
            {
                'user': profile.display_name,
                'message': message,
                'name': name,
                'email': email
            }
        )
        message = f'''
        Dear {profile.display_name},
        {message}

        Contacted by,
        {name}
        {email}
        '''

        if profile:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    recipient_list,
                    fail_silently=False,
                    html_message=html_message
                )
                context['success_message'] = 'Your message has been sent successfully.'
        return render(request, 'contact.html', context)
    return render(request, 'contact.html', context)

def projects(request, username=None):
    profile = get_user_profile(username)
    context = {
        "profile": profile,
        "projects": profile.projects.all() if profile else Project.objects.none(),
    }
    return render(request, 'projects.html', context)

def resume(request, username=None):
    profile = get_user_profile(username)
    context = {
        "profile": profile,
    }
    return render(request, 'resume.html', context)

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
            context['success_message'] = 'Project saved successfully.'
            print('Project successfully saved!')
        else:
            print('failed to save project!')
            context['form'] = form
            return render_dashboard_panel(request, context)
    
    form = ProjectForm(instance = project)
    context['form'] = form
    return render_dashboard_panel(request, context)

@login_required
def project_delete(request, id):
    profile = request.user.profile
    project = Project.objects.get(id=id)
    if project.profile == profile:
        print('User verified.. True')
        project.delete()
        return redirect('project')

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
            context['success_message'] = 'Experience saved successfully.'
        else:
            context['form'] = form
            return render_dashboard_panel(request, context)
    
    form = ExperienceForm(instance = object)
    context['form'] = form
    return render_dashboard_panel(request, context)

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
            context['success_message'] = 'Education saved successfully.'
        else:
            context['form'] = form
            return render_dashboard_panel(request, context)
    
    form = EducationForm(instance = object)
    context['form'] = form
    return render_dashboard_panel(request, context)

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
            context['success_message'] = 'Certificate saved successfully.'
        else:
            context['form'] = form
            return render_dashboard_panel(request, context)
    
    form = CertificateForm(instance = object)
    context['form'] = form
    return render_dashboard_panel(request, context)

@login_required
def certificate_delete(request, id):
    profile = request.user.profile
    certificate = Certificate.objects.get(id=id)
    if certificate.profile == profile:
        print('User verified.. True')
        certificate.delete()
        return redirect('certificate')

@login_required
def reference(request, id=None):
    try:
        profile = request.user.profile
    except:
        return redirect('edit_profile')
    
    context = {
        'references': profile.references.all(),
        'heading': 'Reference',
        'action': 'Update',
        'profile': profile,
    }

    if id:
        object = Reference.objects.get(id=id)
    else:
        object = None
        context['action'] = 'Create'
    
    if request.method == 'POST':
        form = ReferenceForm(request.POST, instance = object)
        if form.is_valid():
            form = form.save(commit=False)
            form.profile = profile
            form.save()
            context['success_message'] = 'Reference saved successfully.'
        else:
            context['form'] = form
            return render_dashboard_panel(request, context)
    
    form = ReferenceForm(instance = object)
    context['form'] = form
    return render_dashboard_panel(request, context)

@login_required
def reference_delete(request, id):
    profile = request.user.profile
    reference = Reference.objects.get(id=id)
    if reference.profile == profile:
        print('User verified.. True')
        reference.delete()
        return redirect('reference')
