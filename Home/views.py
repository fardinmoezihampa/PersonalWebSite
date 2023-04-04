from django.shortcuts import render

from Sliders.models import Slider
from Resume.models import Skill, Biography, Experience


def home_page(request):
    sliders = Slider.objects.filter(is_show=True)
    skills = Skill.objects.all()[:3]
    bio = Biography.objects.filter(is_active=True).first()
    experience = Experience.objects.first()
    context = {
        'sliders': sliders,
        'skills': skills,
        'bio': bio,
        'experience': experience,
    }
    return render(request, 'Home/index.html', context)
