*Rendering a fractal using Newton's method*

Author : Mathis CARPENTIER, Engineering student at IPSA

The purpose of this paper is to log my experience while working project.

The project itself was created after I watched [[https://www.youtube.com/watch?v=-RdOwhmqP5s|this]] video from the Youtube channel 3Blue1Brown about Newton's fractal, which greatly fascinated me, as Newton's method is something I have already come across as an engineering student, yet I was completely unaware that it was capable of producing beautiful and interesting fractals such as those produced in this project.

Not only has the project yielded mesmerising results, but it also has helped me improve my knowledge in both mathematics and programming.

This paper will fully explain the method used to create Newton's fractals.
# Principle
Newton's method is a root-finding algorithm, which allows to approximate the root(s) of a function. This method goes as follows:
- An initial input $x_0$ is chosen, generally at random, with $f(x_0)$ being its image.
- A step to take from this point is calculated with the following equation : $$\mathrm{step}=\frac{f(x_0)}{f'(x_0)}$$
- A new value $x_1$ is defined as follows : $x_1=x_0-\mathrm{step}$ 
- The previous steps are repeated using $x_1$, then $x_2$, and so on until a certain integer $n$ is reached, where $f(x_n)$ is generally an approximation of one of the roots of the function.

Notes :
- A larger value for $n$ tends to yield a more precise approximation.
- The method must be run multiple times with different values for $x_0$ for more complete results when dealing with functions with multiple roots.
- The method is not 100% reliable. There are some cases where the values of $x_n$ will bounce a lot, yielding extremely imprecise results. In these cases, $x_n$ does tend to eventually stabilise to a root, however the steps it takes vary a lot, possibly too many for a computer to calculate in a reasonable amount of time.

Most of the time, the method is used to find real roots. However, it can also be used to find complex roots, which we will be doing. This is because our fractal is rendered in two dimensions, and by using complex numbers, we can attribute the real part as the abscissa and the imaginary part as the ordinate, so that any number $z=a+ib$ will correspond to a point on a 2D plane with a positions of $\binom{a}{b}$.

We will consider a grid of points all corresponding to different complex numbers.
Let $P(z)$ be a polynomial function that takes in a complex number and outputs another complex number. We will assert that this polynomial has multiple roots in the complex set.

Our objective is to determine for each number in our grid which root said number will end up closest to after applying Newton's method with that number as an input. We will represent the results in a graphic with colour-coded regions, with each colour representing a certain root which the points inside regions of the same colour approach after applying Newton's method.
# Coding the fractal
In order to achieve our graphic, we will be using the Python programming language.
## Implementing Newton's method

We will be dealing with complex numbers, which aren't built-in to Python, therefore they will be represented by a custom class containing two attributes, the first representing the real part, and the second representing the imaginary part. We will also define all necessary arithmetic operations for complex numbers in this class.

Due to the nature of this implementation of complex numbers, it is important that they are represented in the $\alpha+i\beta$ form.

We will be using the classic function used for Newton's fractal, which is : $$f(x)=x^3-1$$
This polynomial has three roots : $$1;-\frac{1}{2}+i\frac{\sqrt{3}}{2};-\frac{1}{2}-i\frac{\sqrt{3}}{2}$$
We know that the input to this function will always be a complex number of the $a+ib$ form, therefore we can rewrite the function's expression as : $$f(a+ib)=(a+ib)^3-1$$
However, as mentioned previously, it is imperative that all complex numbers use the $a+ib$ form, which includes the output of the function, as such we will refactor this expression in the following way:
$$f(a+ib)=(a+ib)^3-1$$$$=a^3+3a^2ib+3a(ib)^2+(ib)^3-1$$$$=a^3-3ab^2-1+i3a^2b-ib^3$$$$=a^3-3ab^2-1+i(3a^2b-b^3)$$
Thanks to this new expression, we can now easily implement the function in Python :
```python
def f(z : Complex) -> Complex:
	a,b = z.a, z.b # Unpacking the input as two variables for convenience
	f_a = pow(a,3) - 3*a*pow(b,2) - 1 # real part
	f_b = 3*pow(a,2)*b - pow(b,3) # imaginary part
	return Complex(f_a, f_b)
```

The same is done for the derivative of this function : $$f'(a+ib)=3(a+ib)^2$$ $$=3(a^2+2aib+b^2)$$ $$=3(a^2+b^2)+i(6ab)$$
```python
def fder(z : Complex) -> Complex:
	a,b = z.a, z.b 
	fder_a = 5*(a*a + b*b)
	fder_b = 6*a*b
	return Complex(fder_a, fder_b)
```

Now that both our function and its derivative are implemented, we can use Newton's, which we will implement in the following manner :
```python
EPSILON = 1e-10
MAX_STEPS = 1000

def newton(z0 : Complex, f : Callable, fder : Callable) -> Complex:
	global EPSILON, MAX_STEPS
	if abs(fder(z0)) < EPSILON: return z0 # to avoid dividing by zero
	values = [z0,z0 - f(z0)/fder(z0)]
	iteration = 0
	
	while iteration < MAX_STEPS and abs(values[-1] - values[-2]) > EPSILON:
		z = values[-1]
		values.append(z - f(z)/fder(z))
		iteration += 1
	return values[-1]
```

## Creating the data for the graphic
Now that we have implemented Newton's method, we need to apply it to a grid of points and see which root the method approximates from it.

To do this, we will be going over every pixel, getting their location relative to the center of the screen, and then applying Newton's method, before assigning said pixel a number representing the specific root the method approached.

We start by generating a grid using this function :
```python
def create_grid(height:int, width:int,scale_x:float,scale_y:float) -> list:  
    grid = []  
    for line in range(height):  
        new_line = []  
        for column in range(width):  
            scaled_x = ((column - width // 2) / width) * scale_x  
            scaled_y = ((height // 2 - line) / height) * scale_y  
            position = Complex(scaled_x, scaled_y)  
            new_line.append(position)  
        grid.append(new_line)  
    return grid
```
For each value in this grid, its position in the complex plane is inscribed.

Then, we run through the grid and, using the complex value stored in each pixel (represented by a value in the grid), we apply Newton's method on it, determine the closest root from the approximated result, and attribute an index for said root :


## Drawing the graphic
[WIP]
