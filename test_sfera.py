'''Modulo test sfera, eq: (x-x0)^2+(y-y0)^2+(z-z0)^2=r^2'''
import math
import cmath
import random
import numpy as np
import pandas as pd

# (x-x0)^2 + (y-y0)^2 + (z^2 -2*z*z_0 + z_0^2) = R^2
# z^2 -2*z_0*z +((x-x0)^2 + (y-y0)^2 - R^2) = 0
# A*z^2 + B*z + C = 0




def trova_z_sfera( X: float, Y: float, x_0: float, y_0: float, z_0: float, R: float) -> float:
    A = 1
    B = 2 * z_0
    C = (X - x_0)**2 + (Y - y_0)**2 - R**2

    Z = risolvi_equazione_parabola(A, B, C)

    return Z



def risolvi_equazione_parabola(A: float, B: float, C: float) -> float:

    dis = (B**2) - (4 * A*C)
  
    # find two result
    ans1 = (-B-cmath.sqrt(dis))/(2 * A)
    ans2 = (-B + cmath.sqrt(dis))/(2 * A)

    return max([ans1.real, ans2.real])

def crea_excel_punti_sfera(excel_file: str, num_righe: int, num_colonne: int,
                      random_seed: int, y_random = False) -> None:
    
    '''Funzione che ritorna nuvola di punti per superfice con griglia e valori z su sfera'''
    
    #valori in mm
    y_min, y_max = 0, 100
    lun_righe_min, lun_righe_max  = 30, 30
    x_0_min, x_0_max = 0, 0
    

    #coordinate centro sfera e raggio
    xC = 100
    yC = 100
    zC = 200
    R = 50
    
    #inizializzo il random
    random.seed(random_seed)

    #creo valori y ( altezze righe orizzontali)
    if y_random :
        y_righe = [random.randint(y_min, y_max) for _ in range(num_righe)]
    else:
        y_righe = [y for y in np.linspace(y_min, y_max, num_righe, endpoint = True)]
    
    y_righe.sort()

    #creo vettore lunghezza righe in mm
    lun_righe = [random.randint(lun_righe_min, lun_righe_max) for _ in range(num_righe)]

    #creo vettore valore x dei punti sulla prima colonna 0
    x_0 = [random.randint(x_0_min, x_0_max) for _ in range(num_righe)]

    #genero i valori delle x di tutti i punti tenendo il vincolo di x_0 (x_inizio)
    X = []
    for i, x_inizio in enumerate(x_0):
        X.append([x for x in np.linspace(x_inizio, x_inizio + lun_righe[i], num_colonne, endpoint = True)])

    #creo le coordinate (x, y, z) dei punti della superficie con z random tra 2 valori, li converto poi in numpy.array
    Points = []
    
    for i, y in enumerate(y_righe):
        for x in X[i]:
            z = trova_z_sfera(x, y, xC, yC, zC, R)
            Points.append([x, y, z])

    #numpy_array
    points = np.array([np.array(p) for p in Points])

    all_points = Points

    print("y_righe: ", y_righe)
    print("len_righe: ", lun_righe)
    print("x_0: ", x_0)
    print("X: ", X)
    print(all_points)
    
    
    #Creo excel
    df_punti = pd.DataFrame(all_points)
    df_punti.to_excel(excel_file, index = False, header = False)  


if __name__ == "__main__":
    excel_file = r"C:\Users\DSL1PVI\Desktop\progetti codice\NuVOLa2\input\sfera.xlsx"
    crea_excel_punti_sfera(excel_file, num_righe = 5, num_colonne = 5, random_seed = 13,
                            y_random = False )