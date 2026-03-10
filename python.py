import cv2
import numpy as np

def grayscale ():
    img_brut=input("Veuillez rentrer le chemin de votre fichiers:")
    img = cv2.imread(img_brut)
    img_float = img.astype(float)
    Blue = img_float[:, :, 0]
    Green = img_float[:, :, 1]
    Red = img_float[:, :, 2]
    grayscale_img = ((Blue+Green+Red)/3)
    grayscale_img=np.where (grayscale_img<127,0,255)
    grayscale_img = grayscale_img.astype(np.uint8)
    L=int(input("Largeur souhaité ?"))
    Lo=int(input("Longueur souhaité ?"))
    new_size=(L,Lo)
    resized_img = cv2.resize(grayscale_img, new_size, interpolation=cv2.INTER_AREA)
    nom_fichier=input("Quel nom pour votre fichier ?")
    cv2.imwrite(f'{nom_fichier}.png', resized_img)
    matrice=np.where(grayscale_img>127,0,1)
    coordonnées = np.argwhere(matrice==1)
    y_min, x_min = coordonnées.min(axis=0)
    y_max, x_max = coordonnées.max(axis=0)
    grayscale_img_2 = matrice[y_min:y_max+1, x_min:x_max+1]
    print(grayscale_img_2)

grayscale()