import turtle


bob = turtle.Turtle()
print(bob)

# for i in range(4):
#     bob.fd(100)
#     bob.lt(90)
# turtle.mainloop()

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
polygon(bob, 8, 70)


