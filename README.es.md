[![en](https://img.shields.io/badge/lang-en-blue)](README.md)

# CLI Painter

CLI Painter es una aplicación de consola para dibujar figuras geométricas básicas. Su propósito es practicar los conceptos básicos de POO en python desarrollando una aplicación CLI simple.

## Descripción de la actividad

Hacer un fork de este repositorio en tu cuenta de github, luego clonarlo. Después, en el módulo `model.py` crear las siguientes clases:

### Clase Point

- Una clase `Point` con dos atributos `x` e `y` de tipo `float`. Ambos atributos deben ser inicializados con parámetros en el constructor.

### Clase Circle

- Una clase `Circle` con los atributos `center` de tipo `Point` y `radius` de tipo `float`. Ambos atributos deben ser inicializados con parámetros en el constructor.

- Un método `area` que devuelve el área del círculo como un `float`.

- Un método `draw` que crea un dibujo del círculo. Utiliza el siguiente código para dibujar el círculo en el cuerpo del método:

    ```python
    circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
    plt.gca().add_patch(circle)
    plt.axis("scaled")
    plt.show()
    ```

    Para que este código funcione, necesitas importar el módulo `matplotlib.pyplot` al principio del archivo, así:

    ```python
    import matplotlib.pyplot as plt
    ```

- Un método `__str__` que devuelve una representación en cadena del círculo en el siguiente formato:

    ```python
    Circle with center at (x, y) and radius r
    ```

    donde `x`, `y` y `r` son los valores de las coordenadas x e y del centro y el radio del círculo, respectivamente.

### Clase Triangle

- Una clase `Triangle` con los atributos `point_1`, `point_2` y `point_3` de tipo `Point`. Todos los atributos deben ser inicializados con parámetros en el constructor.

- Un método `area` que devuelve el área del triángulo como un `float`.

- Un método `draw` que crea un dibujo del triángulo. En el cuerpo del método, utiliza el siguiente código para dibujar el triángulo:

    ```python
    x = [self.point_1.x, self.point_2.x, self.point_3.x, self.point_1.x]
    y = [self.point_1.y, self.point_2.y, self.point_3.y, self.point_1.y]
    plt.fill(x, y, color='b')
    plt.axis("scaled")
    plt.show()
    ```

    Para que este código funcione, necesitas importar el módulo `matplotlib.pyplot` al principio del archivo, así:

    ```python
    import matplotlib.pyplot as plt
    ```

- Un método `__str__` que devuelve una representación en cadena del triángulo en el siguiente formato:

    ```python
    Triangle with vertices at (x1, y1), (x2, y2) and (x3, y3)
    ```

    donde `x1`, `y1`, `x2`, `y2`, `x3` y `y3` son los valores de las coordenadas x e y de los vértices del triángulo.

### Clase Rectangle

- Una clase `Rectangle` con los atributos `point_1` y `point_2` de tipo `Point` que representan los vértices opuestos del rectángulo. Ambos atributos deben ser inicializados con parámetros en el constructor.

- Un método `area` que devuelve el área del rectángulo como un `float`.

- Un método `draw` que crea un dibujo del rectángulo. En el cuerpo del método, utiliza el siguiente código para dibujar el rectángulo:

    ```python
    x = [self.point_1.x, self.point_2.x, self.point_2.x, self.point_1.x, self.point_1.x]
    y = [self.point_1.y, self.point_1.y, self.point_2.y, self.point_2.y, self.point_1.y]
    plt.fill(x, y, color='g')
    plt.axis("scaled")
    plt.show()
    ```

    Para que este código funcione, necesitas importar el módulo `matplotlib.pyplot` al principio del archivo, así:

    ```python
    import matplotlib.pyplot as plt
    ```

- Un método `__str__` que devuelve una representación en cadena del rectángulo en el siguiente formato:

    ```python
    Rectangle with vertices at (x1, y1) and (x2, y2)
    ```

    donde `x1`, `y1`, `x2` y `y2` son los valores de las coordenadas x e y de los vértices opuestos del rectángulo.


### Clase Painter

Para completar las clases, crea una clase `Painter` con el siguiente código:
    
```python
class Painter:

FILE = ".painter"

def __init__(self) -> None:
    self.shapes: list = []
    self._load()

def _load(self) -> None:
    try:
        with open(Painter.FILE, "rb") as f:
            self.shapes = pickle.load(f)
    except (EOFError, FileNotFoundError):
        self.shapes = []

def _save(self) -> None:
    with open(Painter.FILE, "wb") as f:
        pickle.dump(self.shapes, f)

def add_shape(self, shape) -> None:
    self.shapes.append(shape)
    self._save()

def total_area(self) -> float:
    return sum(shape.area() for shape in self.shapes)

def clear(self) -> None:
    self.shapes = []
    self._save()
```

Para que este código funcione, necesitas importar el módulo `pickle` al principio del archivo, así:

```python
import pickle
```