# Библиотека для работы с базой данных
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
# Импорт движка для работы с базой
from database.baseclass import engine
# Импорт класса для выборки
from database.tablesclasses import Towns, Kinds, Levels, Places, Types
# Импорт базового класса Base
from database.baseclass import Base

class selectdatesfromDB:

    def __init__(self):
        Base.metadata.create_all(bind=engine)
        # Создаём сессию
        self.Session = sessionmaker(engine)

    # Получение всех городов
    def selecttowns(self):
        with self.Session(autoflush=False, bind=engine) as db:
            # получение всех объектов
            towns = db.query(Towns).all()
            return towns

    # Получение всех типов спорта
    def selectypessport(self):
        with self.Session(autoflush=False, bind=engine) as db:
            # получение всех объектов
            kinds = db.query(Kinds).all()
            return kinds

    # Получение всех уровней подготовки
    def selectleveltraining(self):
        with self.Session(autoflush=False, bind=engine) as db:
            # получение всех объектов
            levels = db.query(Levels).all()
            return levels

    # Получение всех мест тренировок
    def selectplacetraining(self):
        with self.Session(autoflush=False, bind=engine) as db:
            # получение всех объектов
            places = db.query(Places).all()
            return places

    # Получение всех типов аккаунта
    def selecttypeaccaunt(self):
        with self.Session(autoflush=False, bind=engine) as db:
            # получение всех объектов
            types = db.query(Types).filter(Types.name != "Администратор").all()
            return types