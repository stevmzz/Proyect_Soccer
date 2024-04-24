import pandas as pd

# Crear un DataFrame con los datos
data = {
    'Resumen de Actividades y Explicación': [
        'Elaboración de interfaz gráfica inicial y funcionalidades básicas\n- Diseño de la interfaz gráfica.\n- Implementación de funcionalidades básicas como música de fondo y generación de enemigos.',
        'Reimplementación en Tkinter y desarrollo de lógica de juego\n- Rehíce la interfaz en Tkinter.\n- Desarrollé la lógica central del juego incluyendo la generación del laberinto y el movimiento del personaje.',
        'Finalización del movimiento del personaje y detalles estéticos\n- Finalicé la implementación del movimiento del personaje y añadí detalles estéticos al juego.',
        'Conexión de archivos y funcionalidades principales\n- Conecté los archivos del proyecto y añadí funcionalidades principales como la vida del personaje y la generación de la llave.',
        'Implementación de características adicionales y pulido de detalles\n- Añadí características adicionales como el sistema de ranking y pulí detalles estéticos y funcionales del juego.'
    ],
    'Semana': ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4', 'Semana 5'],
    'Horas Invertidas': ['20 horas', '25 horas', '25 horas', '25 horas', '25 horas']
}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel
excel_filename = 'resumen_actividades.xlsx'
df.to_excel(excel_filename, index=False)

print(f'Se ha guardado la tabla en el archivo: {excel_filename}')
