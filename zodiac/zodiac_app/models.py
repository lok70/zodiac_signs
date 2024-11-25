from django.db import models

# Create your models here.

zodiac_data = [
    {
        'zodiac_ru': 'овен',
        'zodiac_en': 'aries',
        'start_day': '20 марта',
        'end_day': '19 апреля',
        'svg': '''<svg class="horoscope-icon" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="45" fill="url(#ariesGradient)"/>
            <path d="M50 20 C60 40 70 40 70 60 M50 20 C40 40 30 40 30 60" stroke="#FFD700" stroke-width="4"
                  fill="none"/>
            <defs>
                <radialGradient id="ariesGradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
                    <stop offset="0%" style="stop-color:#FF6B6B;stop-opacity:1"/>
                    <stop offset="100%" style="stop-color:#FF4500;stop-opacity:1"/>
                </radialGradient>
            </defs>
        </svg>'''
    },
    {
        'zodiac_ru': 'телец',
        'zodiac_en': 'taurus',
        'start_day': '20 апреля',
        'end_day': '20 мая',
        'svg': '''<svg class="horoscope-icon" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="45" fill="url(#taurusGradient)"/>
            <path d="M25 60 Q50 20 75 60 M35 75 Q50 55 65 75" stroke="#FFD700" stroke-width="4" fill="none"/>
            <defs>
                <radialGradient id="taurusGradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
                    <stop offset="0%" style="stop-color:#66CDAA;stop-opacity:1"/>
                    <stop offset="100%" style="stop-color:#2E8B57;stop-opacity:1"/>
                </radialGradient>
            </defs>
        </svg>'''
    },
    {
        'zodiac_ru': 'близнецы',
        'zodiac_en': 'gemini',
        'start_day': '21 мая',
        'end_day': '20 июня',
        'svg': '''<svg class="horoscope-icon" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="45" fill="url(#geminiGradient)"/>
            <path d="M30 30 L70 30 M30 70 L70 70 M40 30 L40 70 M60 30 L60 70" stroke="#FFD700" stroke-width="4"
                  fill="none"/>
            <defs>
                <radialGradient id="geminiGradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
                    <stop offset="0%" style="stop-color:#87CEFA;stop-opacity:1"/>
                    <stop offset="100%" style="stop-color:#4169E1;stop-opacity:1"/>
                </radialGradient>
            </defs>
        </svg>'''
    },
    {
        'zodiac_ru': 'рак',
        'zodiac_en': 'cancer',
        'start_day': '21 июня',
        'end_day': '21 июля',
        'svg': '''<svg class="horoscope-icon" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="45" fill="url(#cancerGradient)"/>
            <path d="M30 50 A20 20 0 0 1 70 50 A20 20 0 0 1 30 50 M25 70 A10 10 0 0 0 45 70 M55 70 A10 10 0 0 0 75 70"
                  stroke="#FFD700" stroke-width="4" fill="none"/>
            <defs>
                <radialGradient id="cancerGradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
                    <stop offset="0%" style="stop-color:#E0FFFF;stop-opacity:1"/>
                    <stop offset="100%" style="stop-color:#5F9EA0;stop-opacity:1"/>
                </radialGradient>
            </defs>
        </svg>'''
    },
    {
        'zodiac_ru': 'лев',
        'zodiac_en': 'leo',
        'start_day': '22 июля',
        'end_day': '22 августа',
        'svg': '''<svg class="horoscope-icon" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="45" fill="url(#leoGradient)"/>
            <path d="M50 25 A25 25 0 0 1 75 50 A25 25 0 0 1 50 75 A25 25 0 0 1 25 50 A25 25 0 0 1 50 25 M50 40 L50 60 M40 50 L60 50"
                  stroke="#FFD700" stroke-width="4" fill="none"/>
            <defs>
                <radialGradient id="leoGradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
                    <stop offset="0%" style="stop-color:#FFA500;stop-opacity:1"/>
                    <stop offset="100%" style="stop-color:#FF4500;stop-opacity:1"/>
                </radialGradient>
            </defs>
        </svg>'''
    },
    {
        'zodiac_ru': 'дева',
        'zodiac_en': 'virgo',
        'start_day': '23 августа',
        'end_day': '22 сентября',
        'svg': '''<svg class="horoscope-icon" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="45" fill="url(#virgoGradient)"/>
            <path d="M30 50 Q50 20 70 50 Q50 80 30 50 M40 50 L60 50" stroke="#FFD700" stroke-width="4" fill="none"/>
            <defs>
                <radialGradient id="virgoGradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
                    <stop offset="0%" style="stop-color:#98FB98;stop-opacity:1"/>
                    <stop offset="100%" style="stop-color:#2E8B57;stop-opacity:1"/>
                </radialGradient>
            </defs>
        </svg>'''
    },
    {
        'zodiac_ru': 'весы',
        'zodiac_en': 'libra',
        'start_day': '23 сентября',
        'end_day': '22 октября',
        'svg': '''<svg class="horoscope-icon" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="45" fill="url(#libraGradient)"/>
            <path d="M25 60 L75 60 M50 60 L50 30 M35 30 A15 15 0 0 1 65 30" stroke="#FFD700" stroke-width="4"
                  fill="none"/>
            <defs>
                <radialGradient id="libraGradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
                    <stop offset="0%" style="stop-color:#E6E6FA;stop-opacity:1"/>
                    <stop offset="100%" style="stop-color:#8A2BE2;stop-opacity:1"/>
                </radialGradient>
            </defs>
        </svg>'''
    },
    {
        'zodiac_ru': 'cкорпион',
        'zodiac_en': 'scorpio',
        'start_day': '23 октября',
        'end_day': '21 ноября',
        'svg': '''<svg class="horoscope-icon" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="45" fill="url(#scorpioGradient)"/>
            <path d="M25 50 Q50 20 75 50 L75 70 M65 60 L75 70 L85 60" stroke="#FFD700" stroke-width="4" fill="none"/>
            <defs>
                <radialGradient id="scorpioGradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
                    <stop offset="0%" style="stop-color:#FF69B4;stop-opacity:1"/>
                    <stop offset="100%" style="stop-color:#8B008B;stop-opacity:1"/>
                </radialGradient>
            </defs>
        </svg>'''
    },
    {
        'zodiac_ru': 'cтрелец',
        'zodiac_en': 'sagittarius',
        'start_day': '22 ноября',
        'end_day': '21 декабря',
        'svg': '''<svg class="horoscope-icon" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="45" fill="url(#sagittariusGradient)"/>
            <path d="M20 80 L80 20 M60 20 L80 20 L80 40 M50 50 L70 30" stroke="#FFD700" stroke-width="4" fill="none"/>
            <defs>
                <radialGradient id="sagittariusGradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
                    <stop offset="0%" style="stop-color:#00BFFF;stop-opacity:1"/>
                    <stop offset="100%" style="stop-color:#1E90FF;stop-opacity:1"/>
                </radialGradient>
            </defs>
        </svg>'''
    },
    {
        'zodiac_ru': 'козерог',
        'zodiac_en': 'capricorn',
        'start_day': '22 декабря',
        'end_day': '20 января',
        'svg': '''<svg class="horoscope-icon" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="45" fill="url(#capricornGradient)"/>
            <path d="M25 65 Q40 20 55 50 Q70 80 85 65 M55 50 L85 65" stroke="#FFD700" stroke-width="4" fill="none"/>
            <defs>
                <radialGradient id="capricornGradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
                    <stop offset="0%" style="stop-color:#B0C4DE;stop-opacity:1"/>
                    <stop offset="100%" style="stop-color:#4682B4;stop-opacity:1"/>
                </radialGradient>
            </defs>
        </svg>'''
    },
    {
        'zodiac_ru': 'водолей',
        'zodiac_en': 'aquarius',
        'start_day': '21 января',
        'end_day': '18 февраля',
        'svg': '''<svg class="horoscope-icon" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="45" fill="url(#aquariusGradient)"/>
            <path d="M25 40 Q50 20 75 40 M25 60 Q50 40 75 60" stroke="#FFD700" stroke-width="4" fill="none"/>
            <defs>
                <radialGradient id="aquariusGradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
                    <stop offset="0%" style="stop-color:#E0FFFF;stop-opacity:1"/>
                    <stop offset="100%" style="stop-color:#00CED1;stop-opacity:1"/>
                </radialGradient>
            </defs>
        </svg>'''
    },
    {
        'zodiac_ru': 'рыбы',
        'zodiac_en': 'pisces',
        'start_day': '19 февраля',
        'end_day': '19 марта',
        'svg': '''<svg class="horoscope-icon" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="45" fill="url(#piscesGradient)"/>
            <path d="M25 50 Q50 20 75 50 Q50 80 25 50 M25 50 Q50 80 75 50" stroke="#FFD700" stroke-width="4"
                  fill="none"/>
            <defs>
                <radialGradient id="piscesGradient" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
                    <stop offset="0%" style="stop-color:#AFEEEE;stop-opacity:1"/>
                    <stop offset="100%" style="stop-color:#20B2AA;stop-opacity:1"/>
                </radialGradient>
            </defs>
        </svg>'''
    }
]

class ZodiacSign(models.Model):
    zodiac_ru = models.CharField(max_length=50, unique=True)
    zodiac_en = models.CharField(max_length=50, unique=True)
    start_day = models.CharField(max_length=20, unique=True)
    end_day = models.CharField(max_length=50, unique=True)
    svg = models.TextField(max_length=50, unique=True)


    def __str__(self):
        return self.zodiac_en


def bulk_create_zodiac_signs():
    zodiac_signs = [
        ZodiacSign(
            zodiac_ru=data['zodiac_ru'],
            zodiac_en=data['zodiac_en'],
            start_day=data['start_day'],
            end_day=data['end_day'],
            svg=data['svg']
        )
        for data in zodiac_data
    ]

    ZodiacSign.objects.bulk_create(zodiac_signs)

