# Wilf

A toy probabilistic programming tool built around characteristic functions.

```python
    # Create two normal RVs
    x = wilf.normal(mean=1, std=1)
    y = wilf.normal(mean=4, std=2)
    # Get the sum of the two as a new RV
    z = x + y
    # print the mean and variance of the new RV
    print(z.mean(), z.var())
```
## TODO

### rv.py
* [ ] Implement RV.cdf() RV.pdf(), RV.rvs()
* [ ] Implement __mul__, __pow__, __div__, etc
* [ ] Add explicit support for discrete distributions
* [ ] Multivariate constructions (joint, marginal, conditional)
* [ ] Conversion of MGFs or probability generating functions?

### powerseries.py
* [ ] Write tests for PowerSeries
* [ ] Confirm PowerSeries works for complex coefficients
* [ ] It could be nice to extend the PowerSeries class to a Polynomial class
      in which the maximum degree is explicitly defined. This could then be used
      to define systems of polynomial equations, algebraic varieties, and all sorts of cool things from computational algebraic geometry.
* [ ] Look into techniques to improve numerical stability.

## References

### Formal power series and generating functions
* Grahah; Kunoth; Patashnik (1994). Concrete Mathematics. Addison-Wesley.
* Wilf, James. (2008). Generatingfunctionology. Retrieved from https://www2.math.upenn.edu/~wilf/gfology2.pdf
* Jiszka, Jason. (2013). Infinite lazy polynomials. Retrieved from http://blog.jliszka.org/2013/10/31/infinite-lazy-polynomials.html

### Characteristic functions

#### Algebraic maniupations
* Good, I. J. (1968). The characeristic functions of functions. https://www.jstor.org/stable/2416209

#### Inversion and sampling
* Shephard, N. G. (1991). From characteristic function to distribution function: A simple framework. Econometric Theory, vol 7. 519-229. https://scholar.harvard.edu/files/ET91.pdf
* Rácz, S., Tari, Á., & Telek, M. (2006). A moments based distribution bounding method. Math. Comput. Model., 43, 1367-1382. http://webspn.hit.bme.hu/~telek/cikkek/racz06a.pdf
* Tekel, J., & Cohen, L. (2012, May). Constructing and estimating probability distributions from moments. In Automatic target recognition XXII (Vol. 8391, pp. 114-123). SPIE. https://fks.sk/~juro/docs/paper_spie_2.pdf
* Mnatsakanov, R. M., & Hakobyan, A. S. (2009). Recovery of distributions via moments. In Optimality (pp. 252-265). Institute of Mathematical Statistics. https://projecteuclid.org/ebook/Download?urlid=10.1214%2F09-LNMS5715&isFullBook=False
* Devroye, L. (1986). An automatic method for generating random variates with a given characteristic function. SIAM journal on applied mathematics, 46(4), 698-719.
* Devroye, L. (1989). On random variate generation when only moments or Fourier coefficients are known. Mathematics and Computers in Simulation, 31(1-2), 71-89. http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.15.1349&rep=rep1&type=pdf
#### Empirical characteristic functions
* https://www.webdepot.umontreal.ca/Usagers/carrascm/MonDepotPublic/carrascm/Carrasco_Kotchoni_ET2017.pdf
* Carrasco, M., & Kotchoni, R. (2017). Efficient estimation using the characteristic function. Econometric Theory, 33(2), 479-526. https://www.webdepot.umontreal.ca/Usagers/carrascm/MonDepotPublic/carrascm/Carrasco_Kotchoni_ET2017.pdf
* u, J. (2004). Empirical characteristic function estimation and its applications. Econometric reviews, 23(2), 93-123. http://www.mysmu.edu/faculty/yujun/Research/YuER.pdf
