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

img_B = np.array([
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,1,0,0,0,0,0,0,1],
    [1,0,0,0,1,0,1,1,0,1],
    [1,0,1,0,1,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1]
])

img_C = []
for l in range(6):
    linha = []
    for c in range(10):
        if(img_A[l][c] == 1 and img_B[l][c]==1):
            linha.append(1)
        else:
            linha.append(0)
    img_C.append(linha)

print(np.matrix(img_C))
plt.subplot(3,1,1), plt.imshow(img_A,"gray", vmin=0, vmax=1), plt.title('Imagem 1'), plt.xticks([]), plt.yticks([])
plt.subplot(3,1,2), plt.imshow(img_B,"gray", vmin=0, vmax=1), plt.title('Imagem 2'), plt.xticks([]), plt.yticks([])
plt.subplot(3,1,3), plt.imshow(img_C,"gray", vmin=0, vmax=1), plt.title('Imagem resultante da Operação AND'), plt.xticks([]), plt.yticks([])
plt.show()
