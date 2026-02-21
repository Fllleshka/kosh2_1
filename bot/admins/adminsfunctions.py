# Библиотека для работы с Ботом
from aiogram import Router, F,types
from aiogram.types import Message, FSInputFile
# Импорт кнопок для админской панели
from bot.buttons.adminbuttons import AdminButtons
from bot.buttons.usersbuttons import Buttons
from bot.buttons.choosebuttons import returnreplymarkup
from database.baseclass import baseclass
# Библиотека для работы с базой данных
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
# Импорт движка для работы с базой
from database.baseclass import engine
from datetime import datetime
# Импорт бота
from create_bot import bot
# Библиотеки для работы с файлами
import os
import shutil
import openpyxl
from openpyxl.worksheet.page import PageMargins
from openpyxl.styles import Border, Side, Font, Alignment

from database.tablesclasses import Users, Towns, Kinds, Levels, Types, Places

# Создаём роутер
adminsfunctionsrouter = Router()

@adminsfunctionsrouter.message(F.text == Buttons.textautorisationadmin)
async def savedatabase(message: Message):
    text = "Вы вошли как администратор.\nФункционал отображается для администратора."
    markup = returnreplymarkup("adminsbutton", message.from_user.id)
    await message.answer(text, reply_markup=markup)

@adminsfunctionsrouter.message(F.text == AdminButtons.textsavedatabase)
async def savedatabase(message: Message):
    # Формируем название файла backup
    date = datetime.now()
    newnamefile = f"database_backup_{str(date.day)}.{date.month}.{date.year}_{date.hour}.{date.minute}.db"
    # Проверка файла базы данных на нахождение

    pathtodatabase = baseclass.databaseurl()
    pathtobackup = "database/backups/" + newnamefile
    try:
        shutil.copyfile(pathtodatabase, pathtobackup)
        text = f"База данных сохранена.\nНазвание файла:\n{newnamefile}"
        await message.answer(text)
    except Exception as e:
        print(e)

@adminsfunctionsrouter.message(F.text == AdminButtons.textalltrainer)
async def alltrainer(message: Message):
    # Формируем название файла backup
    date = datetime.now()
    namefile = f"database/files/alltrainers_{str(date.day)}.{date.month}.{date.year}_{date.hour}.{date.minute}.xlsx"
    title = "Отчёт по тренерам"
    nametable = 'Список всех аккаунтов тренеров'

    # Вызываем функцию формирования файла
    createfile(namefile, title, nametable, "Тренер")

    # Отправка сообщения
    file_to_send = FSInputFile(namefile)
    text = "Вот файл со всеми тренерами зарегистрированными в системе"
    await bot.send_document(chat_id = message.chat.id, caption = text, document = file_to_send)

@adminsfunctionsrouter.message(F.text == AdminButtons.textallathletes)
async def allathletes(message: Message):
    # Формируем название файла backup
    date = datetime.now()
    namefile = f"database/files/allathletes_{str(date.day)}.{date.month}.{date.year}_{date.hour}.{date.minute}.xlsx"
    title = "Отчёт по спортсменам"
    nametable = 'Список всех аккаунтов спортсменов'

    # Вызываем функцию формирования файла
    createfile(namefile, title, nametable, "Спортсмен")

    # Отправка сообщения
    file_to_send = FSInputFile(namefile)
    text = "Вот файл со всеми спортсменами зарегистрированными в системе"
    await bot.send_document(chat_id=message.chat.id, caption=text,
                            document=file_to_send)


# Функция создания и форматирования файла
def createfile(namefile, title, nametable, nametableindatabase):
    # Создаём рабочую книгу и активный лист
    workbook = openpyxl.Workbook()
    worklist = workbook.active
    worklist.title = title

    # Запись данных в таблицу
    # Формируем таблицу согласно шаблону
    # Обводка ячеек
    thin = Side(border_style="thin", color="000000")
    border = Border(top=thin, left=thin, right=thin, bottom=thin)
    # Ориентация
    worklist.page_setup.orientation = 'landscape'
    # Поля
    worklist.page_margins = PageMargins(left=0.25, right=0.25, top=0.5,
                                        bottom=0.5)
    # Озаглавливание таблицы
    worklist.merge_cells('A1:I1')
    font_style_table_name = Font(name="Times New Roman", size=14, bold=True)
    worklist['A1'] = nametable
    worklist['A1'].font = font_style_table_name
    worklist['A1'].alignment = Alignment(horizontal='center', vertical='center')

    # Озаглавливаем столбцы
    mass_colums = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    mass_width = [3.5, 35, 10, 8, 11, 17, 14, 21, 14]
    name_colums = ["№", "ФИО", "Дата рождения", "Рейтинг", "TelegramID", "Город", "Уровень", "Место", "Описание"]


    for elem in range(0, len(mass_colums)):
        worklist.column_dimensions[mass_colums[elem]].width = mass_width[elem]
        name_cell = mass_colums[elem] + "2"
        cell = worklist[name_cell]
        cell.value = name_colums[elem]
        cell.border = border
        cell.alignment = Alignment(wrap_text = True, horizontal = "center", vertical = "center")

    worklist.row_dimensions[2].height = 30

    data = importdatesfrombase(nametableindatabase)

    index = 0
    for user, town, kind, level, type, place in data:
        for element in mass_colums:
            # print(f"\t\t{element}")
            # Вставляем номер строки
            name_cell = element + str(index + 3)
            cell = worklist[name_cell]
            # print(f"\t\t{cell}")
            match (element):
                # Номер строки
                case "A":
                    # print(f"\tA\t{index}")
                    cell.value = index
                # ФИО
                case "B":
                    # print(f"\tB\t{user.first_name} {user.middle_name} {user.last_name}")
                    cell.value = f"{user.first_name} {user.middle_name} {user.last_name}"
                # Дата рождения
                case "C":
                    # print(f"\tC\t{user.birth_date}")
                    cell.value = user.birth_date
                # Рейтинг
                case "D":
                    # print(f"\tD\t{user.rating}")
                    cell.value = user.rating
                # TelegramID
                case "E":
                    # print(f"\tE\t{user.id_telegram}")
                    if user.id_telegram == 0:
                        cell.value = "FAKE ACC"
                    else:
                        cell.value = user.id_telegram
                # Город
                case "F":
                    # print(f"\tF\t{town.name}")
                    cell.value = town.name
                # Уровень
                case "G":
                    # print(f"\tG\t{level.name}")
                    cell.value = level.name
                # Место
                case "H":
                    # print(f"\tH\t{place.name}")
                    cell.value = place.name
                # Описание
                case "I":
                    # print(f"\tI\t{user.description}")
                    if user.description == "":
                        cell.value = " "
                    else:
                        cell.value = user.description
                case _:
                    pass
            cell.border = border
        index += 1

    # Сохраняем файл
    workbook.save(namefile)

# Функция импорта данных их базы
def importdatesfrombase(nametable):
    # Получение данных из базы
    # Создаём сессию
    Session = sessionmaker(bind=engine)
    with Session() as session:
        sqlquerty = (
            select(Users, Towns, Kinds, Levels, Types, Places)
            .join(Towns, Users.id_town == Towns.id_town)
            .join(Kinds, Users.id_kind == Kinds.id_kind)
            .join(Levels, Users.id_level == Levels.id_level)
            .join(Types, Users.id_type == Types.id_type)
            .join(Places, Users.id_place == Places.id_place)
            .filter(Types.name == nametable)
        )
        resultquerty = session.execute(sqlquerty).all()

    return resultquerty