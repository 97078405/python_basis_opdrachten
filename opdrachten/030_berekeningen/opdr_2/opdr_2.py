# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

def c_to_f(c):
    return c * (9/5) + 32

def f_to_c(f):
    return (f - 32) * (5/9)

c = -12
f = 102

fahreinheit = c_to_f(c)
celsius = f_to_c(f)

print(f"{c} graden Celsius is gelijk aan {fahreinheit:.1f} graden Fahrenheit")
print(f"{f} graden Fahrenheit is gelijk aan {celsius:.1f} graden Celsius")

c = 62.2
f = 96

fahreinheit = c_to_f(c)
celsius = f_to_c(f)

print(f"{c} graden Celsius is gelijk aan {fahreinheit:.1f} graden Fahrenheit")
print(f"{f} graden Fahrenheit is gelijk aan {celsius:.1f} graden Celsius")

