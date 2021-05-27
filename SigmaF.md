# Cómo creé mi propio lenguaje de programación

![Persona programando](https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1052&q=805)

Si eres programador o ya tienes experiencia con los lenguajes de programación sabrás que existen muchísimos hoy en día, cada uno con sus fortalezas y debilidades, su sintaxis y peculiaridades. 

Quizás hayas pensado en que un lenguaje sería mejor con cierta cualidad. O tal vez pensaste en resolver un tipo de problema, pero las herramientas que tenías no se acoplaban lo suficiente a lo que necesitabas. Para ello una solución que encontré fue crear mi propio lenguaje de programación. Aquí te contaré cómo lo hice. :wink:

## ¿Qué tomar en cuenta antes de empezar?

### Paradigma
Una de las principales cualidades de un lenguaje de programación es el [paradigma](https://platzi.com/cursos/historia-programacion/) al que pertenece. Existen dos clasificaciones principales de ellos: **imperativos** y **declarativos**. Por ejemplo:

* Imperativos:
    - Programación procedimental
    - Programación orientada a objetos o POO
* Declarativo:
    - Programación funcional
    - Programación lógica  

Dentro de cada uno de estos paradigmas podemos encontrar varios lenguajes, como:

* C (imperativo, procedimental).
* Java (imperativo, POO).
* Haskell (declarativo, funcional).
* Prolog (declarativo, lógico).

También existen los lenguajes **multiparadigma**, lenguajes en los que puedes programar en múltiples paradigmas o mezclando varios paradigmas. Algunos ejemplos son:

* Python
* JavaScript
* Julia

### Interpretado o compilado

Para crear un nuevo lenguaje debes tomar en cuenta cómo el computador entenderá tu lenguaje. Puede hacerse con **intérpretes** o **compiladores**. 

A grandes rasgos, los lenguajes compilados son aquellos que se traducen a un lenguaje máquina para que el computador pueda entenderlo desde un archivo ejecutable. En cambio, los lenguajes interpretados se leen instrucción por instrucción y se ejecutan paso a paso conforme se leen.


![Imgur](https://i.imgur.com/kn5IDhU.png)


### Sintaxis y semántica

Luego de eso también se debe pensar en su sintaxis y semántica.

- Sintaxis: se define como las reglas que verifican si el conjunto de símbolos de un programa está bien escrito o no. 

- Semántica:  es cómo el computador entiende el programa cuando lo ejecutamos. Para ello postula una máquina abstracta con las reglas de ejecución de un programa.

> Si quieres saber más de la maquina abstracta te recomiendo el 
[Curso de Historia de la Programación: Lenguajes y Paradigmas](https://platzi.com/clases/historia-programacion/) 

Deberás buscar que tu lenguaje sea fácil y claro de entender, según su propósito.

## ¿Y ahora cómo empiezo a crear mi lenguaje? :thinking:

Una vez que pensé en los puntos anteriores fue que comencé mi propio lenguaje de programación al ver el [Curso de Introducción al Desarrollo de Lenguajes de Programación](https://platzi.com/cursos/desarrollo-lenguajes-programacion/) y el [Curso de Creación Lenguajes de Programación: Intérpretes](https://platzi.com/cursos/interpretes-software/). 

Decidí que sería un lenguaje interpretado para seguir con el curso. Además que es una de las formas más simples de comenzar con un lenguaje. En un comienzo no tenia un problema claro que resolver, sino que lo veía más como un reto y ambicioso proyecto. 

### No te olvides de los detalles 

Citando a mi profesor de lenguajes de programación:
> "Hacer un lenguaje de programación es mitad diseñarlo y hacerlo bien y la otra mitad es community management".

Mi lenguaje lo llamé [SigmaF](https://github.com/FabianVegaA/sigmaF) porque quería que fuese funcional, ya que yo estaba muy emocionado de haber conocido Haskell  y para que sonara lo más matemático posible.

Elegí una letra griega que me gustara y quedara bien, en un nombre sucedido por la letra F por funcional. Y así es como nació el concepto de SigmaF.

Otro detalle importante es cómo los demás interactúan con tu lenguaje. Es decir, como está construido, en mi caso yo use **Python 3.8** y **TDD** o ***Test-driven development*** para su desarrollo lo que agiliza la implementación de nuevas cualidades y permite anticiparte a los problemas o *bugs* que se puedan presentar.

Si tienes más interés por saber como lo hice o te interesa contribuir en este lenguaje te invito a mi repositorio en GitHub que encontraras en este [enlace](https://github.com/FabianVegaA/sigmaF).

![SigmaF consola](https://images.unsplash.com/photo-1616091238212-aca6808e3cf0?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1750&q=80)

### Dale un propósito  :raised_hands: 

En este momento el propósito de SigmaF es ser un puente entre el **paradigma funcional** y el **paradigma imperativo**, ya que la mayoría no suelen ser tan fáciles de aprender, especialmente si te has acostumbrado a programar imperativamente. Por ello quiero que este sea un lenguaje fácil de aprender para cualquier programador, y los que no lo son aún, siendo la puerta para otros lenguajes funcionales.

## Ahora te toca a ti crear tu lenguaje

Espero que con todo esto te animes a crear tu propio lenguaje o a apoyar otros en desarrollo. Ya tienes varias herramientas a tu disposición, para profundizar en ellas toma el [**Curso de Introducción al Desarrollo de Lenguajes de Programación**](https://platzi.com/clases/desarrollo-lenguajes-programacion/) y cuéntame aquí en comentarios cómo será tu lenguaje. :muscle: