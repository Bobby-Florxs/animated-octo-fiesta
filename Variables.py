import csv
import datetime

# Definir la fecha de inicio del año 2024
start_date = datetime.date(2024, 1, 1)

# Definir la fecha de fin del año 2024
end_date = datetime.date(2024, 12, 31)

# Crear una lista para almacenar los datos de la semana
week_data = []

# Iterar a través de las semanas del año 2024
current_date = start_date
week_number = 1
while current_date <= end_date:
    # Calcular la fecha de inicio de la semana (lunes)
    start_of_week = current_date - datetime.timedelta(days=current_date.weekday())
    
    # Calcular la fecha de fin de la semana (domingo)
    end_of_week = start_of_week + datetime.timedelta(days=6)
    
    # Agregar los datos de la semana a la lista
    week_data.append([week_number, start_of_week.strftime('%d/%m/%Y'), end_of_week.strftime('%d/%m/%Y')])
    
    # Avanzar a la siguiente semana
    current_date = end_of_week + datetime.timedelta(days=1)
    week_number += 1

# Escribir los datos en un archivo CSV
with open('semanas_2024.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Escribir el encabezado
    writer.writerow(['Semana', 'Fecha de inicio', 'Fecha de fin'])
    
    # Escribir los datos de cada semana
    for data in week_data:
        writer.writerow(data)

print("Archivo CSV generado exitosamente.")
