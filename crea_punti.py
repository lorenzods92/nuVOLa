'''Modulo per creare punti file excel'''

import numpy as np
import pandas as pd
import random



def crea_excel_punti_random(excel_file: str, num_righe: int, num_colonne: int,
                      random_seed: int, y_random = False) -> None:
    
    '''Funzione che ritorna nuvola di punti per superfice con griglia e valori z random'''
    
    #valori in mm
    y_min, y_max = 0, 100
    lun_righe_min, lun_righe_max  = 100, 110
    x_0_min, x_0_max = 0, 0
    z_min, z_max = 20, 35
    
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
            z = random.randint(z_min, z_max)
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
    excel_file = r"C:\Users\DSL1PVI\Desktop\progetti codice\NuVOLa2\input\test4.xlsx"
    crea_excel_punti_random(excel_file, num_righe = 5, num_colonne = 5, random_seed = 13,
                            y_random = False )
    
