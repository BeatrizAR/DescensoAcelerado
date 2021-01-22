#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 08/11/2019

@author: Beatriz
'''

import sys
import math
import numpy as np
import sympy as sp
from sympy import *
from sympy.plotting import plot
from sympy.abc import x,y,t #t = lambda
init_printing()


class descenso_acelerado():
    
    def __init__(self):
        '''Aqui se inicializan las variables'''
        '''Notacion en la funcion: x= es la variable x1, y= es la variable x2'''
        self.f = x**4 - 2*y*x**2 + y**2 + x**2 - 2*x + 5
        self.gradiente = []
        self.epsilon = 10**-5
        self.k=0
        self.kmax= 0
        self.xinicial = []
        self.pgradev = []
        self.normGrad = 0 
        self.s = []
        self.puntol= []
        self.funcl=0
        self.lamb=0
        for i in range(0,2):
            self.s.append(0)
        
        
    '''En esta funcion toma el gradiente y evalua sobre los valores del vector X, devuelve un vector'''
    def evaluacion_de_gradiente(self,gradiente,n1,n2 ):
        pgradev = []
        grad1=gradiente[0]
        grad2=gradiente[1]
        
        for i in range(0,len(gradiente)):
            pgradev.append(0)
        
        pgradev[0]=grad1.subs([(x,n1),(y,n2)])
        self.s[0]=pgradev[0]*-1
        pgradev[1]=grad2.subs([(x,n1),(y,n2)])
        self.s[1]=pgradev[1]*-1
        
            
        return pgradev
    
    '''En esta funcion evalua sobre una funcion con valores de un un vector, regresa un valor númerico '''
    def evaluacion_de_lambda(self,vector):
        punto1=vector[0]
        punto2=vector[1]
        
        funcion = self.f.subs([(x,punto1),(y,punto2)])
        return funcion
    
    '''En esta funcion encuentra el vector, que evaluado en la funcion da el minimo'''
    def evaluacion_minima(self,valores,puntos):
        puntonuevo = []
        evaluacionf = []
        
        for j in range(0,len(valores)):
            evaluacionf.append(0)
           
        for l in range(0,2):
            puntonuevo.append(0)
            
        
        for i in range(0,len(valores)):
            raiz = str(sp.N(valores[i])).split()[0]
            evaluacionf[i]=self.f.subs([(x,puntos[0].subs([(t,raiz)])),(y,puntos[1].subs([(t,raiz)]))])
            
        
        
        pos = evaluacionf.index(min(evaluacionf))
        self.lamb= str(sp.N(valores[pos])).split()[0]
       
        a1=puntos[0].subs([(t,self.lamb)])
        a2=puntos[1].subs([(t,self.lamb)])
         
        
        
        n1=str(sp.N(a1)).split()[0]
        n2=str(sp.N(a2)).split()[0]
        
        puntonuevo[0]= N(n1)
        puntonuevo[1]= N(n2)
        
        return puntonuevo

    
    def main(self):
        
        self.xinicial = [1,2]
        
        dfx = diff(self.f, x) # 1era. derivada sobre x
        dfy = diff(self.f, y) # 1era. derivada sobre y
        self.gradiente.append(dfx)
        self.gradiente.append(dfy)
        correcto=False
        while(not correcto):
            try:
                print "ingrese un epsilon: "
                self.epsilon = N(input())
                #print "Epsilon ",self.epsilon
                print "Ingrese un maximo de iteraciones: "
                self.kmax = N(input())
                correcto=True
            except:
                print("Ingrese valores númericos")
        
        print "k"+"\t\t x1"+"\t\t x2"+"\t\t f(x)"+"\t\t norma del gradiente"+"\t\t s1"+"\t\t s2"+"\t\t lambda*"
        
        '''mientras la normal sea menor o igual a epsilon, o k sea menor o igual al k max'''
        while(self.normGrad <= self.epsilon or self.k <= self.kmax):
            
            
            evaluacionf =self.evaluacion_de_lambda(self.xinicial)
            
            self.pgradev = self.evaluacion_de_gradiente(self.gradiente,self.xinicial[0],self.xinicial[1])
        
            self.normGrad = N(sqrt(self.pgradev[0]**2+self.pgradev[1]**2))
        
            self.puntol = np.array(self.xinicial)+t*(np.array(self.s)) 
            
            self.funcl=self.evaluacion_de_lambda(self.puntol)
            
            dfl= diff(self.funcl,t)
                    
            self.valoresl = solve(N(Eq(dfl, 0)))
            
            nuevosPuntos = self.evaluacion_minima(self.valoresl,self.puntol)
        
            print "\n\n",self.k,"\t",self.xinicial[0],"\t",self.xinicial[1],"\t",evaluacionf,"\t",self.normGrad,"\t",self.s[0],"\t",self.s[1],"\t",self.lamb
            
            self.xinicial = nuevosPuntos
            

            self.k+=1

        #time.sleep(100000000000000)
obj = descenso_acelerado()
obj.main() 