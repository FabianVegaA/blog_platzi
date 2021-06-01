# Qué es la programación funcional

Muchas veces dentro del mundo de la programación debes haber escuchado sobre la programación orientada a objetos (*OOP* por sus siglas en inglés) o programcion procedimental. A esto se les llama paradigmas de la programación, que son formas de solucionar un problema, pero ¿alguna vez has oido hablar de la programación funcional? Si no, ahora te cuento y si has escuchado de ella te cuento porque deberias aprenderla.

La programación funcional a diferencia de la programación procedimental o la *OOP*, es un paradigma **declarativo** ¿qué signica eso? Pues a grandes razgos en estos paradigmas tu en vez de decir "cómo", tu dices que es lo que necesitas.

## ¿Cuáles son sus ventajas?
En el punto de vista tecnico existen varias ventajas sobre otros paradigmas como su facilidad para poder utilizar la concurrencia y la ausencia de *side-effect* o efectos colaterales. Además de una sintaxis limpia y clara.



## ¿Cómo comienzo?
Esto depende, existen varios lenguajes multiparadigmas que admite en cierta forma la programación funcional, como Python y Javascript. Tambien existen lenguajes puramente funcionales, como Lisp, Scala y [Haskell](http://aprendehaskell.es/main.html) (mi favorito), que permiten este paradigma en todo su explendor.

> Por cierto, yo cree mi propio lenguaje de programación open-source y funcional llamado *SigmaF*, te dejo el repositorio de [GitHub](https://github.com/FabianVegaA/sigmaF) y un post para saber más sobre este haz click [aquí](https://platzi.com/blog/crear-lenguaje-programacion/). Tambien puedes preguntarme a traves de mi Twitter [@fabianmativeal](https://twitter.com/fabianmativeal).


### Algunos ejemplos

1. Probablemente alguna vez te encontraste con el problema de imprimir esto:
```
*
**
***
****
*****
```

Pues ahora te dejo con la solución funcional usando *SigmaF*.
``` Haskell
let stairs = fn i::int -> str {
	if i == 1 then {
		=> "*\n";
	}
	=> stairs(i-1) + sconcat(srepeat("*", i)) + "\n";
}

printLn(stairs(5))
```

2. Este programa te da los números primos usando Haskell
``` Haskell
factors :: Int -> [Int]
factors n = [x | x <- [1..n], n `mod` x == 0]

isPrime :: Int -> Bool
isPrime n = factors n == [1,n]

primes :: [Int] -> [Int]
primes n = [x | x <- [2..n], isPrime x]
```

3. O un simplemente un "*Hello, World!*" usando Scala
``` Scala
object HolaMundo {
  def main(args: Array[String]) {
    println("¡Hola, mundo!")
  }
}
```
## Mi recomendación
Aprender un nuevo paradigma es buenisimo para poder ver la programación desde otra perspectiva y si logras aprender a utilizarlo tendras una nueva herramienta poderosisima para entrentarte a casi cualquier problema en la programación. Desde mi experiencia, pasar de la programación *imperativa* a la funcional es dificil, pero estoy convecido de que vale la pena.

Si te interesa seguir aprendiendo del tema te recomiendo [Curso de Historia de la Programación: Lenguajes y Paradigmas](https://platzi.com/clases/historia-programacion/), [Curso de Programación Funcional con Scala](https://platzi.com/clases/scala/) y este tutorial de [Haskell](http://aprendehaskell.es/main.html).



