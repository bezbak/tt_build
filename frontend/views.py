from django.shortcuts import render


def index(request):
    return render(request, "index.html",  {
        "title": "Заказать сайт и IT-услуги в Кыргызстане — Tomorrow-Techs",
        "description": "Создаем сайты, CRM, ботов и мобильные приложения под ключ. Digital-услуги в Кыргызстане от Tomorrow-Techs.",
        "og_title": "Tomorrow-Techs — IT-студия",
        "og_description": "Разработка, SMM и автоматизация бизнеса в Кыргызстане.",
        "canonical": "https://tomorrow-techs.com/"
    })


def about(request):
    return render(request, "index.html",  {
        "title": "О нас — Проекты и отзывы | Tomorrow-Techs",
        "description": "Реальные отзывы и выполненные проекты нашей IT-студии Tomorrow-Techs.",
        "og_title": "О нас — Tomorrow-Techs",
        "og_description": "Опыт, кейсы, отзывы клиентов.",
        "canonical": "https://tomorrow-techs.com/about"
    })


def services(request):
    return render(request, "index.html", {
        "title": "Услуги — Разработка сайтов, CRM, брендинг | Tomorrow-Techs",
        "description": "Все IT-услуги: сайты, 3D, брендинг, чат-боты и таргет.",
        "og_title": "Услуги Tomorrow-Techs",
        "og_description": "Цифровые решения от одной команды.",
        "canonical": "https://tomorrow-techs.com/services"
    })


def contacts(request):
    return render(request, "index.html", {
        "title": "Контакты — Tomorrow-Techs",
        "description": "Свяжитесь с нами и получите бесплатную консультацию.",
        "og_title": "Контакты Tomorrow-Techs",
        "og_description": "Контактная информация и мессенджеры.",
        "canonical": "https://tomorrow-techs.com/contacts"
    })
