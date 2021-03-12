# ¿Cómo cree mi propio lenguaje de programación?  :scream:

<img src="https://img.freepik.com/free-photo/working-code_1098-19858.jpg?size=626&ext=jpg&ga=GA1.2.1482204611.1614734745" alt="computer image" width=1000 height= 500>

Sí eres programador o ya tienes experiencia con los lenguajes de programación sabrás que existen muchísimos hoy en día, cada uno con sus fortalezas y debilidades, su sintaxis y peculiaridades. Quizás hayas pensado en que un lenguaje sería mejor con cierta cualidad u otra, o tal vez pensaste en resolver un tipo de problema, pero las herramientas que tenías no se acoplaban lo suficiente a lo que necesitabas. Para ello una solución que encontré fue crear un lenguaje de programación propio. Aquí te cuento cómo lo hice. :wink:

## ¿Qué debes tomar en cuenta?

### Paradigma
Una de las principales cualidades de un lenguaje de programación es el paradigma al que pertenece. Existe dos clasificaciones principales para los paradigmas. Los paradigmas Imperativos y Declarativos. Aquí te van algunos ejemplos:

* Imperativos:
    - Programación Procedimental
    - Programación Orientada a Objetos o POO
* Declarativo:
    - Programación Funcional
    - Programación Lógica  

Y para cada uno de estos paradigmas podemos encontrar un lenguaje, como:

* C (Imperativo, procedimental)
* Java (Imperativo, POO)
* Haskell (Declarativo, Funcional)
* Prolog (Declarativo, Lógico)

También existen los lenguajes Multiparadigma, lenguajes en los que puedes programar en múltiples paradigmas o mezclando varios paradigmas. Algunos ejemplares son:

* Python
* Javascript
* Julia

### Interpretado o Compilado

Para crear un nuevo lenguaje, debemos tomar en cuenta todas estas variables, y contar algunas más, como por ejemplo, cómo hará el computador para entender tu lenguaje. Existen varias maneras de hacerlo, con Intérpretes o Compiladores principalmente. En grandes rasgos, un lenguaje Compilados, son aquellos que se traducen a un lenguaje máquina para que esta pueda entenderlo, en cambio los lenguajes interpretados se leen instrucción por instrucción y ejecutándose paso a paso.

<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile host=\&quot;app.diagrams.net\&quot; modified=\&quot;2021-03-12T01:26:41.410Z\&quot; agent=\&quot;5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36\&quot; etag=\&quot;EaSVoaFwyCVtK78ghZDD\&quot; version=\&quot;14.1.9\&quot; type=\&quot;google\&quot;&gt;&lt;diagram id=\&quot;KW2WlLn21J5BkVNL_qxn\&quot; name=\&quot;Page-1\&quot;&gt;7Vldb9owFP01eWyVxISQR0hpN62TJqFp26MhJrhzclNjStivn904kMThY2uBilZCKPfEn+dcX187FgqT/I7jbPYVIsIs145yC91Yrhv4XfmvgFUBeIFTADGnUQFVgBH9QzRoa3RBIzKvFRQATNCsDk4gTclE1DDMOSzrxabA6r1mOCYGMJpgZqI/aCRmBdpz/Q3+idB4VvbsdIPiTYLLwnom8xmOYFmB0NBCIQcQxVOSh4Qp7kpeinq3W96uB8ZJKg6p8NAnw+HT9zG7hce7/Ms8uyL9K93KE2YLPWE9WLEqGeCwSCOiGrEtNFjOqCCjDE/U26WUXGIzkTBpOfJRN0e4IPnWcTrr2UuvIZAQwVeySF5XflWa2l5W6C/LzCrUo5JorCWP101vWJEPmph/IMk1SPqcCsIzTiIpqUGYnLqoszIXHH6TEBhwiaSQypKDKWWsAWFG41SaE6Lal4Aikkpn7OsXCY0i1U2rDHWhppAKvZxc+3WUQUGnLo1rStNpUeZowiBDmBCSjLJ3rYrbPbMqjhlDSCSDqjaBixnEkGI23KANmjZl7gEyrdcDEWKlycMLAXU125lVHe/mVY4TFnxCdkzI0/sO5jERO8r57TpxwrCgT/VxvDrrnrkWrBBZAxTRWK4G+3ah3NdQZk88x/Os2FWnNFfqHMOB/UbAb/HfXov/9o7mv+jC/Lf7Qr/UVb8BlT2vZWtu1KjTEKRYL7pWQ5P1MP5fpu6lODxqy3BO6fDuWRxeksVXP3X9Z+OXMq690rzJqy9vVju30FdZKP6BgX6bvqeJ9L7h+IZ8ZYZyj8eEfYM5FRRUpjIGISBpSWEENNaBPK1kqrEkj9W57nqM53RynQFbxaqlgXoKAXj0PDtvIH/2tSs3odC2PDmE8Bnw64CjLFWqDvhes4pTAdwGYFSpNCp/xdAYVanbsVIu44zSsmWtk+PT7Fm24RTlGaUlBl5sLux6DWGCc+fC/oXlEk7nwBjpvDTreBnvnY8g+caCZFuac+Ig2XJGKu8L+PsNkgidO0gGH/lnJWYeElx7Zw2u+45ekUw57ERBfedxQVNs6LtRz9l/qXyCSzPkHBicukdbBL39O5ZshmbzbYHjxKdYL6iHETfwDAqDFgaDox1jzRx4JENxZHrfG+PR27tPnvY64ICPQm+MwUbW753bE92L8MQj3sRKc/Pls7gR3Hw+RsO/&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div>

### Sintaxis y Semantica

Luego de eso también se debe pensar en su sintaxis y semántica. Ahora te explico que son: 

- Sintaxis: En pocas palabras la sintaxis se define como las reglas que verifican si el *string* de un programa esta bien escrito o no. 

- Semantica: La semantica se describe en como el computador puede entender el programa cuando lo ejecutamos. Para ello lo que se hace es postular una maquina abstracta con las reglas de ejecucion de un programa.

> Si quieres saber más de la maquina abstracta te recomiendo el 
[Curso de Historia de la Programación: Lenguajes y Paradigmas](https://platzi.com/clases/historia-programacion/) 

Deberas buscar que tu lenguaje sea facil y claro de entender, según su proposito.

## ¿Y ahora cómo empiezo a crear mi lenguaje? :thinking:

Con todo eso y más se coloca las manos a la obra.

Así fue como comencé con mi propio lenguaje de programación, al ver el [**Curso de Introducción al Desarrollo de Lenguajes de Programación**](https://platzi.com/clases/desarrollo-lenguajes-programacion/) y el [**Curso de Creación Lenguajes de Programación: Intérpretes**](https://platzi.com/clases/interpretes-software/). Decidí que fuese un lenguaje interpretado para seguir con el curso, además de que es una de las formas más simples de comenzar con un lenguaje. 

En un comienzo no tenia un problema claro el cual resolver, sino que lo veia más como un reto y ambicioso proyecto. 

### No te olvides de los detalles 

Cito a mi profesor de Lenguajes de programación.
> " Hacer un lenguaje de programación es mitad diseñarlo y hacerlo bien y la otra mitad es community management."

Mi lenguaje lo llame [SigmaF](https://github.com/FabianVegaA/sigmaF), pues sabia que quería que fuese funcional pues estaba en la fiebre de Haskell y quería que fuese lo más matemático posible, aunque no estoy seguro si lo logre :sweat_smile:, es así como elegí una letra griega que me gustara y quedara bien en un nombre sucedido por "F" por funcional. Y nació [SigmaF](https://github.com/FabianVegaA/sigmaF).

![sigmaF](https://camo.githubusercontent.com/51012dfbaa85e52d026f6aba844a7cb691dce4693424b709322786934f6748b8/68747470733a2f2f692e696d6775722e636f6d2f625a52706145782e706e67)

### Un proposito  :raised_hands: 

En este momento el propósito de [SigmaF](https://github.com/FabianVegaA/sigmaF) es de que fuese un lenguaje puente entre los lenguajes del Paradigma Funcional y Paradigmas Imperativos, pues la mayoría no suelen ser fáciles de aprender como Haskell que por experiencia son complejos de aprender cuando estás acostumbrado programar imperativamente. Por ello quiero que este sea un lenguaje fácil de aprender para cualquier programador y los que no lo son siendo la puerta para otros lenguajes funcionales.

## Ahora te toca a ti crear tu lenguaje

Espero que con todo esto te animes a crear tu propio lenguaje o a apoyar otros en desarrollo. Ya tienes varias herramientas a tu disposición. Para profundizar en ellas toma el Curso de Introducción al Desarrollo de Lenguajes de Programación y cuéntame aquí en comentarios cómo será tu lenguaje. 