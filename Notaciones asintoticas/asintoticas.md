# ¿Qué son las notaciones asintóticas y cómo se usan?

Una notación asintótica es una notación que se usa para representar matemáticamente el comportamiento de una función, pero en las ciencias de la computación se utilizan principalmente para tener una aproximación de la complejidad temporal o espacial de un algoritmo, de esta manera nos podemos hacer una idea de la eficiencia de nuestros programas.

## ¿Qué es la complejidad de un algoritmo?

La complejidad de un algoritmo se puede medir de dos maneras distintas:
1. **Complexidad temporal**: Es la cantidad de operaciones que se realizan en un algoritmo para resolver un problema.
2. **Complexidad espacial**: Es la cantidad de operaciones que se realizan en un algoritmo para resolver un problema, pero en una dimensión dada.


## ¿Cómo medir el desempeño de un algoritmo?

Para ello existen muchos principios, pero solo nombraré 4 de ellos:

 1. **Secuencia de acciones**: La suma de los costos de cada acción que se realiza en un algoritmo.
 2. **Alternación**: En el caso de que existen múltiples opciones, se debe determinar cuantas veces se efectua cada alternativa.
 3. **Ciclos**: Se debe evaluar la cantidad de veces que se repite una acción.
 4. **Llamadas a procesos**: El costo de una llamada a un cuerpo (proceso, método o función) que se realiza en un algoritmo.

## Notaciones asintóticas

Existen varias notaciones asintóticas que se pueden usar para medir la complejidad de un algoritmo. algunas más comunes son:

1. **Big Oh**: Es una notación que nos permite saber una cota superior de la cantidad de operaciones que realiza un algoritmo. Que se define como:
   
   Para un $f(x) = O(g(x))$, entonces $|f(x)| \leq c|g(x)|$, donde $c$ es una constante mayor a 0, y a partir de un valor de $x$, que por lo general se escribe como $x_0$.
   

    ![](https://www.tutorialspoint.com/assets/questions/media/9995/big_oh_notation.jpg)

2. **Big Omega**: Al igual que Big Oh, este da una cota, pero en este caso una inferior. Se define como:
   
   Para un $f(x) = \Omega(g(x))$, entonces $|f(x)| \geq c|g(x)|$, para $c>0$ y $x \geq x_0$.
   

   ![](https://www.tutorialspoint.com/assets/questions/media/9995/big_omega_notation.jpg)
   
3. **Big Theta**: Es una notación que nos permite saber una cota inferior y superior del algoritmo. Su definición matemática es:

    Para un $f(x) = \Theta(g(x))$, entonces $f(x)=O(g(x))$ y $f(x)=\Omega(g(x))$, para $x \geq x_0$.

    ![](https://www.tutorialspoint.com/assets/questions/media/9995/big_theta_notation.jpg)



Además de estas, existen muchas más. Algunos ejemplos son:

1. **Little Oh**: Es decir $f(x) = o(g(x))$ que se define como $\lim_{x\rightarrow \infty} \frac{f(x)}{g(x)} = 0$
2. **Little Omega**: Es decir $f(x) = \omega(g(x))$ que se define como $\lim_{x\rightarrow \infty} \frac{f(x)}{g(x)} \not= 0$
3. **Landau Notation**: Esta es una de las más peculiares, que se define como $f(x)\sim g(x)$, de manera que, $\lim_{x\rightarrow \infty} \frac{f(x)}{g(x)} = 1$

Estas notaciones son poco utilizadas, pero es conveniente saber que existen.

> Nota: No te preocupes demasiado por las matemáticas, estas notaciones estan echas para poder ayudarte a medir la complejidad de tu algoritmo. Es recomendable que sepas que existen y usar las notaciones que más te convengan.

## ¿Cómo medir la complejidad de un algoritmo?

Teniendo toda esta información en mente podemos medir la complejidad de nuestros programas siguiendo la lógica de los siguientes ejemplos:

### Factorial

Un ejemplo básico de algoritmo, es el cálculo del factorial, en este caso de manera recursiva. Para calcular la complejidad temporal (cuántas operaciones debe hacer mi programa para dar una solucion) de un algoritmo es la siguiente:

Dado el siguiente algoritmo
``` Haskell
let factorial = fn n::int -> int {
    if n < 2 then { return 1; }
    else {
        return n * factorial(n-1);
    }
}
``` 
Para calcular la complejidad debemos saber que en caso de que sea menor a 2, el factorial es 1, es decir, solo hará una operación, en otras palabras $T(1) = 1$ y para $n > 2$ la complejidad temporal es $T(n+1) = T(n) + 1$, es decir, la cantidad de operaciones del factorial anterior más una operación que se realiza para calcular el factorial de 1. Esto lo podemos expandir de la siguiente manera:

$T(1) = 1\\
T(2) = T(1) + 1 = 2\\
T(3) = T(2) + 1 = 3\\
...\\
T(n) = O(n)$

Tal como podemos ver, la complejidad temporal de este algoritmo es $O(n)$ lo que nos dice que crece linealmente su complejidad.

### Las torres de Hanoi
``` Haskell
let hanoi = fn n::int, src::str, tmp::str, dst::str -> int {
    if n > 0 then {
        hanoi(n-1, src, tmp, dst);
        printLn("Move disk " + to_string(n) + " from " + src + " to " + dst);
        hanoi(n-1, tmp, dst, src);
    }
}
```

Siguiendo la misma lógica de antes, para $T(0) =0$ y para $T(n+1) = 2T(n) + 1$, de manera que al expandir se obtiene:

$T(0) = 0\\
T(1) = 2T(0) + 1 = 1\\
T(2) = 2T(1) + 1 = 3\\
T(3) = 2T(2) + 1 = 7\\
...\\
T(n) = 2^n - 1$

En este caso no estan evidente si existe una cota superior (Big Oh), pero con un poco de matemaáticas podemos obtener que es $O(2^n)$ lo que nos dice que crece exponencialmente su complejidad. 
> La demostración es relativamente sencilla, pero es una tarea para ti ¡Ánimo! :D

Estos son algunos ejemplos de algoritmos que podemos medir su complejidad temporal, pero no todos. Existen algunos algoritmos que no son sencillos de medir, como por ejemplo el algoritmo **Merge Sort**, en el cual debes usar **El Teorema Maestro**.



## ¿Cómo puedo saber si mi programa es eficiente?

Para ello, podemos usar la notación de Big Oh, con la siguiente imagen:

![](https://codeyz.com/wp-content/uploads/2020/07/01_mfiw3erf3-594x512.png)

Lo que debes tomar en cuenta es que mientras más rápido crezca la función, más recursos o tiempo tu algoritmo necesita, por lo que lo más eficiente seria que fuera $O(1)$, es de creciemiento constante (un ejemplo puede ser los diccionarios de Python, luego vendria seguido por $O(\log{n})$), $O(\sqrt{n})$, $O(n)$, $O(n\log{n})$, $O(n^2)$, $O(2^n)$, $O(n!)$, etc. Eso sí, debes tomar en cuenta desde que punto en adelante.

## Conclusión
Ya con todas estas herramientas tenemos lo basico para comenzar a medir la complejidad de nuestros algoritmos o programas, lo cual puede ser muy util si lo que necesitas es rapidez y eficiencia. También para elegir que algoritmo utilizar o incluso comenzar a crear tus propios algoritmos a la medida. 

Recuerda que hay todo un mundo de conocimientos sobre cosas como complejidad, desibilidad, algoritmos, etc. Transversales a las ciencias de la computación, con aplicaciones en multiples campos, como la fisica, la biologia y el desarrollo de software. Si quieres saber más de este grandioso mundo dime en comentarios para seguir compartiendo todo sobre esta maravillosa area del conocimiento.



 


