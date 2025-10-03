# Импорт базового класса модели таблиц БД
from sqlalchemy.orm import DeclarativeBase
# Импорт данных для движка
from sqlalchemy import create_engine

# Библиотека для логирования
import logging
# Библиотека для работы с файлами
import os

# Базовый класс наследуемый из класса библиотеки
class Base(DeclarativeBase):

    # Функция проверки наличия файла базы данных
    def checkdatabase(self):
        pathtodatabase = self.databaseurl()
        if(os.path.exists(pathtodatabase) == True):
            logging.info(f"База данных существует. Расположение: {pathtodatabase}")
            return True
        else:
            logging.info(f"База данных не существует. Расположение: {pathtodatabase}")
            return False

    # Функция вычисления правильного асботютного пути до базы
    def databaseurl(self):
        # Получаем директорию скрипта
        current_dir = os.path.dirname(os.path.abspath(__file__))
        #logging.info("Current DIR: " + current_dir)
        # Создаём полный путь к базе данных
        db_file_path = os.path.join(current_dir, 'my_database.db')
        #logging.info("DB FILE PATH: " + db_file_path)
        # Создаём правильный путь для работы
        #database_url = f"sqlite:///{db_file_path}"
        #logging.info("DATABASE URL: " + database_url)
        return db_file_path

    # Создание пути для движка
    def pathforengine(self):
        pathtofile = self.databaseurl()
        pathtopaste = f"sqlite:///{pathtofile}"
        return pathtopaste

baseclass = Base()
# Создание движка для работы с БД
engine = create_engine(baseclass.pathforengine())