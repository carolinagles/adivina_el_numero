"""
Historial de partidas

- Mostrar en formato tabla la ultimas 20 partidas 
- Mejores Jugadores en gráfico de barras.
- Gráfico de pastele para ganados/perdidos.



"""
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
from .configuraciones import estadisticas


def historial():
    while True:
        print("\n1. Últimas 20 Partidas\n2. Mejores Jugadores\n3. Partidas Ganadas o Perdidas\n4. Regresar\n")
        opcion=input("Selecciona una opción númerica: ")
        
        if opcion == '1':
            ultimas_partidas()
        elif opcion == '2':
            mejores_jugadores()            
        elif opcion == '3':
            graf_partidas()
        elif opcion == '4':
            break
        else:
            print("Selecciona una opción entre 1-3: ")

            
# Últimas partidas            
def ultimas_partidas():
    print("\n   Últimas partidas")
    display(pd.read_excel(estadisticas).tail(20))


# Mejores jugadores

def mejores_jugadores():
    df = pd.read_excel(estadisticas)
    jugadores_ganadas = df[df['Resultado'] == 'Ganado']['Nombre'].value_counts().plot.bar(
        title="Mejores 3 Jugadores",
        color="cornflowerblue",
        edgecolor="white"
    )
    plt.ylabel("Victorias")
    plt.xlabel('')
    plt.xticks(rotation=45)
    plt.show()
    
# Gráficos 

def graf_partidas():
    df = pd.read_excel(estadisticas)
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 3))

    # generales    
    resultado_generales = df['Resultado'].value_counts().plot.pie(
        ax=ax1,
        title="Partidas Generales",
        shadow=True,
        colors=["mediumseagreen", "tomato"],
        autopct=lambda p: f'{p * sum(df["Resultado"].value_counts()) / 100:.0f}'
    )
    ax1.set_ylabel('')
    
    # solitarios
    resultado_solitarios = df[df['Modo']=="Solitario"]['Resultado'].value_counts().plot.pie(
        ax=ax2,
        title="Partidas Solitarias",
        shadow=True,
        colors=["mediumseagreen", "tomato"],
        autopct=lambda p: f'{p * sum(df["Resultado"].value_counts()) / 100:.0f}'
    )
    ax2.set_ylabel('')

    # dobles
    resultado_dobles = df[df['Modo']=="Doble"]['Resultado'].value_counts().plot.pie(
        ax=ax3,
        title="Partidas Dobles",
        shadow=True,
        colors=["mediumseagreen", "tomato"],
        autopct=lambda p: f'{p * sum(df["Resultado"].value_counts()) / 100:.0f}'
    )
    ax3.set_ylabel('')
    plt.show()