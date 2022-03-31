# Variable del contador de intentos
intentos = 1

# Ciclo for para calcular numero de intentos
for var in range (0,5):
    user = input('User: ')
    password = input('Password: ')
    if (user != 'admin' and password != 'admin123'):
        intentos += 1
    else:
        print(f'Has iniciado con {intentos} intentos')