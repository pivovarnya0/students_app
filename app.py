from flask import Flask, jsonify, render_template_string # type: ignore

app = Flask(__name__)

COURSES = [
    {"id": 1, "name": "DevOps инженерия"},
    {"id": 2, "name": "Базы данных"},
    {"id": 3, "name": "Разработка веб-сервисов"},
    {"id": 4, "name": "Основы кибербезопасности"},
    {"id": 5, "name": "Статистика и анализ данных"},
]

TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ title }} | StudentSpace</title>
    <style>
        * { box-sizing: border-box; }

        body {
            margin: 0;
            background: #f6f8fc;
            color: #202938;
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }

        nav {
            background: white;
            border-bottom: 1px solid #e7eaf0;
            padding: 18px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 20px;
            flex-wrap: wrap;
        }

        .logo {
            color: #315bea;
            font-size: 21px;
            font-weight: 700;
            text-decoration: none;
        }

        nav a:not(.logo) {
            color: #596579;
            text-decoration: none;
            margin-left: 22px;
            font-size: 14px;
        }

        nav a:hover { color: #315bea; }

        main {
            max-width: 1000px;
            margin: 55px auto;
            padding: 0 24px;
        }

        .hero {
            background: white;
            border: 1px solid #e7eaf0;
            border-radius: 18px;
            padding: 42px;
            margin-bottom: 32px;
        }

        .tag {
            display: inline-block;
            background: #edf2ff;
            color: #315bea;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
        }

        h1 {
            font-size: clamp(28px, 5vw, 40px);
            line-height: 1.2;
            margin: 18px 0 12px;
            letter-spacing: -1px;
        }

        h2 { font-size: 23px; margin-bottom: 8px; }

        .muted { color: #748094; }

        .button {
            display: inline-block;
            background: #315bea;
            color: white;
            padding: 11px 18px;
            border-radius: 9px;
            text-decoration: none;
            margin-top: 14px;
            font-size: 14px;
            font-weight: 600;
        }

        .button:hover { background: #2449c9; }

        .section-heading {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 12px;
            margin-bottom: 16px;
        }

        .section-heading h2 { margin: 0; }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 16px;
        }

        .course {
            background: white;
            border: 1px solid #e7eaf0;
            border-radius: 13px;
            padding: 22px;
            transition: transform .15s, box-shadow .15s;
        }

        .course:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 24px #2637540c;
        }

        .course-number {
            color: #315bea;
            font-size: 13px;
            font-weight: 700;
        }

        .course h3 { font-size: 16px; margin: 12px 0 0; }

        .info {
            background: white;
            border: 1px solid #e7eaf0;
            border-radius: 14px;
            padding: 26px;
        }

        footer {
            text-align: center;
            padding: 28px 20px;
            color: #8a94a6;
            font-size: 13px;
            border-top: 1px solid #e7eaf0;
            margin-top: 70px;
        }

        @media (max-width: 600px) {
            nav { padding: 16px 20px; }
            nav a:not(.logo) { margin-left: 12px; }
            main { margin-top: 30px; padding: 0 16px; }
            .hero { padding: 26px; }
        }
    </style>
</head>
<body>
    <nav>
        <a class="logo" href="/">StudentSpace.</a>
        <div>
            <a href="/">Главная</a>
            <a href="/courses">Дисциплины</a>
            <a href="/about">О проекте</a>
        </div>
    </nav>

    <main>
        {{ content|safe }}
    </main>

    <footer>
        StudentSpace · Учебный проект по DevOps · Python + Flask
    </footer>
</body>
</html>
"""


def page(title, content):
    return render_template_string(TEMPLATE, title=title, content=content)


@app.get("/")
def index():
    content = """
    <section class="hero">
        <span class="tag">STUDENT PORTAL</span>
        <h1>Твоя учёба.<br>В одном месте.</h1>
        <p class="muted">
            Информационная система студента для просмотра учебных дисциплин
        </p>
        <a class="button" href="/courses">Посмотреть дисциплины →</a>
    </section>

    <div class="section-heading">
        <h2>Что внутри</h2>
        <span class="muted">Основные возможности</span>
    </div>

    <div class="grid">
        <article class="course">
            <span class="course-number">01 / ОБУЧЕНИЕ</span>
            <h3>Учебные дисциплины</h3>
            <p class="muted">Список доступных предметов в одном месте</p>
        </article>
        <article class="course">
            <span class="course-number">02 / API</span>
            <h3>Доступ к данным</h3>
            <p class="muted">Получение информации в формате JSON.</p>
        </article>
        <article class="course">
            <span class="course-number">03 / DEVOPS</span>
            <h3>Автоматизация</h3>
            <p class="muted">Проверка кода с помощью GitHub Actions.</p>
        </article>
    </div>
    """
    return page("Главная", content)


@app.get("/courses")
def courses_page():
    items = "".join(
        f'<article class="course"><span class="course-number">'
        f'COURSE / {course["id"]:02}</span>'
        f'<h3>{course["name"]}</h3></article>'
        for course in COURSES
    )

    content = f"""
    <span class="tag">ОБУЧЕНИЕ</span>
    <h1>Учебные дисциплины</h1>
    <p class="muted">Все дисциплины собраны в одном месте</p>
    <div class="grid">{items}</div>
    """
    return page("Дисциплины", content)


@app.get("/about")
def about_page():
    content = """
    <span class="tag">О ПРОЕКТЕ</span>
    <h1>Student Information System</h1>
    <section class="info">
        <h2>Учебное приложение</h2>
        <p class="muted">
            Проект демонстрирует разработку веб-приложения и настройку
            автоматизированного CI/CD-конвейера.
        </p>
        <p><strong>Технологии:</strong> Python, Flask, pytest, GitHub Actions.</p>
        <p><strong>Проверки:</strong> автоматические тесты и проверка синтаксиса.</p>
        <p><strong>Конвейер:</strong> сборка артефакта и тестовое развёртывание.</p>
    </section>
    """
    return page("О проекте", content)


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.get("/api/courses")
def api_courses():
    return jsonify({"courses": COURSES}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
