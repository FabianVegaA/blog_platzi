# ¿Cómo creé mi propio lenguaje de programación?  :scream:

<img src="https://img.freepik.com/free-photo/working-code_1098-19858.jpg?size=626&ext=jpg&ga=GA1.2.1482204611.1614734745" alt="computer image" width=1000 height= 500>

Sí eres programador o ya tienes experiencia con los lenguajes de programación sabrás que existen muchísimos hoy en día, cada uno con sus fortalezas y debilidades, su sintaxis y peculiaridades. Quizás hayas pensado en que un lenguaje sería mejor con cierta cualidad u otra, o tal vez pensaste en resolver un tipo de problema, pero las herramientas que tenías no se acoplaban lo suficiente a lo que necesitabas. Para ello una solución que encontré fue crear un lenguaje de programación propio. Aquí te cuento cómo lo hice. :wink:

## ¿Qué debes tomar en cuenta?

### Paradigma
Una de las principales cualidades de un lenguaje de programación es el paradigma al que pertenece. Existe dos clasificaciones principales para los paradigmas. Los paradigmas **imperativo** y **declarativo**. Aquí te van algunos ejemplos:

* Imperativos:
    - Programación Procedimental
    - Programación Orientada a Objetos o POO
* Declarativo:
    - Programación Funcional
    - Programación Lógica  

Y para cada uno de estos paradigmas podemos encontrar un lenguaje, como:

* C (Imperativo, procedimental)
* Java (Imperativo, POO)
* Haskell (Declarativo, funcional)
* Prolog (Declarativo, lógico)

También existen los lenguajes **multiparadigma**, lenguajes en los que puedes programar en múltiples paradigmas o mezclando varios paradigmas. Algunos ejemplares son:

* Python
* Javascript
* Julia

### Interpretado o Compilado

Para crear un nuevo lenguaje, debemos tomar en cuenta todas estas variables, como por ejemplo, cómo hará el computador para entender tu lenguaje. Existen varias maneras de hacerlo, con **intérpretes** o **compiladores** principalmente. En grandes rasgos, los lenguajes compilados, son aquellos que se traducen a un lenguaje máquina para que esta pueda entenderlo, en cambio los lenguajes interpretados se leen instrucción por instrucción y ejecutándose paso a paso.


![Imgur](https://i.imgur.com/25U26xw.png)


### Sintaxis y Semántica

Luego de eso también se debe pensar en su sintaxis y semántica. Ahora te explico que son: 

- Sintaxis: En pocas palabras la sintaxis se define como las reglas que verifican si el *string* de un programa esta bien escrito o no. 

- Semántica: La semántica se describe en como el computador puede entender el programa cuando lo ejecutamos. Para ello lo que se hace es postular una maquina abstracta con las reglas de ejecucion de un programa.

> Si quieres saber más de la maquina abstracta te recomiendo el 
[Curso de Historia de la Programación: Lenguajes y Paradigmas](https://platzi.com/clases/historia-programacion/) 

Deberás buscar que tu lenguaje sea fácil y claro de entender, según su propósito.

## ¿Y ahora cómo empiezo a crear mi lenguaje? :thinking:

Así fue como comencé con mi propio lenguaje de programación, al ver el [**Curso de Introducción al Desarrollo de Lenguajes de Programación**](https://platzi.com/clases/desarrollo-lenguajes-programacion/) y el [**Curso de Creación Lenguajes de Programación: Intérpretes**](https://platzi.com/clases/interpretes-software/). Decidí que fuese un lenguaje interpretado para seguir con el curso, además de que es una de las formas más simples de comenzar con un lenguaje. 

En un comienzo no tenia un problema claro el cual resolver, sino que lo veia más como un reto y ambicioso proyecto. 

### No te olvides de los detalles 

Cito a mi profesor de Lenguajes de programación.
> " Hacer un lenguaje de programación es mitad diseñarlo y hacerlo bien y la otra mitad es community management."

Mi lenguaje lo llamé [SigmaF](https://github.com/FabianVegaA/sigmaF), ya que quería que fuese funcional, pues estaba en la fiebre de Haskell y quería que fuera lo más matemático posible, aunque no estoy seguro si lo logré :sweat_smile:. 
Es así como elegí una letra griega que me gustara y quedara bien, en un nombre sucedido por "F" por funcional. Y así es como nació [SigmaF](https://github.com/FabianVegaA/sigmaF).

![sigmaF](https://camo.githubusercontent.com/51012dfbaa85e52d026f6aba844a7cb691dce4693424b709322786934f6748b8/68747470733a2f2f692e696d6775722e636f6d2f625a52706145782e706e67)

### Dale un propósito  :raised_hands: 

En este momento el propósito de [SigmaF](https://github.com/FabianVegaA/sigmaF) es que fuese un lenguaje puente entre el **paradigma funcional** y el **paradigma imperativo**, pues la mayoría no suelen ser fáciles de aprender como Haskell que por experiencia son complejos de aprender cuando estás acostumbrado programar imperativamente. Por ello, quiero que este sea un lenguaje fácil de aprender para cualquier programador y los que no lo son aun, siendo la puerta para otros lenguajes funcionales.

## Ahora te toca a ti crear tu lenguaje

Espero que con todo esto te animes a crear tu propio lenguaje o a apoyar otros en desarrollo. Ya tienes varias herramientas a tu disposición. Para profundizar en ellas toma el [**Curso de Introducción al Desarrollo de Lenguajes de Programación**](https://platzi.com/clases/desarrollo-lenguajes-programacion/) y cuéntame aquí en comentarios cómo será tu lenguaje. :muscle: