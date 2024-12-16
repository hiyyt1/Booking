import csv
from app import db
from app.models import News

# Функция для заполнения базы данных из CSV
def populate_database():
    with open('date.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        count = 0
        for row in reader:
            count+=1
            if count == 1: continue
            if len(row) == 8:
                news_item = News(
                    href=row[1],
                    title=row[2],
                    short_text=row[3],
                    full_text=row[4],
                    pub_date=row[5],
                    pub_time=row[6],
                    tag=row[7]
                )
                db.session.add(news_item)
        db.session.commit()
