from django import forms
from portfolio.models import *

class FormControlMixin():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for x in self.fields.values():
            x.widget.attrs.update({
                'class': 'form-control'
            })

class ProfileForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user',]

        widgets = {
            'resume_skills': forms.Textarea({
                'placeholder': '''\
Languages: C, C++, Python, Java
Frontend: React.js, Tailwind, Bootstrap, Javascript, Typescript
Backend: Node.js, Express.js, RESTfull API, SQL, MongoDB
Libraries: NumPy, Pandas, Matplotlib, Scikit-learn
Tools: Git, Github, VS code, Postman, Thunderclient, Chrome DevTools
'''
            })
        }

class TagForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

class ProjectForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['profile',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['attach'].widget.attrs['class'] = 'form-check form-check-input ms-3 border-primary'      

class ExperienceForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        exclude = ['profile',]

class EducationForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        exclude = ['profile',]

class CertificateForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'
        exclude = ['profile',]

class TestimonialForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'
        exclude = ['profile',]

class ReferenceForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Reference
        fields = '__all__'
        exclude = ['profile',]