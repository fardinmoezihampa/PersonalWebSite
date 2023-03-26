from django.shortcuts import render

from Sliders.models import Slider
from Resume.models import Skill, Biography


def home_page(request):
    sliders = Slider.objects.filter(is_show=True)
    skills = Skill.objects.all()
    bio = Biography.objects.filter(is_active=True).first()
    context = {
        'sliders': sliders,
        'skills': skills,
        'bio': bio,
    }
    return render(request, 'Home/index.html', context)
