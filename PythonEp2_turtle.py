import turtle
t = turtle.Pen()
t.shape('turtle')
t.speed(20)

def Circlr(m):
    for i in range(10):
        n=10
        while n <= m:
            t.circle(n)
            n = n+10
        t.lt(36)

Circlr(150)
