import numpy as np
import matplotlib.pyplot as plt
import time


a, b = np.loadtxt("sun_AM0.dat.dat", unpack="True")
b = b * 100000
a = a * 0.001
plt.figure(1)
plt.clf()

plt.plot(np.log10(a),np.log10(b))


plt.ylabel("flujo en ergs por centimetro cuadrado por micron")
plt.xlabel("longitud de onda en micrones")
plt.legend
plt.show()

int = 0.
for i in range(1696):
    int = int + ((a[i+1]-a[i])/2.)*(b[i]+b[i+1])
print "primera integral"
print int

print "integral con scipy"

prueba = np.trapz(b,a)
print prueba

c, d=np.linspace(0.,np.pi,num=2001, endpoint=True,retstep=True)
print c
print d

def evaluador(x):
    valor= ((np.tan(x)*np.tan(x)*np.tan(x))/(np.cos(x)*np.cos(x)*(np.exp(np.tan(x))-1)))
    return valor

e=np.zeros(2001)

int2 = 0
start_time = time.time()
for i in range(1999):
    int2 = int2 + d/2*(evaluador(c[i+1])+evaluador(c[i+2]))
    e[i+1]=evaluador(c[i+1])
print ("%s segundos" % (time.time() - start_time))
print int2


print "integral2 con scipy"
start_time2 = time.time()
prueba2 = np.trapz(e,c)
print ("%s segundos" % (time.time() - start_time2))
print prueba2
