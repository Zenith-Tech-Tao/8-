import turtle

# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Создание черепашки
pen = turtle.Turtle()
pen.speed(10)

# Функция для рисования сердца
def draw_heart():
    pen.fillcolor("red")
    pen.begin_fill()
    pen.left(140)
    pen.forward(224)
    pen.circle(-112, 200)
    pen.left(120)
    pen.circle(-112, 200)
    pen.forward(224)
    pen.end_fill()

# Функция для рисования текста
def draw_text():
    pen.penup()
    pen.goto(0, 200)  # Позиция для текста
    pen.pendown()
    pen.color("black")  # Цвет текста
    pen.write("С 8 марта тебя", align="center", font=("Arial", 24, "bold"))

# Функция для рисования имени
def draw_name():
    pen.penup()
    pen.goto(0, -30)
    pen.pendown()
    pen.color("white")  # Цвет текста
    pen.write("Миранда", align="center", font=("Arial", 24, "bold"))

# Функция для рисования дополнительного текста
#def draw_additional_text():
    #pen.penup()
    #pen.goto(150, -200)  # Позиция для дополнительного текста
    #pen.pendown()
    #pen.color("black")  # Цвет текста
    #pen.write("где кружки?)", align="right", font=("Arial", 12, "normal"))

# Рисуем сердце
pen.penup()
pen.goto(0, -200)
pen.pendown()
draw_heart()

# Рисуем текст в верхнем центре
draw_text()

# Рисуем имя в центре сердца
draw_name()

# Рисуем дополнительный текст в нижнем правом углу
#draw_additional_text()

# Завершение работы
turtle.done()
