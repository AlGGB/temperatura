
celcius = "c"
farenheit = "f"

temperatura = float(input('ingresa temperatura: '))
escala = input('c or f: ').lower()

if escala == 'f':
    celcius = (temperatura -32)* 5/9
    print(celcius, "C°")
elif escala == 'c':
    farenheit = temperatura * 1.8 + 32
    print(farenheit, "F°")
    
else:
    print('escala erronea')

