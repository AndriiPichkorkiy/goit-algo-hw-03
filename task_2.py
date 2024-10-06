import turtle


def koch_curve(t: turtle.Turtle, order: int, size: int) -> None:
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_curve(order: int, size=150):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size * 1.5)
    t.pendown()

    koch_curve(t, order, size)

    for _ in range(5):
        t.left(-60)
        koch_curve(t, order, size)

    window.mainloop()


if __name__ == "__main__":
    # Виклик функції
    draw_koch_curve(2)
