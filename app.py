from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__, static_folder="assets")

# Загрузка index.html как шаблона
def load_index_html():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

index_html_template = load_index_html()

# SEO-конфиг для каждой страницы
seo = {
    "/": {
        "title": "Заказать сайт и IT-услуги в Кыргызстане — Tomorrow-Techs",
        "description": "Создаем сайты, CRM, ботов и мобильные приложения под ключ. Digital-услуги в Кыргызстане от Tomorrow-Techs.",
        "og_title": "Tomorrow-Techs — IT-студия",
        "og_description": "Разработка, SMM и автоматизация бизнеса в Кыргызстане.",
        "canonical": "https://tomorrow-techs.com/"
    },
    "/about": {
        "title": "О нас — Проекты и отзывы | Tomorrow-Techs",
        "description": "Реальные отзывы и выполненные проекты нашей IT-студии Tomorrow-Techs.",
        "og_title": "О нас — Tomorrow-Techs",
        "og_description": "Опыт, кейсы, отзывы клиентов.",
        "canonical": "https://tomorrow-techs.com/about"
    },
    "/services": {
        "title": "Услуги — Разработка сайтов, CRM, брендинг | Tomorrow-Techs",
        "description": "Все IT-услуги: сайты, 3D, брендинг, чат-боты и таргет.",
        "og_title": "Услуги Tomorrow-Techs",
        "og_description": "Цифровые решения от одной команды.",
        "canonical": "https://tomorrow-techs.com/services"
    },
    "/contacts": {
        "title": "Контакты — Tomorrow-Techs",
        "description": "Свяжитесь с нами и получите бесплатную консультацию.",
        "og_title": "Контакты Tomorrow-Techs",
        "og_description": "Контактная информация и мессенджеры.",
        "canonical": "https://tomorrow-techs.com/contacts"
    },
}


@app.route("/assets/<path:path>")
def serve_assets(path):
    return send_from_directory(app.static_folder, path)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_index(path):
    full_path = "/" + path
    meta = seo.get(full_path, seo["/"])  # если нет — отдаем главную

    return render_template_string(index_html_template, **meta)


if __name__ == "__main__":
    app.run(debug=True)
