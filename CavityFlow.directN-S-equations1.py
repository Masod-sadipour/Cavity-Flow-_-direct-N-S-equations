## LID DRIVEN CAVITY FLOW 
## May 2020.

# importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# variables and discritization parameters

nt=100
nit=50
nx=41
ny=41
rho=1
nu=0.1
dt = 0.001
dx=2/(nx-1)
dy=2/(ny-1)

x = np.linspace(0, 2, nx)
y = np.linspace(0, 2, ny)

# initial condition for all variables

u = np.zeros((ny, nx))    #X-Velocity initialization
un = np.zeros((ny, nx))   
v = np.zeros((ny, nx))    #Y-Velocity initialization
vn = np.zeros((ny, nx))    
p = np.zeros((ny, nx))    #pressure initialization
pn = np.zeros((ny, nx))   
b= np.zeros((ny, nx))     #Right Hand Side of final pressure discritization

for n in range(nt):  ##loop across number of time steps(nt)

    for n in range(nit):  #loop for pressure (nit)

        pn = p.copy()
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                b = rho * ((((u[i + 1, j] - u[i - 1, j]) / (2 * dx)) ** 2)
                           + 2 * (((u[i, j + 1] - u[i, j - 1]) / (2 * dy)) * ((v[i + 1, j] - v[i - 1, j]) / (2 * dy)))
                           + (((v[i, j + 1] - v[i, j - 1]) / (2 * dy)) ** 2))
                p[i, j] = (((pn[i, j - 1] + pn[i, j + 1]) * (dx ** 2) + (pn[i - 1, j] + pn[i + 1, j]) * (dy ** 2)) / (
                            2 * (dx ** 2 + dy ** 2))
                           + (b * ((dy * dx) ** 2)) / (2 * (dx ** 2 + dy ** 2)))
        
        # Pressure boundary conditions
        p[:, -1] = p[:, -2]  # dp/dx = 0 at x = 2
        p[0, :] = p[1, :]  # dp/dy = 0 at y = 0
        p[:, 0] = p[:, 1]  # dp/dx = 0 at x = 0
        p[-1, :] = 0  # p = 0 at y = 2

    un = u.copy()
    vn = v.copy()
    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            u[i, j] = (un[i, j] - (un[i, j] * (dt / dx) * (un[i, j] - un[i - 1, j])) - vn[i, j] * (dt / dy) * (
                        un[i, j] - un[i, j - 1])) + (
                                  (nu * dt / (dx ** 2)) * (un[i + 1, j] - 2 * un[i, j] + un[i - 1, j]) + (
                                      nu * dt / (dy ** 2)) * (un[i, j - 1] - 2 * un[i, j] + un[i, j + 1])) - (
                                  (dt / (2 * rho * dx)) * (p[i + 1, j] - p[i - 1, j]))
            v[i, j] = (vn[i, j] - (un[i, j] * dt / dx * (vn[i, j] - vn[i - 1, j])) - vn[i, j] * dt / dy * (
                        vn[i, j] - vn[i, j - 1])) + (
                                  (nu * dt / (dx ** 2)) * (vn[i + 1, j] - 2 * vn[i, j] + vn[i - 1, j]) + (
                                      nu * dt / (dx ** 2)) * (vn[i, j - 1] - 2 * vn[i, j] + vn[i, j + 1])) - (
                                  (dt / (2 * rho * dy)) * (p[i, j + 1] - p[i, j - 1]))
     #Velocity boundary conditions
    u[0, :] = 0
    u[:, 0] = 0
    u[:, -1] = 0
    u[-1, :] = 1  
    v[0, :] = 0
    v[-1, :] = 0
    v[:, 0] = 0
    v[:, -1] = 0


# plotting the X-Velocity field as a contour
X, Y = np.meshgrid(x, y)
breaks1 = np.linspace(-0.2, 1, 26)
fig = plt.figure(figsize=(11, 7), dpi=200)
plt.contourf(X, Y, u, breaks1, alpha=0.6, cmap=cm.jet)
plt.colorbar(ticks=breaks1)
plt.contour(X, Y, u, breaks1, cmap=cm.jet)
plt.title('U')
plt.xlabel('X')
plt.ylabel('Y');
fig.savefig('U.png', bbox_inches='tight')
# plotting the Y-Velocity field as a contour
X, Y = np.meshgrid(x, y)
breaks=np.linspace(-0.0024,0.0024,17)
fig = plt.figure(figsize=(11, 7), dpi=200)
plt.contourf(X, Y, v,breaks,alpha=0.6, cmap=cm.jet)
plt.colorbar(ticks=breaks)
plt.contour(X, Y, v,breaks,cmap=cm.jet)
plt.title('V')
plt.xlabel('X')
plt.ylabel('Y');
fig.savefig('V.png', bbox_inches='tight')
