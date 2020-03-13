import random as rd
import numpy as np

class CA():
  #PI - PADRAO INICIAL / NG=número de Gerações/ rg= regra

  def __init__(self,grid,rg,IP=0,BC=1):

    #transforma o valor da regra no código da REGRA
    self.grid=grid
    rg=list(bin(rg))    
    x1=np.zeros((8))
    for i in range(0,len(rg)-1):
      x1[i-1]=rg[-i]
    self.rg=x1
    if IP==0: #condições inciais aleatórias
      PI=np.random.randint(2, size=grid)    
    if IP==1: #condição incial ponto no meio
      PI=np.zeros((grid))
      PI[int(grid%2+grid/2-1)]=1
    self.PI=PI
    self.BC=BC
    
     

  def evo(self,NG): #loop das próximas gerações 
    grid=self.grid
    rule=self.rg
    BC=self.BC
    IP=self.PI
    if BC==1: #Condicoes de contorno periodicas
     MA=np.zeros((NG,grid))
     MA[0,:]=self.PI  
     stt=0
     end=grid        
    if BC==0: #Condicoes de contorno 0
     MA=np.zeros((NG,grid+2))
     MA[0,1:-1]=self.PI 
     stt=1
     end=grid+1
    for i in range(1,NG):
      for u in range(stt,end):
        y1=str(int(MA[i-1,u-1]))+str(int(MA[i-1,u]))+str(int(MA[i-1,(u+1)%grid]))
        y1=int(y1,2)
        MA[i,u]=rule[y1]
                   
    return MA



