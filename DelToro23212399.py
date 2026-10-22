"""
Práctica 2: Modelado y Control de Sistemas Fisiologicos

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Eduardo Del Toro Nuñez
Número de control: C23212399
Correo institucional: C23212399@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
#Librerías

import numpy as np
import math as m
import control as ctrl
import matplotlib.pyplot as plt
from scipy import signal
import pandas as pd

#Datos Generales de la Simulacion

u = np.array(pd.read_excel('signal.xlsx',header=None))
x0,t0,tend,dt,w,h = 0,0,15,1e-3,10,5
N = round((tend-t0)/dt) + 1
t = np.linspace(t0,tend,N)
u = np.reshape(signal.resample(u,len(t)),-1)

def cardio(Z,L,R,C):
    num = [L*R,R*Z]
    den = [C*R*L*Z,L*R+L*Z,R*Z]
    sys = ctrl.tf(num,den)
    L = np.roots(den)
    return sys,L

#Funcion de Transferencia: Normotenso
Z,L,R,C = 0.010,0.001,1.00,1.500
sysnormo,L = cardio(Z,L,R,C)
print(f'Funcion de Transferencia del Normotenso (control): {sysnormo}')
print(f"Polos del sistema: L1 = {L[0]:.3e}, L2 = {L[1]:.3e}\n")

#Funcion de Transferencia: Hipertenso
Z,L,R,C = 0.010,0.001,1.00,1.000
syshiper,L = cardio(Z,L,R,C)
print(f'Funcion de transferencia del hipertenso (caso 2): {syshiper}')
print(f"Polos del Sistema: L1 = {L[0]:.3e}, L2 = {L[1]:.3e}\n")

#Funcion de Transferencia: Hipotenso
Z,L,R,C = 0.010,0.001,1.00,3.500
syshipo,L = cardio(Z,L,R,C)
print(f'Funcion de transferencia del hipertenso (caso 3): {syshipo}')
print(f"Polos del Sistema: L1 = {L[0]:.3e}, L2 = {L[1]:.3e}\n")

#Componentes del Controlador del Hipertenso
kP, kI, kD = 1.42831061828755, 155.70187045244, 0.00109677996369316
Cr = 1E-6
Re = 1/(Cr*kI)
Rr = kP*Re
Ce = kD/Rr
numPIDH = [Re*Rr*Ce*Cr, (Re*Ce + Rr*Cr), 1]
denPIDH = [Re*Cr, 0]
PIDH = ctrl.tf(numPIDH,denPIDH)
print(f"Capacitancia Cr: {Cr} Faradios\n")
print(f"Resistencia Re: {Re:.3e} Ohms\n")
print(f"Resistencia Rr: {Rr:.3e} Ohms\n")
print(f"Capacitancia Ce: {Ce:.3e} Faradios\n")
print(f"Función de transferencia del controlador PIDH: {PIDH}\n")
sysPIDH = ctrl.feedback(ctrl.series(PIDH,syshiper),1,sign = -1)
print(f"Funcion de transferencia en lazo cerrado: {sysPIDH}\n")


#Componentes del Conrolador Hipotenso
kP, kI, kD = 291.976430518119, 451014.46273679, 0.00626523346028193
Cr = 1E-6
Re = 1/(Cr*kI)
Rr = kP*Re
Ce = kD/Rr
numPIDL = [Re*Rr*Ce*Cr, (Re*Ce + Rr*Cr), 1]
denPIDL = [Re*Cr, 0]
PIDL = ctrl.tf(numPIDL,denPIDL)
print(f"Capacitancia Cr: {Cr} Faradios\n")
print(f"Resistencia Re: {Re:.3e} Ohms\n")
print(f"Resistencia Rr: {Rr:.3e} Ohms\n")
print(f"Capacitancia Ce: {Ce:.3e} Faradios\n")
print(f"Función de transferencia del controlador PIDL: {PIDL}\n")
sysPIDL = ctrl.feedback(ctrl.series(PIDL,syshipo),1,sign = -1)
print(f"Funcion de transferencia en lazo cerrado: {sysPIDL}\n")

# Colores

clr1 = np.array([139,30,45])/255
clr2 = np.array([51,104,160])/255
clr3 = np.array([18, 84, 79])/255

_,Pp0 = ctrl.forced_response(sysnormo,t,u,x0)
_,Pp1 = ctrl.forced_response(syshipo,t,Pp0,x0)
_,Pp2 = ctrl.forced_response(syshiper,t,Pp0,x0)

plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']

fg1 = plt.figure()
plt.plot(t,Pp1,'-',linewidth=0.5,color=clr1,label='Pp(t): Hipotenso')
plt.plot(t,Pp2,'--',linewidth=0.5,color=clr2,label='Pp(t): Hipertenso')
plt.plot(t,Pp0,':',linewidth=0.5,color=clr3,label='Pp(t): Normotenso')
plt.grid(False)
plt.xlim([0,15]); plt.xticks(np.arange(0,15.1,1))
plt.ylim([-1.8,1.8]); plt.yticks(np.arange(-1.8,1.9,0.2))
plt.xlabel('t [s]')
plt.ylabel('Pp(t) [V]')
plt.legend(bbox_to_anchor=(0.5, -0.25), loc='center', ncol=3)
fg1.set_size_inches(w,h)
fg1.tight_layout()
fg1.savefig('Individuos_python.pdf')
plt.show()

_,PIDH = ctrl.forced_response(sysPIDH,t,Pp0,x0)

plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']

fg2 = plt.figure()
plt.plot(t,Pp1,'-',linewidth=0.5,color=clr1,label='Pp(t): Hipotenso')
plt.plot(t,PIDH,'--',linewidth=0.5,color=clr2,label='PID(t): Hipertenso')
plt.plot(t,Pp0,':',linewidth=0.5,color=clr3,label='Pp(t): Normotenso')
plt.grid(False)
plt.xlim([0,15]); plt.xticks(np.arange(0,15.1,1))
plt.ylim([-1.8,1.8]); plt.yticks(np.arange(-1.8,1.9,0.2))
plt.xlabel('t [s]')
plt.ylabel('Pp(t) [V]')
plt.legend(bbox_to_anchor=(0.5, -0.25), loc='center', ncol=3)
fg2.set_size_inches(w,h)
fg2.tight_layout()
fg2.savefig('ControladorHipertenso_Python.pdf')
plt.show()


_,PIDL = ctrl.forced_response(sysPIDL,t,Pp0,x0)

plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']

fg3 = plt.figure()
plt.plot(t,Pp1,'-',linewidth=0.5,color=clr1,label='Pp(t): Hipotenso')
plt.plot(t,PIDL,'--',linewidth=0.5,color=clr2,label='PID(t): Hipotenso')
plt.plot(t,Pp0,':',linewidth=0.5,color=clr3,label='Pp(t): Normotenso')
plt.grid(False)
plt.xlim([0,15]); plt.xticks(np.arange(0,15.1,1))
plt.ylim([-1.8,1.8]); plt.yticks(np.arange(-1.8,1.9,0.2))
plt.xlabel('t [s]')
plt.ylabel('Pp(t) [V]')
plt.legend(bbox_to_anchor=(0.5, -0.25), loc='center', ncol=3)
fg3.set_size_inches(w,h)
fg3.tight_layout()
fg3.savefig('ControladorHipotenso_Python.pdf')
plt.show()



