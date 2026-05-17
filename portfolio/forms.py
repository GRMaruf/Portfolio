from django import forms
from portfolio.models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user',]

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for x in self.fields.values():
            x.widget.attrs.update({
                'class': 'form-control'
            })

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for x in self.fields.values():
            x.widget.attrs.update({
                'class': 'form-control'
            })

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['profile',]

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for x in self.fields.values():
            x.widget.attrs.update({
                'class': 'form-control'
            })

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['profile',]

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for x in self.fields.values():
            x.widget.attrs.update({
                'class': 'form-control'
            })

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        exclude = ['profile',]

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for x in self.fields.values():
            x.widget.attrs.update({
                'class': 'form-control'
            })

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        exclude = ['profile',]

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for x in self.fields.values():
            x.widget.attrs.update({
                'class': 'form-control'
            })

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'
        exclude = ['profile',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for x in self.fields.values():
            x.widget.attrs.update({
                'class': 'form-control'
            })

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'
        exclude = ['profile',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for x in self.fields.values():
            x.widget.attrs.update({
                'class': 'form-control'
            })

class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = '__all__'
        exclude = ['profile',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for x in self.fields.values():
            x.widget.attrs.update({
                'class': 'form-control'
            })

