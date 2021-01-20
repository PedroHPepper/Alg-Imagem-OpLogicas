import cv2
import numpy as np
import matplotlib.pyplot as plt



img1 = cv2.imread('C:/Users/pedro/Google Drive/Faculdade/3º Período/Computação gráfica e Processamento de Imagens/Python/untitled/lena.jpg', 0)

#img2 = cv2.bitwise_not(img1)

img2 = []

for l in range(len(img1)):
    linha = []
    for c in range(len(img1[0])):
        linha.append(255-img1[l][c])
    img2.append(linha)


print(np.matrix(img2))

plt.subplot(2,1,1), plt.imshow(img1,"gray", vmin=0, vmax=255), plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,1,2), plt.imshow(img2,"gray", vmin=0, vmax=255), plt.title('Imagem Invertida'), plt.xticks([]), plt.yticks([])
plt.show()