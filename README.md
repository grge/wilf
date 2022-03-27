# Wilf

A toy probabilistic programming tool built around characteristic functions.

```python
    # Create two normal RVs
    x = wilf.normal(mean=1, std=2)
    y = wilf.normal(mean=4, std=1)
    # Get the sum of the two as a new RV
    z = x + y
    # calculate the mean and variance
    print(z.mean(), z.var())
```
## TODO

### rv.py
* [ ] Implement RV.cdf() RV.pdf(), RV.rvs()
* [ ] Implement __mul__, __pow__, __div__, etc
* [ ] Empirical characteristic function 
* [ ] Add explicit support for discrete distributions
* [ ] Multivariate constructions (joint, marginal, conditional)
* [ ] Conversion of MGFs or probability generating functions?

### powerseries.py
* [ ] Write tests for PowerSeries
* [ ] Confirm PowerSeries works for complex coefficients
* [ ] It could be nice to extend the PowerSeries class to a Polynomial class
      in which the maximum degree is explicitly defined. This could then be used
      to define systems of polynomial equations, algebraic varieties, and all sorts of cool things from computational algebraic geometry.

## References

### Formal power series and generating functions
* Grahah; Kunoth; Patashnik (1994). Concrete Mathematics. Addison-Wesley.
* Wilf, James. (2008). Generatingfunctionology. Retrieved from https://www2.math.upenn.edu/~wilf/gfology2.pdf
* Jiszka, Jason. (2013). Infinite lazy polynomials. Retrieved from http://blog.jliszka.org/2013/10/31/infinite-lazy-polynomials.html

### Characteristic functions
* Good, I. J. (1968). The characeristic functions of functions. https://www.jstor.org/stable/2416209
* Shephard, N. G. (1991). From characteristic function to distribution function: A simple framework. Econometric Theory, vol 7. 519-229. https://scholar.harvard.edu/files/ET91.pdf
* https://www.webdepot.umontreal.ca/Usagers/carrascm/MonDepotPublic/carrascm/Carrasco_Kotchoni_ET2017.pdf
* Carrasco, M., & Kotchoni, R. (2017). Efficient estimation using the characteristic function. Econometric Theory, 33(2), 479-526. https://www.webdepot.umontreal.ca/Usagers/carrascm/MonDepotPublic/carrascm/Carrasco_Kotchoni_ET2017.pdf
* u, J. (2004). Empirical characteristic function estimation and its applications. Econometric reviews, 23(2), 93-123. http://www.mysmu.edu/faculty/yujun/Research/YuER.pdf
