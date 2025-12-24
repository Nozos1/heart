# love_heart_anim.py
import math
import turtle as t

# --- konfiguracja okna/turtle ---
t.setup(width=800, height=800)
t.bgcolor("black")
t.hideturtle()
t.speed(0)
t.pensize(1)
t.color("red")
t.delay(0)          # bez sztucznego opóźnienia
t.tracer(False)     # ręczna kontrola odświeżania

# parametry krzywej serca (x(t), y(t))
def heart_point(theta, scale=12):
    x = 16 * math.sin(theta)**3
    y = (13*math.cos(theta)
         - 5*math.cos(2*theta)
         - 2*math.cos(3*theta)
         -     math.cos(4*theta))
    return scale*x, scale*y

def draw_ray(theta, steps=60):
    """Animuje pojedynczy promień od (0,0) do punktu na krzywej serca."""
    x, y = heart_point(theta)
    t.penup(); t.goto(0, 0); t.pendown()
    # rośnij w małych krokach i odświeżaj ekran
    for k in range(1, steps + 1):
        t.goto(x * k/steps, y * k/steps)
        t.update()

def main():
    rays = 1000          # ile promieni (gęstość)
    growth_steps = 1   # w ilu „klatkach” rośnie każdy promień
    for i in range(rays):
        theta = (2*math.pi) * i / rays
        draw_ray(theta, steps=growth_steps)
    t.done()

if __name__ == "__main__":
    main()
