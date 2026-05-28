from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "display_name", "location", "created_at")
    search_fields = ("full_name", "display_name")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "profile", "start_date", "end_date")
    list_filter = ("tags", "start_date")
    search_fields = ("title", "description")

    filter_horizontal = ("tags",)  # 👈 makes ManyToMany tags easy UI

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("position", "company", "start_date", "end_date")
    search_fields = ("position", "company")
    list_filter = ("company",)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "start_year", "end_year")
    search_fields = ("institution", "degree")

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("title", "issuer", "issue_date")
    list_filter = ("issuer",)
    search_fields = ("title", "issuer")

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "created_at", "rating")
    search_fields = ("name", "position")
    list_filter = ("rating",)

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "email","created_at")
    search_fields = ("name", "position")