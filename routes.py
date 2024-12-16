from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import News

# Главная страница - отображение всех новостей и статистики
@app.route('/')
def index():
    # Получаем все новости
    news_items = News.query.all()

    # 1. Получаем топ-5 тегов (считаем, сколько раз каждый тег встречается)
    top_tags = db.session.execute('SELECT tag, COUNT(*) FROM news GROUP BY tag ORDER BY COUNT(*) DESC LIMIT 5').fetchall()

    # 2. Получаем количество новостей по каждому дню (группируем по дате публикации)
    news_by_date = db.session.execute('SELECT pub_date, COUNT(*) FROM news GROUP BY pub_date ORDER BY pub_date DESC LIMIT 5').fetchall()

    # 3. Получаем среднее количество символов в новостях
    avg_char_count = db.session.execute('SELECT AVG(LENGTH(full_text)) FROM news').fetchone()[0]  # Извлекаем число

    # 4. Получаем общее количество новостей
    total_news_count = db.session.execute('SELECT COUNT(*) FROM news').fetchone()[0]

    # 5. Получаем день с максимальным количеством новостей
    max_news_day = db.session.execute('SELECT pub_date, COUNT(*) FROM news GROUP BY pub_date ORDER BY COUNT(*) DESC LIMIT 1').fetchone()

    return render_template('index.html', 
                           news_items=news_items, 
                           top_tags=top_tags, 
                           news_by_date=news_by_date, 
                           avg_char_count=avg_char_count,
                           total_news_count=total_news_count,
                           max_news_day=max_news_day)  # Передаем день с максимальным количеством новостей

# Страница для добавления статьи
@app.route('/add_article', methods=['GET', 'POST'])
def add_article():
    if request.method == 'POST':
        # Сбор данных из формы
        href = request.form['href']
        title = request.form['title']
        short_text = request.form['short_text']
        full_text = request.form['full_text']
        pub_date = request.form['pub_date']
        pub_time = request.form['pub_time']
        tag = request.form['tag']

        # Создание нового объекта News
        news = News(
            href=href,
            title=title,
            short_text=short_text,
            full_text=full_text,
            pub_date=pub_date,
            pub_time=pub_time,
            tag=tag
        )

        # Добавление новости в базу данных
        db.session.add(news)
        db.session.commit()

        return redirect(url_for('index'))  # Перенаправление на главную страницу

    return render_template('add_article.html')  # Отображение формы для добавления новости

# Страница полной статьи
@app.route('/article/<int:id>')
def article(id):
    # Получаем новость по её ID
    news_item = News.query.get_or_404(id)

    return render_template('article.html', news_item=news_item)
