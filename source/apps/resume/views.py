from apps.resume.models import *
from django.shortcuts import render, Http404


def index(request):
    info = Info.objects.all()
    if info.count() == 0:
        raise 404
    info = info.first()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    skill_categories = SkillCategory.objects.all()

    context = {
        "info": info,
        "educations": educations,
        "experiences": experiences,
        "skill_categories": skill_categories,
    }
    return render(request, "index.html", context=context)