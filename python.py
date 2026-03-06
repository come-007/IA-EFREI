import cv2
import numpy as np

def grayscale ():
    img_brut=input("Veuillez rentrer le chemin de votre fichiers:")
    img = cv2.imread(img_brut)
    Blue = img[:, :, 0]
    Green = img[:, :, 1]
    Red = img[:, :, 2]
    grayscale_img = ((Blue+Green+Red)/3)
    grayscale_img = grayscale_img.astype(np.uint8)
    cv2.imwrite('nom_du_fichier.png', grayscale_img)

grayscale()