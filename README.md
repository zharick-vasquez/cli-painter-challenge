[![es](https://img.shields.io/badge/lang-es-green)](README.es.md)

# CLI Painter

CLI Painter is a console app to draw basic geometric figures. Its purpose is to practice OOP basic concepts in python by developing a simple CLI application.

## Activity Description

Fork this repository to your github account, then clone it. After that, in the `model.py` module create the following classes:

### Point class

-  A `Point` class with two attributes `x` and `y` of type `float`. Both attributes should be initialized with paramaters in the constructor.

### Circle class

- A `Circle` class  with tha attributes `center` of type `Point` and `radius` of type `float`. Both attributes should be initialized with parameters in the constructor.

- A method `area` that returns the area of the circle as a `float`.

- A method `draw` that creates a drawing of the circle. Use the following code to draw the circle in the method's body:

    ```python
    circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
    plt.gca().add_patch(circle)
    plt.axis("scaled")
    plt.show()
    ```

    For this code to work, you need to import the `matplotlib.pyplot` module at the beginning of the file, like this:

    ```python
    import matplotlib.pyplot as plt
    ```

- A method `__str__` that returns a string representation of the circle in the following format:

    ```python
    Circle with center at (x, y) and radius r
    ```

    where `x`, `y` and `r` are the values of the center's x and y coordinates and the radius of the circle, respectively.

### Triangle class

- A `Triangle` class with the attributes `point_1`, `point_2` and `point_3` of type `Point`. All attributes should be initialized with parameters in the constructor.

- A method `area` that returns the area of the triangle as a `float`.

- A method `draw` that creates a drawing of the triangle. In the method's body, use the following code to draw the triangle:

    ```python
    x = [self.point_1.x, self.point_2.x, self.point_3.x, self.point_1.x]
    y = [self.point_1.y, self.point_2.y, self.point_3.y, self.point_1.y]
    plt.fill(x, y, color='b')
    plt.axis("scaled")
    plt.show()
    ```
    
    For this code to work, you need to import the `matplotlib.pyplot` module at the beginning of the file, like this:

    ```python
    import matplotlib.pyplot as plt
    ```

- A method `__str__` that returns a string representation of the triangle in the following format:

    ```python
    Triangle with vertices at (x1, y1), (x2, y2) and (x3, y3)
    ```

    where `x1`, `y1`, `x2`, `y2`, `x3` and `y3` are the values of the x and y coordinates of the triangle's vertices.

### Rectangle class

- A `Rectangle` class with the attributes `point_1` and `point_2` of type `Point` that represent the opposite vertices of the rectangle. Both attributes should be initialized with parameters in the constructor.

- A method `area` that returns the area of the rectangle as a `float`.

- A method `draw` that creates a drawing of the rectangle. In the method's body, use the following code to draw the rectangle:

    ```python
    x = [self.point_1.x, self.point_2.x, self.point_2.x, self.point_1.x, self.point_1.x]
    y = [self.point_1.y, self.point_1.y, self.point_2.y, self.point_2.y, self.point_1.y]
    plt.fill(x, y, color='g')
    plt.axis("scaled")
    plt.show()
    ```

    For this code to work, you need to import the `matplotlib.pyplot` module at the beginning of the file, like this:

    ```python
    import matplotlib.pyplot as plt
    ```

- A method `__str__` that returns a string representation of the rectangle in the following format:

    ```python
    Rectangle with opposite vertices at (x1, y1) and (x2, y2)
    ```

    where `x1`, `y1`, `x2` and `y2` are the values of the x and y coordinates of the rectangle's opposite vertices.

### Painter class

To complete the classes, create a `Painter` class with the following code:

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

For this code to work, you need to import the `pickle` module at the beginning of the file, like this:

```python
import pickle
```
