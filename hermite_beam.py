import matplotlib.pyplot as plt
import numpy as np
import scipy.special as special

# For Hermite polynomials
Hermite = special.hermite
xes = np.arange(-5,5,0.1)

def make_hbeam_plot(deg, squared=True):
    H = Hermite(deg)
    if squared==True:
        plt.semilogy(xes, H(xes)**2, color='k', label='Original Function')
    elif squared==False:
        plt.semilogy(xes, H(xes), color='k', label='Original Function')


def find_hfit(xes,deg, squared=True):
    xs=[]
    ys=[]
    H=Hermite(deg)
    for x in xes:
        xs.append(x)
    for y in H(xes):
        if squared==True:
            ys.append(y**2)
        elif squared==False:
            ys.append(y)

    pfit=np.polynomial.polynomial.polyfit(xs,ys,deg)

    fitfunct=[]
    llist=[]
    for l in range(1,deg+1):
        llist.append(l)
    for i in range(len(xs)):
        fitfunct.append(pfit[0]*xs[i]**0)
    for i in range(len(xs)):
        for ll in llist:
            fitfunct[i]+=pfit[ll]*xs[i]**ll
    return fitfunct

plt.plot(xs,fitfunct,color='r',alpha=0.5,label='PolyFit')
    #for x in xs:
#        fitfunct.append(pfit[0]+pfit[1]*x+pfit[2]*x**2+pfit[3]*x**3+pfit[4]*x**4)

# For Airy functions
airy = special.airy
def make_airy_plot(xes,squared=True):
    ai,aip,bi,bip=airy(xes)
    if squared==True:
        plt.semilogy(xes,ai**2,color='k',label='Original Function')
    elif squared==False:
        plt.plot(xes,ai,color='k',label='Original Function')

def find_afit(xes,deg, squared=True):
    xs=[]
    ys=[]
    ai,aip,bi,bip=airy(xes)
    for x in xes:
        xs.append(x)
    for y in ai:
        if squared==True:
            ys.append(y**2)
        elif squared==False:
            ys.append(y)

    pfit=np.polynomial.polynomial.polyfit(xs,ys,deg)

    fitfunct=[]
    llist=[]
    for l in range(1,deg+1):
        llist.append(l)
    for i in range(len(xs)):
        fitfunct.append(pfit[0]*xs[i]**0)
    for i in range(len(xs)):
        for ll in llist:
            fitfunct[i]+=pfit[ll]*xs[i]**ll
    return xs, fitfunct

def afit_plot(xs,afit,deg,color,squared=True):
    if squared==True:
        plt.semilogy(xs,afit,color=color,label='Deg %s Fit'%deg)
    elif squared==False:
        plt.plot(xs,afit,color=color,label='Deg %s Fit'%deg)
