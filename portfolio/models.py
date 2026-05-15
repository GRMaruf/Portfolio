from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, null=True)

    full_name = models.CharField(max_length=120, default='')
    display_name = models.CharField(max_length=80, blank=True)
    title = models.CharField(max_length=120, blank=True)  # e.g. "Backend Developer"
    bio = models.TextField(blank=True)
    
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=120, blank=True)

    profile_image = models.ImageField(upload_to="profile_images/", blank=True, null=True)

    #  you can use Choose URL Type system
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    website = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.display_name or self.full_name

# e.g. Django, Python, PostgreSQL, Bootstrap
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # e.g. Project.objects.filter(tags__name="Django")

    def __str__(self):
        return self.name
    
class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="projects")

    title = models.CharField(max_length=150)
    description = models.TextField()
    
    tags = models.ManyToManyField(Tag, blank=True)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)

    image = models.ImageField(upload_to="projects/", blank=True, null=True)

    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="skills")

    name = models.CharField(max_length=100)
    
    SKILL_LEVELS = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
        ("expert", "Expert"),
    ]

    level = models.CharField(max_length=20, choices=SKILL_LEVELS, default="beginner")

    def __str__(self):
        return self.name

class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="experiences")

    position = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    location = models.CharField(max_length=120, blank=True)

    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # null = currently working

    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.position} at {self.company}"
    
class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="education")

    institution = models.CharField(max_length=150)
    degree = models.CharField(max_length=150)  # e.g. BSc, MSc
    field_of_study = models.CharField(max_length=150, blank=True)

    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)

    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Certificate(models.Model):
    profile = models.ForeignKey(
        "Profile",
        on_delete=models.CASCADE,
        related_name="certificates"
    )

    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=150)  # e.g. Coursera, Udemy, Google

    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)

    credential_id = models.CharField(max_length=100, blank=True) # real world verification ID or URL
    credential_url = models.URLField(blank=True)

    image = models.ImageField(upload_to="certificates/", blank=True, null=True)

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    profile = models.ForeignKey(
        "Profile",
        on_delete=models.CASCADE,
        related_name="testimonials"
    )

    name = models.CharField(max_length=120)
    position = models.CharField(max_length=120, blank=True)  # e.g. "CEO at XYZ"

    message = models.TextField()

    image = models.ImageField(upload_to="testimonials/", blank=True, null=True)

    rating = models.PositiveSmallIntegerField(default=5)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Testimonial from {self.name}"