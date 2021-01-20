import cv2
import numpy as np
import matplotlib.pyplot as plt


img_A = np.array([
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,1,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1]
])

img_B = []
for l in range(6):
    linha = []
    for c in range(10):
        if(img_A[l][c] == 0):
            linha.append(1)
        else:
            linha.append(0)
    img_B.append(linha)

print(np.matrix(img_B))
plt.subplot(3,1,1), plt.imshow(img_A,"gray", vmin=0, vmax=1), plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])
plt.subplot(3,1,3), plt.imshow(img_B,"gray", vmin=0, vmax=1), plt.title('Imagem resultante da Operação NOT'), plt.xticks([]), plt.yticks([])
plt.show()
