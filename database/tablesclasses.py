# Библиотека для работы с базой данных
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker
from sqlalchemy import Integer, String, ForeignKey, select
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
        try:
            create_users(Users(
                first_name=data['firstname'],
                middle_name=data['middlename'],
                last_name=data['lastname'],
                birth_date=data['age'],
                rating=0,
                id_telegram=data['telegramid'],
                id_town=find_id_in_table('towns', data['town']),
                id_kind=find_id_in_table('kinds', data['typesport']),
                id_level=find_id_in_table('levels', data['levelsport']),
                id_type=find_id_in_table('type', data['typeaccaunt']),
                id_place=find_id_in_table('places', data['place']),
                description=data['discription']), session)
        except:
            session.rollback()
            raise
        else:
            session.commit()
            logging.info("Данные успешно добавлены в базу данных")

# Функция поиска id в базе данных
def find_id_in_table(nametable, data):
    Session = sessionmaker(engine)
    Base.metadata.create_all(engine)
    with Session() as session:
        try:
            match(nametable):
                case "towns":
                    id = session.scalar(select(Towns).where(Towns.name == data))
                    return id.id_town
                case "kinds":
                    id = session.scalar(select(Kinds).where(Kinds.name == data))
                    return id.id_kind
                case "levels":
                    id = session.scalar(select(Levels).where(Levels.name == data))
                    return id.id_level
                case "type":
                    id = session.scalar(select(Types).where(Types.name == data))
                    return id.id_type
                case "places":
                    id = session.scalar(select(Places).where(Places.name == data))
                    return id.id_place
                case _:
                    return None
        except Exception as e:
            print(e)

def find_name_in_table(nametable, id):
    Session = sessionmaker(engine)
    Base.metadata.create_all(engine)
    with Session() as session:
        try:
            match (nametable):
                case "towns":
                    name = session.scalar(select(Towns).where(Towns.id_town == id))
                    return name.name
                case "kinds":
                    name = session.scalar(select(Kinds).where(Kinds.id_kind == id))
                    return name.name
                case "levels":
                    name = session.scalar(select(Levels).where(Levels.id_level == id))
                    return name.name
                case "type":
                    name = session.scalar(select(Types).where(Types.id_type == id))
                    return name.name
                case "places":
                    name = session.scalar(select(Places).where(Places.id_place == id))
                    return name.name
                case _:
                    return None
        except Exception as e:
            print(e)

# Функция поиска всех данных по id
def find_all_data_from_database(userid):
    Session = sessionmaker(engine)
    Base.metadata.create_all(engine)
    with Session() as session:
        try:
            data = session.scalar(select(Users).where(Users.id_telegram == userid))
            return data
        except Exception as e:
            return None