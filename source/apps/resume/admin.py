from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import *


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email", "phone")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "institute",
    )
    search_fields = (
        "title",
        "institute",
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "subtitle",
    )
    search_fields = (
        "title",
        "subtitle",
    )


admin.site.register(SkillCategory)
admin.site.register(Skill)
