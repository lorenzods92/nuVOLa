'''Modulo MAIN per calcolo volume, prende in input file con estensione descritta e con i valori di
x, y e z nelle colonne'''

import sys
from pathlib import Path
import os

from calcolo_volume import calcolo_volume_totale
from crea_punti import crea_excel_punti_random

def main():
    '''Funzione Main'''
    
    #Ottengo nome file in input
    input_file = ottieni_dati_input()
    
    #Calcolo il volume
    volume = calcolo_volume_totale(input_file)
    
    #Stampo risultato
    print("Il volume totale è: ", volume)
    input("Premere INVIO per terminare ")
    
    

# %%
def ottieni_dati_input() -> str:
    '''Ottiene e controlla file in input'''
    
    #Stampo regole input
    print_regole_input()

    #Determino nome percorso se lanciato come exe o come .py
    if getattr(sys, 'frozen', False):
        dirname = os.path.dirname(sys.executable)
    elif __file__:
        dirname = os.path.dirname(__file__)
    
    #Imposto percorso directory_attuale/input per cercare o creare il file
    print('nome attuale directory: ', dirname)
    relative_path = 'input'

    #Verifico se creare excel random
    while True:
        crea_random = input('creare input random? [qualsiasi tasto per SI / premere INVIO per NO]  ')
        if crea_random:
            nome_file = input('Inserire nome file .xlsx: [premere INVIO per nome di default]  ') or 'test.xlsx'
            if not nome_file.endswith('.xlsx'):
                print('inserire un file con estensione .xlsx')
                print('nome file inserito: ', nome_file, '\n')
                continue
            else:
                input_file = os.path.realpath(os.path.join(dirname, relative_path, nome_file))
                print("inserire i seguenti dati:")
                num_righe = int(input("Inserire numero righe: [premere INVIO per nome di default = 5]") or 5)
                num_colonne = int(input("Inserire numero colonne: [premere INVIO per nome di default = 5]") or 5)
                random_seed = input("Inserire random seed: [premere INVIO per valore di default = 5]") or 5
                y_random = input("generare valore y colonne in maniera random?: [qualsiasi tasto per SI / premere INVIO per NO]")
                crea_excel_punti_random(input_file, num_righe, num_colonne, random_seed, y_random)
                break
        else:
            break
    
    #Caso in cui non creo un file excel random
    if not crea_random:
        while True:
            #Ottengo da tastiera nome file
            nome_file = input('Inserire nome file [premere INVIO per nome di default]:  ') or 'test.xlsx'
    
            #Creo il percorso completo
            input_file = os.path.realpath(os.path.join(dirname, relative_path, nome_file))
            
            #Controllo che sia un file e che abbia l'estensione corretta
            if not os.path.isfile(input_file):
                print('Il file in input con il percorso specificato non esiste')
                print('percorso inserito: ', input_file, '\n')
                continue
            elif not nome_file.endswith('.xlsx'):
                print('inserire un file con estensione .xlsx')
                print('nome file inserito: ', nome_file, '\n')
                continue
            else:
                #nome ed estensione input ok
                break
        
    return input_file

def print_regole_input() -> None:
    '''Stampo su console regole input'''

    print('--------------------------------------------------------------------------------------------------')
    print('Regole input: ')
    print('- Viene richiesto se si vuole creare una nuvola random per test [premere INVIO per saltare]')
    print('- File con estensione .xlsx')
    print('- Il nome del file deve contenere la sua estensione: es "test.xlsx"')
    print('- File deve trovarsi in una cartella nominata "input" salvata nella stessa directory del file .exe')
    print('- File deve contenere SOLO i valori x, y e z in colonne, nessuna intestazione delle colonne')
    print('- I valori z devono essere > 0 dato che la base è il piano X-Y con z = 0')
    print('--------------------------------------------------------------------------------------------------')


# %%
if __name__ == "__main__":    
    main()
    