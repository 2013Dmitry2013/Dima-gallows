
from tkinter import *#Импортировали - скачали модуль для работы с интерефейсом
import random
import tkinter.font as tkFont

screen = Tk()#Создали объект экрана
screen.geometry("1920x1080")#Метод для установки размеров экрана

strikethrough_font = tkFont.Font(family="Arial", size=40, overstrike=1)
#картинки

#Шаг 1: сохраняю путь к файлу в переменной (файл должен быть "PNG")
photo_hon = PhotoImage(file = "Picture/MainPicture.png")
photo_play = PhotoImage(file = "Picture/play_button.png")

#Шаг 2: создаю виджет - "label" указываю родителя, указываю изображение прикрепленное к виджету
menu_label = Label(screen, image=photo_hon)
#Шаг 3: спомощью метода "place" размещаю "label" на зкране
menu_label.place(x = 0, y = 0)

# Создаем список с 10 животными
animals = ["lion", "tiger", "elephant", "giraffe", "zebra", "kangaroo", "panda", "leopard", "wolf", "cat"]
# Случайный индекс
random_index = random.randint(0, len(animals) - 1)

# Извлекаем элемент по случайному индексу
random_animal = animals[random_index]
bukvi = len(random_animal)
procherk_1 = "_ " * bukvi#скопировали текст нужное кол-во раз

def click():
    play_button.place_forget()  # place_forget скрывает виджет
    menu_label.place_forget()


    kategory_label = Label(screen, text="Угадай это слово")
    kategory_label.place(x = 960,y = 50)


    procherk = Label(screen, text=procherk_1, font=("Arial", 50))
    procherk.place(x = 960, y = 700, width = 500, height = 100)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    button_width = 75
    button_height = 75
    button_x = -75
    button_y = 750
    otstup = 100
    otstup_y = 0

    def process_letter(bukva):
        for widget in screen.winfo_children():  # Проходим по всем виджетам на экране
            if isinstance(widget, Button) and widget['text'] == bukva:
                widget.config(state="disable", background="gray")
                break  # Останавливаем цикл после обработки нужной кнопки

    for bukva in alphabet:
        if otstup_y != 8:
            button_x += otstup
            otstup_y += 1
        else:
            button_x = 25
            button_y += otstup
            otstup_y = 0

        # Создаём кнопку
        bukva_button = Button(
            screen,
            text=bukva,
            font=("Arial", 40),
            background="green",
            command=lambda b=bukva: process_letter(b)
        )
        bukva_button.place(x=button_x, y=button_y, width=button_width, height=button_height)


#создфю виджет "button". Параметр command отвечает за действие после клика
play_button = Button(screen, image=photo_play, command=click)
#разместили виджет на экране, указали координаты и размеры виджета
play_button.place(x = 315,y = 450)

screen.mainloop()#Метод окна и взаимодействия с пользователей