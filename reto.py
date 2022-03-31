# Declaracion de variables
ancho = int(input('Digite el ancho del rectangulo: '))
altura = int(input('Digita la altura del rectangulo: '))

# Calcular area y perimetro
area = altura*ancho
perimetro = (ancho*2) + (altura*2)

# Imprimir resultados
print(f'El area es: {area}')
print(f'El perimero es: {perimetro}')

for a in range (1,altura+1):
    for l in range (1,ancho+1):
        print('*', end=' ')
    print('')