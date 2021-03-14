def megisto(sinartisi):
    from sympy import Symbol,Function, diff, sin, exp, solve, lambdify
    import numpy as np
    import matplotlib.pyplot as plt
    x = Symbol('x')
    i = Symbol('i')
    f = Symbol('f')
    sinar = Symbol('sinar')
    first = diff(sinartisi, x)
    second = diff(first, x)
    lisi = solve(first,x)
    f = lambdify(x,second)
    sinar = lambdify(x,sinartisi)
    
    for k in lisi:
        if k<=6:
            x_vals = np.linspace(-7, 7,10000)
        elif k >6 and k<=10:
            x_vals = np.linspace(-10, 10,100) 
        elif k >10 and k<=20:
            x_vals = np.linspace(-50, 50,100)
        else:
            x_vals = np.linspace(-70, 70,100)
    y_vals = np.array([sinar(x) for x in x_vals])
    fig, ax=plt.subplots(figsize=(8,5))
    ax.plot(x_vals, y_vals)
    ax.set_title('f(x) = ' + sinartisi)
    ax.set_xlabel('Axis X')
    ax.set_ylabel('Axis Y')
    ax.grid(True)
    
    for i in lisi:
        if f(i) > 0:
            print('\n > Min: y* =', sinar(i),'\n        x* =',i)
            ax.annotate("Min", xytext=(i,i+20),xy=(i,sinar(i)),arrowprops={'facecolor':'black'})
        else:
            print('\n > Max: y* =',sinar(i),'\n        x* =',i)
            ax.annotate("Max",xytext=(i,i+20),xy=(i,sinar(i)), arrowprops={'facecolor':'black'})            
    plt.show()
    
import os
os.system('cls' if os.name == 'nt' else 'clear')
print('')
print('______________________________________________________________________________________')
print('')
print('  Agricultural University of Athens')
print('  School of Applied Economics & Social Sciences')
print('  Department Of Agricultural Economics & Rural Development')
print('  Stefanos Stavrianos, UGRD')
print('  stefanos.stavrianos@outlook.com')
print('  +30 698 595 5584')
print('______________________________________________________________________________________')
print('')
print('                  __________________________________________________')
print('                 |                                                  |')
print('                 |          E X T R E M U M   F I N D E R           |')
print('                 |__________________________________________________|')

sinartisi = input('\n Function: f(x) = ')
while sinartisi == '':
    os.system('cls')
    print('')
    print('______________________________________________________________________________________')
    print('')
    print('  Agricultural University of Athens')
    print('  School of Applied Economics & Social Sciences')
    print('  Department Of Agricultural Economics & Rural Development')
    print('  Stefanos Stavrianos, UGRD')
    print('  stefanos.stavrianos@outlook.com')
    print('  +30 698 595 5584')
    print('______________________________________________________________________________________')
    print('')
    print('                  __________________________________________________')
    print('                 |                                                  |')
    print('                 |          E X T R E M U M   F I N D E R           |')
    print('                 |__________________________________________________|')
    print('')
    print('\n Invalid entry!')
    sinartisi = input('\n Function: f(x) = ')
megisto(sinartisi)