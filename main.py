#Создаем СТАТИЧЕСКОЕ приложение "Висилится" все объекты закреплены в определеных местах


from tkinter import *#Импортировали - скачали модуль для работы с интерефейсом
import random
import tkinter.font as tkFont
import pygame #импортировали библеотеку для разработки игр
pygame.init()#инициализировали pygame
pygame.mixer.init()#инициализировали mixer(микшер)

index = 0

screen = Tk()#Создали объект экрана
screen.geometry("1920x1080")#Метод для установки размеров экрана

strikethrough_font = tkFont.Font(family="Arial", size=40, overstrike=1)
#картинки

#Шаг 1: сохраняю путь к файлу в переменной (файл должен быть "PNG")
photo_hon = PhotoImage(file = "Picture/MainPicture.png")
photo_play = PhotoImage(file = "Picture/play_button.png")
photo_hon2 = PhotoImage(file="Picture/animals.png")
You_Lose = PhotoImage(file="Picture/YouLose.png")

#Висилица
palka1 = PhotoImage(file="Picture/palka_1.png")
palka2 = PhotoImage(file="Picture/palka_2.png")
palka3 = PhotoImage(file="Picture/palka_3.png")
palka4 = PhotoImage(file="Picture/palka_4.png")
palka5 = PhotoImage(file="Picture/palka_5.png")
palka6 = PhotoImage(file="Picture/palka_6.png")
palka7 = PhotoImage(file="Picture/palka_7.png")

#Музыка
oshibka = pygame.mixer.Sound("Sound/Oshibka.mp3")
oshibka.set_volume(1)

ugadal = pygame.mixer.Sound("Sound/Ugadal.mp3")
ugadal.set_volume(1)


pictures = [palka1, palka2, palka3, palka4, palka5, palka6, palka7]#сщхранили все картинки в список для автоматического переключения
actual_picture = pictures[0]#утановили изночальное изображение для висилицы

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
print(procherk_1)
jizni = 0

print(random_animal)

def click():
    global jizni
    global oshibka

    play_button.place_forget()  # place_forget скрывает виджет
    menu_label.place_forget()

    #сделали frame для сохранения виджетов
    Game_process = Frame(screen)
    Game_process.place(width=1920, height=1080, x=0, y=0)

    #label сохраняется на Game_process
    forestground = Label(Game_process, image=photo_hon2)
    forestground.place(x = 0, y = 0)

    palka1_ = Label(Game_process, image=actual_picture)
    palka1_.place(x = 730, y = 370)


    kategory_label = Label(Game_process, text="Угадай это слово")
    kategory_label.place(x = 960,y = 50)


    procherk = Label(Game_process, text=procherk_1, font=("Arial", 50))
    procherk.place(x = 1250, y = 900, width = 500, height = 100)


    alphabet = "abcdefghijklmnopqrstuvwxyz"
    button_width = 75
    button_height = 75
    button_x = -75
    button_y = 750
    otstup = 100
    otstup_y = 0

    def process_letter(bukva):
        global procherk_1
        global jizni
        global oshibka
        a = 0
        for widget in Game_process.winfo_children():  # Проходим по всем виджетам на экране
            if isinstance(widget, Button) and widget['text'] == bukva:
                widget.config(state="disable", background="gray")
                if jizni == 5:
                    print("Ты проиграл")
                    #Скрываем frame (и все виджеты на нем)
                    Game_process.place_forget()
                    You_Lose_ = Label(screen, image=You_Lose)
                    You_Lose_.place(width=1920, height=1080, x=0, y=0)
                if jizni < 6:
                    if bukva in random_animal:
                        for i in random_animal:
                            a = a+1
                            if i == bukva:
                                ugadal.play(0)
                                procherk_1 = procherk_1[:a*2-2] + bukva + " " + procherk_1[a*2:]
                                procherk.config(text=procherk_1)
                                print(procherk_1)
                    else:
                        jizni = jizni + 1
                        oshibka.play(0)#проиграли звук ошибки 1 раз
                        print(jizni)
                        actual_picture = pictures[jizni]#Устанавливаем картинку в зависимости от жизни
                        palka1_.config(image=actual_picture)#Проводим конфигурацию (меняем) картинки
                break  # Останавливаем цикл после обработки нужной кнопки

    for bukva in alphabet:#поочереди обращаемся к каждой букве алфавита
        if otstup_y != 8:#контролируем кол-во букв в одной строке
            button_x += otstup
            otstup_y += 1
        else:
            button_x = 25
            button_y += otstup
            otstup_y = 0

        # Создаём кнопку
        bukva_button = Button(
            Game_process,
            text=bukva,
            font=("Arial", 40),
            background="green",
            command=lambda b=bukva: process_letter(b)
        )
        bukva_button.place(x=button_x, y=button_y, width=button_width, height=button_height)#размещение букв на экране


#создфю виджет "button". Параметр command отвечает за действие после клика
play_button = Button(screen, image=photo_play, command=click)
#разместили виджет на экране, указали координаты и размеры виджета
play_button.place(x = 315,y = 450)

screen.mainloop()#Метод окна и взаимодействия с пользователей