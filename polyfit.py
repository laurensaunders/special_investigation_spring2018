import matplotlib.pyplot as plt
import numpy as np
import scipy.special as special
import scipy.optimize as optimize

xdata = np.arange(-40,40,0.5)
ydata = abs(special.airy(xdata)[0]) + abs(special.airy(-xdata)[0])

plt.plot(xdata,ydata,color='k',label='Data')

plt.plot(xdata,ydata,color='k',label='Data')

#def airyfunction(xs):
#    Ai_list = []
#    for x in xs:
#        Ai = 1/pi*cmath.sqrt(x/3).real*special.yv(1/3,x)*(2/3*x**(2/3))
#        Ai_list.append(Ai)
#    return Ai_list


def airy_to_fit(x,params):
    c1,c2 = params
    airyadd = special.airy(x)[0] + special.airy(c1*x + c2)[0]
    return airyadd

def guess(params,args):
    xs,ys = args
    guessval = airy_to_fit(xs,params)
    return guessval

def get_params(xs,ys,c1,c2):
    params = [c1,c2]
    result, success = optimize.leastsq(guess,copy(params),args=[xs[:],ys[:]])
    return result, success

def get_params2(xs,ys,c1,c2):
    params = [c1,c2]
    result, cov = optimize.curve_fit(airy_to_fit,copy(params),args=[xs[:],ys[:]])
    return result, success

def get_airyfit(xs,ys):
    fitpars,success = get_params(xs,ys,-1,0)
    return fitpars

def plot_fit(xs,params):
    c1,c2=params
    plt.plot(xs,special.airy(xs)[0]+special.airy(c1*xs + c2)[0])
