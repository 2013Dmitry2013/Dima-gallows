
from tkinter import *#Импортировали - скачали модуль для работы с интерефейсом
import random
import tkinter.font as tkFont

screen = Tk()#Создали объект экрана
screen.geometry("1920x1080")#Метод для установки размеров экрана

strikethrough_font = tkFont.Font(family="Obelix Pro", size=40, overstrike=1)
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

    def a():
        a_button.config(state="disable", background="red", font=strikethrough_font)

    a_button = Button(screen, text="a", font=("Obelix Pro", 40), command=a, background="green")
    a_button.place(x=500, y=800,  width=75, height = 75)

#создфю виджет "button". Параметр command отвечает за действие после клика
play_button = Button(screen, image=photo_play, command=click)
#разместили виджет на экране, указали координаты и размеры виджета
play_button.place(x = 315,y = 450)

music_button = Button()

screen.mainloop()#Метод окна и взаимодействия с пользователей