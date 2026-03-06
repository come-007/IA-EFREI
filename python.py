import cv2
import numpy as np

def grayscale ():
    img_brut=input("Veuillez rentrer le chemin de votre fichiers:")
    img = cv2.imread(img_brut)
    Blue = img[:, :, 0]
    Green = img[:, :, 1]
    Red = img[:, :, 2]
    grayscale_img = ((Blue+Green+Red)/3)
    grayscale_img=np.where (grayscale_img<127,0,255)
    grayscale_img = grayscale_img.astype(np.uint8)
    L=input("Largeur souhaité ?")
    Lo=input("Longueur souhaité ?")
    new_size=(L,Lo)
    resized_img = cv2.resize(grayscale_img, new_size, interpolation=cv2.INTER_AREA)
    nom_fichier=input("Quel nom pour votre fichier ?")
    cv2.imwrite(f'{nom_fichier}.png', resized_img)

grayscale()