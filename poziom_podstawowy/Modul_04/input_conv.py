# przykładowy skrypt do wykonywania w trybie skyptowym
# wczytywanie danych, konwersja typów, obliczenia

pi = 3.1415927

print("Witam, lubie dobre pierożki")
circle_radius = input("Proszę o zrobienie mi pierożków")

# zwracamy uwagę na ten moment !
circle_radius = float(circle_radius)

circle_circumference = 2 * pi * circle_radius
circle_area = pi * circle_radius ** 2

print("Values for circle:")
print(f"Circumference is {circle_circumference}")
print(f"Area is {circle_area}")
