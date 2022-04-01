# Wilf

We've got generating functions.

## TODO

### powerseries.py
* [x] Tests
* [x] Confirm PowerSeries works for complex coefficients
* [x] Integration of symbolic expressions
* [ ] Allow providing an arbitrary expression to replace PowerSeries.x
* [ ] Probably rename to Generating Function, or maybe OrdinaryGeneratingFunction.
* [ ] Explore multivariate systems
* [ ] Look into techniques to improve numerical stability.
* [ ] Make sure that the code works with sympy.Symbol objects, as a replacement
      for symbolics.py.
* [ ] Implement other generation fucntion, e.g., ExponentialGeneratingFunction
      Dirichlet Series Generating Functions, etc. (lower priority)
* [ ] Allowing a functional modification of x e.g., f(x) -> e^(-iwt) would allow
      the code to be used for discrete fourier transforms (lower prioirty)
* [ ] It could be nice to extend the PowerSeries class to a Polynomial class
      in which the maximum degree is explicitly defined. This could then be used
      to define systems of polynomial equations, algebraic varieties, and all sorts of cool things from computational algebraic geometry.


### symbolics.py
* [x] Tests
* [ ] Better __str__. Currently only works for simple expressions, and not at all for nested expressions.
* [ ] Rational simplification - Automatically reduce rationals to their lowest terms
* [ ] Exponent simplification - E.g., reduce x * x * x -> x**3
* [ ] It would be useful if subs could take numpy arrays, like sympy.lambdify
* [ ] Some symbolic representation of basic functions are going to be needed. E.g., in powerseries.exp, there is a call to cmath.exp that currently fails when the argument is an Expression. To get around this I need an wilf.symbolics.exp. Probably also log, sin, and cos. Probably others.
        Note: I've worked around this problem for now. Low priority.


## References

### Formal power series and generating functions
* Grahah; Kunoth; Patashnik (1994). Concrete Mathematics. Addison-Wesley.
* Wilf, James. (2008). Generatingfunctionology. Retrieved from https://www2.math.upenn.edu/~wilf/gfology2.pdf
* Jiszka, Jason. (2013). Infinite lazy polynomials. Retrieved from http://blog.jliszka.org/2013/10/31/infinite-lazy-polynomials.html
