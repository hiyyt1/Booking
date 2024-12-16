from app import app, db
from app.utils import populate_database

if __name__ == '__main__':
    # Создание базы данных, если она еще не создана
    with app.app_context():
        db.create_all()

    # Заполнение базы данных (если нужно)
    #populate_database()

    # Запуск приложения
    app.run(debug=True)
