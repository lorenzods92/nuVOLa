# NUVOLA
## INTRO
Programma per calcolare il volume sotteso a una superficie ( dalla superficie al piano X-Y dove z = 0)
La superficie è definita da una nuvola di punti meshati tra di loro con la triagolazione di Delaunay. 


<p align="center">
<img src="immagini\3d-1.png"  width="300" height="300">

Ogni punto sulla superficie è un vertice di un triangolo. Vista in 2D appare:

<p align="center">
<img src="immagini\2d-1.png"  width="200" height="200">

>Il volume viene calcolato come somma dei prismi creati dai triangoli.
<p align="center">
<img src="immagini\prism.png" width="150" height="200">

## INPUT
il file di input deve essere un file di estensione .xlsx contenente 3 colonne con i valori x, y e z dei punti.
Es:

<p align="center">
<img src="immagini\tab.png">

Le regole di inserimento sono:

- File con estensione .xlsx
- Il nome del file deve contenere la sua estensione: es "test.xlsx"
- File deve trovarsi in una cartella nominata "input" salvata nella stessa directory del file .exe
- File deve contenere SOLO i valori x, y e z in colonne, nessuna intestazione delle colonne
- I valori z devono essere > 0 dato che la base è il piano X-Y con z = 0
- L'ordine dei punti è ininfluente

>L'unico concetto importante in fase di inserimento punti riguarda la possibilità di avere un bordo esterno della superficie concavo.
Infatti mediante la triangolazione di Delauney non viene garantito il ripspetto di bordi concavi (vedi nella 2a figura il triangolino in basso a destra)

## CALCOLO VOLUME
Iterando su tutti i prismi il volume del singolo prisma viene calcolato con la segente formula:

> $1/3$ * $Area base$ * ( $\sum_{i=1}^{3} h_i$ )

dove $Area base$ è l'area del triangolo di base sul piano X-Y e
$h_i$ è l'altezza dello spigolo i-esimo (ossia la coordinata z)

## OUTPUT
L'output viene visualizzato sulla riga di comando con unità di misura coerente con le coordinate dei punti


## COME SI USA:

Lanciare il programma da eseguibile o da linea di comando:
```python
 python nuVOLa.py
```
Caso input random
```
creare input random? [qualsiasi tasto per SI / premere INVIO per NO]
```
Inserire il nome del file di input
```
Inserire nome file [premere INVIO per nome di default]:  test4.xlsx
```
Chiudere le figure dopo aver controllato che l'output sia coerente e poi verrà visualizzato il calcolo del volume
```
Il volume totale è:  301389.58
```