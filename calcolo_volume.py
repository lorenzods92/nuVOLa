'''Modulo per calcolo manuale volume superficie '''
# %%
import numpy as np
import pandas as pd
import math
import matplotlib.tri as mtri

from scipy.spatial import Delaunay
from typing import Tuple, List

from plot_3d import plot_points

def calcolo_volume_totale(excel_file: str) -> float:
    '''Funzione che import dati punt x,y,z da file excel e attraverso la triangola
    zione di delaunay e ritorna il volume totale'''
    
    #coordinate punti x,y,z importate da excel come dataframe
    df_points = pd.read_excel(excel_file, header=None)
    #converto dataframe in lista di liste
    points = df_points.values.tolist()
    
    #prendo solo i punti x e y
    points_2D = np.array([[point[0], point[1]] for point in points])

    #trovo i triangoli
    tri = Delaunay(points_2D)
    
    #plotto in 3d
    x = np.asarray([point[0] for point in points])
    y = np.asarray([point[1] for point in points])
    z = np.asarray([point[2] for point in points])

    plot_points(x, y, z, tri)
    
    #calcolo volume come somma dei prismi
    volumi_prismi = []
    for triangle in tri.simplices:
        volume_prisma = calcolo_volume_prisma(triangle, points)
        volumi_prismi.append(volume_prisma)

    volume_tot = round(sum(volumi_prismi), 2)
    
    return volume_tot
    
  
def calcolo_volume_prisma(triangle: Tuple[float, float, float], points: List[List[float]]) -> float:
    '''Calcolo volume di un prisma prendendo come input le 3 coordinate dei punti sulla sup. superiore
    e le coordinate x, y e z dei punti. I primsmi devono avere faccia di base su piano X-Y.
    La formula per il calcolo del volume di un prisma con triangolo di base su X-Y è:
    vol = 1/3 * area_base * (somma dei tre spigoli in Z) '''
    
    #prendo gli indici dei punti
    idx1, idx2, idx3 = triangle
    
    #trovo le coordinate x, y, z dei 3 punti
    point1 = (points[idx1][0], points[idx1][1], points[idx1][2])
    point2 = (points[idx2][0], points[idx2][1], points[idx2][2])
    point3 = (points[idx3][0], points[idx3][1], points[idx3][2])
    
    #trovo le lunghezza lati base
    l12 = math.dist([point1[0], point1[1]], [point2[0], point2[1]])
    l23 = math.dist([point2[0], point2[1]], [point3[0], point3[1]])
    l31 = math.dist([point3[0], point3[1]], [point1[0], point1[1]])
    
    #trovo il semiperimetro
    semi_p = sum([l12, l23, l31])/2
    
    #trovo area base
    area_base = math.sqrt(semi_p * (semi_p - l12) * (semi_p - l23) * (semi_p - l31))
    
    #trovo altezze lati prisma
    h1 = point1[2]
    h2 = point2[2]
    h3 = point3[2]
    
    #trovo il volume del prisma
    vol = 1/3 * area_base * sum([h1, h2, h3])

    return vol

# %%
if __name__ == "__main__":
    excel_file = r"C:\Users\DSL1PVI\Desktop\progetti codice\NuVOLa2\input\test4.xlsx"
    calcolo_volume_totale(excel_file)