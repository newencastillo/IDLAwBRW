'''Vamos a intentar estimar los parámetros a y b de la elipse
 generada por el crecimiento del cluster bajo percolaciones aleatorias'''

import BRW
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""Idea 1: si los parametros a y b de la elipse son un factor que se escala
entoncces se tiene que Area = \pi (a*S) (b*S)
=> S = sqrt(Area/abpi)
Luego podemos ver como varía esta escala dependiendo de los parametros de descarte horizontal y vertical de la percolacion"""

def generar_resultados():
    resultados = []

    for N in [1000, 2000, 3000, 4000]:
        for p_hor in [0.2, 0.3, 0.4, 0.5, 0.6]:
            for p_ver in np.linspace(0,0.8-p_hor,4):
                newen = BRW.BRW_IDLA_PERC(0.0) # Creamos un idla con percolacion SIN BRANCHING
                newen.crear_perc(100, p_ver, p_hor)

                # Hacer crecer el cluster hasta tamaño N (esto deberia ser un metodo interno de brw u.u)
                print("Empezando simulacion (N,ph,pv)", N, p_hor, p_ver)
                while newen.N < N:
                    if newen.vacio:
                        newen.crear_particula()
                    newen.actualizar()

                # Ya llegamos al punto en el que queriamos estar ahora registramos a y b
                
                a, b = newen.obtener_parametros()
                S = N / (a*b*np.pi)
                resultados.append({
                    "N": N,
                    "p_hor": p_hor,
                    "p_ver": p_ver,
                    "a": a,
                    "b": b,
                    "S": S })
                
    return resultados


def main():    

    resultados = generar_resultados()
    with open("resultados.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=resultados[0].keys())
        writer.writeheader()
        writer.writerows(resultados)

def segundomain():
    # 1) Cargar el CSV
    df = pd.read_csv("resultados.csv")

    # 2) Obtener niveles únicos de p_hor y p_ver
    p_hors = sorted(df["p_hor"].unique())
    p_vers = sorted(df["p_ver"].unique())

    # 3) Crear matriz S (heatmap)
    Z = np.zeros((len(p_vers), len(p_hors)))

    for i, pver in enumerate(p_vers):
        for j, phor in enumerate(p_hors):
            fila = df[(df["p_ver"] == pver) & (df["p_hor"] == phor)]
            if not fila.empty:
                Z[i, j] = fila["S"].values[0]
            else:
                Z[i, j] = np.nan   # por si falta algún valor

    # 4) Dibujar heatmap
    plt.figure(figsize=(8,6))
    plt.pcolormesh(p_hors, p_vers, Z, shading="auto")
    plt.colorbar(label="S")
    plt.xlabel("p_hor")
    plt.ylabel("p_ver")
    plt.title("Heatmap de S según p_hor y p_ver")
    plt.tight_layout()
    plt.show()

def tercermain():
    # Leer CSV
    df = pd.read_csv("resultados.csv")

    # Crear figura 3D
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111, projection='3d')

    # Scatter 3D
    p = ax.scatter(
        df["p_hor"],
        df["p_ver"],
        df["S"],
        c=df["N"],     # color según N
        cmap="viridis",
        s=60
    )

    # Barra de colores
    cbar = plt.colorbar(p, ax=ax)
    cbar.set_label("N")

    # Etiquetas
    ax.set_xlabel("p_hor")
    ax.set_ylabel("p_ver")
    ax.set_zlabel("S")
    ax.set_title("Superficie S según p_hor, p_ver y N (color)")

    plt.tight_layout()
    plt.show()


    pass
if __name__ == '__main__':
    main()
    tercermain()
