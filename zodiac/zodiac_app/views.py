from django.shortcuts import render
from asgiref.sync import sync_to_async
from .models import ZodiacSign
from .utils import fetch_horoscope

# Create your views here.


@sync_to_async
def get_all_zodiac_signs():
    return list(ZodiacSign.objects.all())


async def index(request):
    main_data = await get_all_zodiac_signs()
    return render(request, 'index.html', {'main_data': main_data})


@sync_to_async
def get_zodiac_data(zodiac_name):
    return ZodiacSign.objects.get(zodiac_en=zodiac_name)


async def zodiac(request, zodiac_name):
    zodiac_data = await get_zodiac_data(zodiac_name)
    html_description = await fetch_horoscope(zodiac_name)
    return render(request, 'zodiac_page.html',
                  {'title': zodiac_name, 'zodiac_data': zodiac_data, 'html_description': html_description})

