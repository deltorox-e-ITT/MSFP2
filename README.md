[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=deltorox-e-ITT/ModeladoDeSistemasFisiologicosP3)

# Práctica 2: Modelado y control del sistema cardiovascular mediante el modelo Windkessel

## Información del estudiante
Eduardo Del Toro Nuñez; LC23212399.tijuana.tecnm.mx

Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente
Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivos

1. Identificar las variables hemodinámicas y los parámetros del modelo Windkessel de cuatro elementos en un circuito eléctrico equivalente.
2. Formular el modelo dinámico en espacio de estados y obtener las funciones de transferencia para condiciones normotensa (control), hipotensa e hipertense (casos).
3. Evaluar analíticamente la estabilidad de los tres modelos y su error en estado estacionario ante una entrada escalón.
4. Emular y simular la respuesta del sistema cardiovascular en MATLAB, Simulink y Simscape Electrical ante una señal aleatoria de excitación.
5. Diseñar y sintonizar las ganancias de dos controladores PID independientes (normotenso-hipotenso y normotenso-hipertenso) mediante la herramienta Tune de Simulink.
6. Analizar y comparar el comportamiento en lazo abierto y lazo cerrado de los modelos en MATLAB y Python para la verificación cruzada entre plataformas.
7. Elaborar un diagrama biológico (BioRender) que relacione las estructuras cardiovasculares con los parámetros $Z$, $C$, $R$ y $L$.

## Descripción detallada del sistema

El modelo Windkessel de cuatro elementos representa un sistema dinámico de segundo orden que modeliza las características hemodinámicas del sistema arterial humano. La analogía electro-hidráulica se establece mapeando la presión arterial $P(t)$ con el voltaje $V(t)$ y el flujo sanguíneo $F(t)$ con la corriente $I(t)$.

El circuito equivalente está integrado por cuatro parámetros hemodinámicos:
* **Impedancia característica ($Z$):** Representa la oposición al flujo en la región proximal de la aorta.
* **Inertancia arterial ($L$):** Representa los efectos inerciales asociados con la masa y aceleración de la sangre en movimiento.
* **Distensibilidad arterial total ($C$):** Representa la capacidad del lecho arterial para almacenar volumen mediante elasticidad/distensión.
* **Resistencia periférica ($R$):** Representa la oposición al flujo en los vasos periféricos y arteriolas.

Aunque cuenta con cuatro elementos, el circuito contiene únicamente dos elementos independientes de almacenamiento de energía ($C$ y $L$), por lo que su dinámica se describe mediante dos variables de estado: el flujo a través de la inertancia $F_L(t)$ y la presión asociada a la distensibilidad arterial $P_p(t)$, considerando la presión arterial $P_a(t)$ como la entrada del sistema.

En esta práctica se analizan tres condiciones fisiológicas variando la distensibilidad arterial ($C$):
1. **Normotenso ($C = 1.500\text{ mL/mmHg}$):** Sirve como modelo de referencia (control) con respuesta sobreamortiguada y polos reales estables.
2. **Hipotenso ($C = 3.500\text{ mL/mmHg}$):** Un incremento en la capacitancia arterial atenúa las variaciones de presión, presentando un comportamiento subamortiguado con polos complejos conjugados.
3. **Hipertenso ($C = 1.000\text{ mL/mmHg}$):** Una reducción en $C$ denota mayor rigidez arterial, dando lugar a una respuesta críticamente amortiguada con polos reales repetidos.

Se diseñan e implementan esquemas de control con controladores PID sintonizados para reducir la discrepancia de las respuestas de los casos hipotenso e hipertenso con respecto a la respuesta de referencia del paciente normotenso.

**Palabras clave:** Modelo Windkessel; Sistema cardiovascular; Hemodinámica; Controlador PID; Distensibilidad arterial; Circuito equivalente RLC; Simulaciones *in silico*.

## Lista de archivos incluidos en el repositorio
1. Cuaderno computacional de MATLAB [.mlx]. si
2. Modelo de Simulink y Simscape Electrical [.slx]. si
3. Archivos del código fuente de Python [.py]. si
4. Imagen con las ganancias de los controladores PID sintonizados en Simulink. si
5. Figuras de las simulaciones de lazo abierto y lazo cerrado en MATLAB y Python [.pdf]. si
6. Capturas de pantalla de las simulaciones y del esquema de control. 
7. Diagrama biológico del sistema cardiovascular realizado en BioRender. si
8. Archivo de metadatos de citación [CITATION.cff]. 

## Referencias
\[1] P. A. Valle, Syllabus para Modelado de Sistemas Fisiológicos, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2026. Permalink: https://biomath.xyz/course/

\[2] M. C. Khoo, Physiological Control Systems: Analysis, Simulation, and Estimation, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018.

\[3] N. S. Nise, Control Systems Engineering, 8th ed. Hoboken, New Jersey, USA: John Wiley & Sons, 2020.

\[4] J. E. Hall, Guyton and Hall Textbook of Medical Physiology, 14th ed. Elsevier, 2021.
