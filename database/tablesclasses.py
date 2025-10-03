# Библиотека для работы с базой данных
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker
from sqlalchemy import Integer, String, ForeignKey
# Импорт базового класса Base
from database.baseclass import Base
# Импорт библиотеки для создания случайных данных
from faker import Faker
# Библиотека для логирования
import logging
# Импорт движка для работы с базой
from database.baseclass import engine
# Импорт данных из файла dates
from database.dates import dates_for_database

# Города
class Towns(Base):
    __tablename__ = "town"

    id_town: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=True)

# Виды спорта
class Kinds(Base):
    __tablename__ = "kind_sport"
    id_kind: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

# Уровни спорта
class Levels(Base):
    __tablename__ = "level_training"
    id_level: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

# Типы аккаунтов
class Types(Base):
    __tablename__ = "accaunt_type"
    id_type: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

# Места проведения
class Places(Base):
    __tablename__ = "place"
    id_place: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

# Пользователи
class Users(Base):
    __tablename__ = "users"
    id_user: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    middle_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    birth_date: Mapped[str] = mapped_column(String(50))
    rating: Mapped[int] = mapped_column(Integer)
    id_telegram: Mapped[int] = mapped_column(Integer)
    id_town: Mapped[int] = mapped_column(ForeignKey("town.id_town"))
    id_kind: Mapped[int] = mapped_column(ForeignKey("kind_sport.id_kind"))
    id_level: Mapped[int] = mapped_column(ForeignKey("level_training.id_level"))
    id_type: Mapped[int] = mapped_column(ForeignKey("accaunt_type.id_type"))
    id_place: Mapped[int] = mapped_column(ForeignKey("place.id_place"))
    description: Mapped[str] = mapped_column(String(300))

# Функции добавления таблиц в БД
def create_town(town: Towns, session) -> None:
    session.add(town)
def create_kinds(kind: Kinds, session) -> None:
    session.add(kind)
def create_levels(level: Levels, session) -> None:
    session.add(level)
def create_types(type: Types, session) -> None:
    session.add(type)
def create_places(place: Places, session) -> None:
    session.add(place)
def create_users(user: Users, session) -> None:
    session.add(user)

# Главная функция генерации таблиц и данных в БД
def create_all_databases():
    logging.info(f"Начинаем создание первоначальной базы данных")
    # Создаём сессию
    Session = sessionmaker(engine)
    Base.metadata.create_all(engine)
    with Session() as session:
        try:
            # Города
            for element in dates_for_database.towns:
                create_town(Towns(name=element), session)
            # Виды
            for element in dates_for_database.kinds:
                create_kinds(Kinds(name=element), session)
            # Уровни
            for element in dates_for_database.levels:
                create_levels(Levels(name=element), session)
            # Роли
            for element in dates_for_database.types:
                create_types(Types(name=element), session)
            # Места
            for element in dates_for_database.places:
                create_places(Places(name=element), session)

            # Пользователи
            # Список тестовых пользователей
            fake = Faker("ru_RU")
            for element in range(0,20):
                # Мужчины
                if fake.boolean() == True:
                    create_users(Users(
                        first_name = fake.first_name_male(),
                        middle_name = fake.middle_name_male(),
                        last_name = fake.last_name_male(),
                        birth_date = fake.date_of_birth(minimum_age=15, maximum_age=40).strftime("%d.%m.%Y"),
                        rating = fake.random_int(min=0, max=60),
                        id_telegram = 0,
                        id_town = fake.random_int(min=0, max=18),
                        id_kind = fake.random_int(min=0, max=18),
                        id_level = fake.random_int(min=0, max=2),
                        id_type = fake.random_int(min=0, max=1),
                        id_place =  fake.random_int(min=0, max=3),
                        description = ""), session)
                # Женщины
                else:
                    create_users(Users(
                        first_name = fake.first_name_female(),
                        middle_name = fake.middle_name_female(),
                        last_name = fake.last_name_female(),
                        birth_date = fake.date_of_birth(minimum_age=15, maximum_age=40).strftime("%d.%m.%Y"),
                        rating = fake.random_int(min=0, max=60),
                        id_telegram = 0,
                        id_town = fake.random_int(min=0, max=18),
                        id_kind = fake.random_int(min=0, max=18),
                        id_level = fake.random_int(min=0, max=2),
                        id_type = fake.random_int(min=0, max=1),
                        id_place =  fake.random_int(min=0, max=3),
                        description = ""), session)
            logging.info("База данных успешно сгенерированная и заполнена тестовыми данными")
        except:
            session.rollback()
            raise
        else:
            session.commit()

# Функция добавления данных в базу данных
def insert_user_dates_in_database(data):
    logging.info("Функция вставки данных в базу")
    Session = sessionmaker(engine)
    Base.metadata.create_all(engine)
    with Session() as session:
        create_users(Users(
            first_name=data['firstname'],
            middle_name=data['middlename'],
            last_name=data['lastname'],
            birth_date=data['age'],
            rating=0,
            id_telegram=data['telegramid'],
            id_town=1,
            id_kind=1,
            id_level=1,
            id_type=1,
            id_place=1,
            description=data['discription']), session)
    session.commit()
    logging.info("Данные успешно добавлены в базу данных")
    '''
    text = bot_messages.messagefinalregistration
    text += "\n\n"
    text += "[" + str(dates['telegramid']) + "]\n"
    text += "Имя:\n        " +  + "\n"
    text += "Фамилия:\n        " +  + "\n"
    text += "Отчество:\n        " +  + "\n"
    text += "Дата рождения:\n        " + dates['age'] + "\n"
    text += "Город:\n        " + dates['town'] + "\n"
    text += "Тип спорта:\n        " + dates['typesport'] + "\n"
    text += "Уровень подготовки:\n        " + dates['levelsport'] + "\n"
    text += "Место подготовки:\n        " + dates['place'] + "\n"
    text += "Тип аккаунта:\n        " + dates['typeaccaunt'] + "\n"
    text += "Картинка:\n        " + dates['imageuser'] + "\n"
    text += "Описание:\n        " +  + "\n"
    '''
