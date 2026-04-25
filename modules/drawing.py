import turtle


def setup_drawing():
    # Создаём черепашку
    t = turtle.Turtle()
    t.ondrag(t.goto)
    screen = turtle.Screen()

    # Настройки
    screen.title("Рисовалка с черепашкой")
    screen.bgcolor("white")
    screen.setup(800, 600)

    # Настройки черепашки
    t.shape("turtle")  # Форма черепашки (можно "circle", "arrow" и др.)
    t.pensize(3)  # Толщина линии
    t.speed(0)  # 0 - максимальная скорость
    t.pencolor("deep pink")

    # Функции рисования
    def draw(x, y):
        t.pendown()
        t.goto(x, y)

    def move_without_draw(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def clear_all():
        t.clear()  # Очистить рисунок
        t.penup()
        t.home()  # Вернуться в центр
        t.pendown()
        t.pencolor("deep pink")

    def change_color_red():
        t.pencolor("red")

    def change_color_blue():
        t.pencolor("blue")

    def change_color_green():
        t.pencolor("green")

    def change_color_black():
        t.pencolor("black")

    # Привязываем события мыши
    t.ondrag(t.goto)  # Рисовать при движении с зажатой кнопкой
    screen.onclick(move_without_draw, 1)  # Переместить черепашку без рисования

    # Клавиши для очистки и смены цвета
    screen.onkey(clear_all, "c")  # Нажми C для очистки
    screen.onkey(change_color_red, "r")  # R - красный
    screen.onkey(change_color_blue, "b")  # B - синий
    screen.onkey(change_color_green, "g")  # G - зелёный
    screen.onkey(change_color_black, "k")  # K - чёрный
    screen.onkey(lambda: t.pensize(t.pensize() + 1), "Up")  # Стрелка вверх - толще
    screen.onkey(lambda: t.pensize(max(1, t.pensize() - 1)), "Down")  # Стрелка вниз - тоньше

    # Инструкция
    screen.listen()  # Слушаем нажатия клавиш

    print("=== Управление ===")
    print("Рисуй мышкой (зажми левую кнопку и води)")
    print("Кликни мышкой - переместить черепашку")
    print("C - очистить")
    print("R, G, B, K - цвет (красный, зелёный, синий, чёрный)")
    print("↑ ↓ - толщина линии")

    turtle.mainloop()


if __name__ == "__main__":
    setup_drawing()