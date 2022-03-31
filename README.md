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


## Features


## TODO

### rv.py
* [ ] Implement RV.cdf() RV.pdf(), RV.rvs(). I am aware of four general approaches:
        - Direct inversion of the characteristic function e.g., (Sheppard 1991).
          While this appears to be the most straight forward, the reliance on
          integration is problematic if we can only use the first n terms of the
          characteristic function.  Even if n is very large, we can't integrate
          over the whole range, or even over most of it. Note, there are also
          techniques out there for going straight to the quantile function from
          the characteristic function (Shaw and McCabe 2009) 
        - Use moments to generate the approximants. This, so far, appears to be
          the most likely approach. The general technique is to use optimisation
          (usually linear least squares) to fit a sum of polynomials, potentially
          combined in some way with a base distribution, to the desired PDF by
          matching the moments. Some regularisation is needed to make the output
          a bona fide distribution, then quadrature integration is used to
          get the CDF, then the quantile function is generated, and random samples
          can be generated.
        - The third approach, which I haven't found any literature on, would be
          to find the coefficients of the series expansion CDF or PDF in terms
          of the moments, or of the coefficients of the series expansion of the
          characteristic function. If this is possible, and if it avoids the
          numerical numerical stability problems mentioned in option 1, then I 
          think this is the best approach, but I don't know how to do it yet.
        - Finally, there is Devroye's work on generating random samples from
          just the moments. 

* [ ] Implement __mul__, __pow__, __div__, etc
    - At this stage I'm not sure what is possible. Maybe it is only realistic to support linear / affine functions of RVs.
    - The paper by I.J Good "The characteristic function of functions" looks promising. It seems to offer a general method for calculating CF of g(X) where the CF of X is known, and seems to have results for "powers, logarithms, exponentials, quadratic forms, and sets of quadratic forms". 

* [ ] Add explicit support for discrete distributions
    - Most of the code already works for discrete distributions. It is only when I have implemented .cdf, .pdf and .rvs that I will need to have some explicit code for dealing with the discretisation.

* [ ] Inference.
    - This will require having power series with symbols. The naive approach would be to do something like maximum likelihood estimation, but there appears to be other approaches in the literature based around the empirical characteristic function.
    - As of 2022-03-29, I have implemented a basic symbolic computer algebra system, and modified the powerseries implementation so that the coefficient functions have be Expression valued. Not yet confirmed to be working for all functionality, but it is a promising start.
    - I could probably use a generic optimiser along with the method of moments


* [ ] Prior distributions for model parameters
    - I currently have no idea how to do this. Probably possible, but I don't know how yet. Would they need to be conjugate? Probably not?

* [ ] Multivariate constructions (joint, marginal, conditional)

* [ ] Conversion of MGFs or probability generating functions?
    - Maybe not all that useful. This is not a priority.

* [ ] Methods like .mean() and .var() should probably just return the Real component.


### powerseries.py
* [x] Tests
* [x] Confirm PowerSeries works for complex coefficients
* [x] Integration of symbolic expressions
* [ ] Probably rename to Generating Function, or maybe OrdinaryGeneratingFunction
* [ ] Explore multivariate systems
* [ ] Look into techniques to improve numerical stability.
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

### Characteristic functions

#### Algebraic manipulation
* Good, I. J. (1968). The characeristic functions of functions. https://www.jstor.org/stable/2416209

#### Inversion
* Shephard, N. G. (1991). From characteristic function to distribution function: A simple framework. Econometric Theory, vol 7. 519-229. https://scholar.harvard.edu/files/ET91.pdf
* Witkovský, V. (2016). Numerical inversion of a characteristic function: An alternative tool to form the probability distribution of output quantity in linear measurement models. Acta IMEKO, 5(3), 32-44. https://www.researchgate.net/profile/Viktor-Witkovsky/publication/309713869_Numerical_inversion_of_a_characteristic_function_An_alternative_tool_to_form_the_probability_distribution_of_output_quantity_in_linear_Measurement_models/links/58230e5b08aeb45b58891df6/Numerical-inversion-of-a-characteristic-function-An-alternative-tool-to-form-the-probability-distribution-of-output-quantity-in-linear-Measurement-models.pdf
* https://www.tandfonline.com/doi/abs/10.1080/00031305.1995.10476180
* Shaw, W. T., & McCabe, J. (2009). Monte Carlo sampling given a characteristic function: quantile mechanics in momentum space. arXiv preprint arXiv:0903.1592. https://arxiv.org/pdf/0903.1592.pdf


#### Moment based density estimation

* https://www.researchgate.net/profile/Serge-Provost/publication/242782657_Moment-Based_Density_Approximants/links/5418b2510cf203f155adb50f/Moment-Based-Density-Approximants.pdf
* Zang, Y. (2019). Advances in Moment-Based Distributional Methodologies. https://ir.lib.uwo.ca/cgi/viewcontent.cgi?article=8671&context=etd
* Rácz, S., Tari, Á., & Telek, M. (2006). A moments based distribution bounding method. Math. Comput. Model., 43, 1367-1382. http://webspn.hit.bme.hu/~telek/cikkek/racz06a.pdf
* Tekel, J., & Cohen, L. (2012, May). Constructing and estimating probability distributions from moments. In Automatic target recognition XXII (Vol. 8391, pp. 114-123). SPIE. https://fks.sk/~juro/docs/paper_spie_2.pdf
* Mnatsakanov, R. M., & Hakobyan, A. S. (2009). Recovery of distributions via moments. In Optimality (pp. 252-265). Institute of Mathematical Statistics. https://projecteuclid.org/ebook/Download?urlid=10.1214%2F09-LNMS5715&isFullBook=False

#### Sampling methods
* Devroye, L. (1986). An automatic method for generating random variates with a given characteristic function. SIAM journal on applied mathematics, 46(4), 698-719.
* Devroye, L. (1989). On random variate generation when only moments or Fourier coefficients are known. Mathematics and Computers in Simulation, 31(1-2), 71-89. http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.15.1349&rep=rep1&type=pdf
#### Empirical characteristic functions
* https://www.webdepot.umontreal.ca/Usagers/carrascm/MonDepotPublic/carrascm/Carrasco_Kotchoni_ET2017.pdf
* Carrasco, M., & Kotchoni, R. (2017). Efficient estimation using the characteristic function. Econometric Theory, 33(2), 479-526. https://www.webdepot.umontreal.ca/Usagers/carrascm/MonDepotPublic/carrascm/Carrasco_Kotchoni_ET2017.pdf
* u, J. (2004). Empirical characteristic function estimation and its applications. Econometric reviews, 23(2), 93-123. http://www.mysmu.edu/faculty/yujun/Research/YuER.pdf
