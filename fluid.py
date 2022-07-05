
import numpy as np
import matplotlib.pyplot as plt

n = 10
x = np.linspace(-n,n,4)
y = np.linspace(-n,n,4)

X,Y = np.meshgrid(x,y)

U = X**2 + Y - 1
V = X + Y**2 + 1

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)

plt.colorbar(plt.streamplot(X,Y,U,V,color = U, density = [1,1],cmap = "rainbow").lines)

plt.title("Stream Plot - U", fontsize = 15)
plt.xlabel("X",fontsize = 15)
plt.ylabel("Y",fontsize = 15)
plt.tight_layout(pad=3)

plt.subplot(1,2,2)
plt.colorbar(plt.streamplot(X,Y,U,V,color = V, density = [1,1],cmap = "rainbow").lines)
plt.title("Stream Plot - V", fontsize = 15)
plt.xlabel("X",fontsize = 15)
plt.ylabel("Y",fontsize = 15)

plt.xlim(-n,n)
plt.ylim(-n,n)
plt.show()