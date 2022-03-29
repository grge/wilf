from abc import ABC, abstractmethod
from dataclasses import dataclass
from numbers import Number
from typing import Dict, Tuple

from wilf.utils import product

class SymbolicExpression(ABC):
    def __mul__(self, other : 'Expression') -> 'Expression':
        return Product(self, other).simplify()

    def __rmul__(self, other : 'Expression') -> 'Expression':
        return Product(other, self).simplify()

    def __add__(self, other : 'Expression') -> 'Expression':
        return Sum(self, other).simplify()

    def __radd__(self, other : 'Expression') -> 'Expression':
        return Sum(other, self).simplify()
    
    def __sub__(self, other : 'Expression') -> 'Expression':
        return Sum(self, -other).simplify()
    
    def __pow__(self, other : 'Expression') -> 'Expression':
        return Power(self, other).simplify()

    def __neg__(self) -> 'Expression':
        return Product(-1, self).simplify()

    def __truediv__(self, other : 'Expression') -> 'Expression':
        return Fraction(self, other).simplify()

    def __rtruediv__(self, other : 'Expression') -> 'Expression':
        return Fraction(other, self).simplify()


    @abstractmethod
    def simplify(self):
        ...

    def subs(self, subs: 'Dict[Symbol, Expression]', simplify: bool = True) -> 'Expression':
        new_dict = {}
        for k, v in self.__dict__.items():
            if isinstance(v, tuple):
                new_dict[k] = (subs_expr(v, subs, simplify=simplify) for v in v)
            else:
                new_dict[k] = subs_expr(v, subs, simplify=simplify)
        new_expr = self.__class__(**new_dict)
        if simplify:
            return simplify_expr(new_expr)
        else:
            return new_expr
    
Expression = SymbolicExpression | Number

def subs_expr(expr:'Expression', subs: 'Dict[Symbol, Expression]', simplify: bool = True) -> 'Expression':
    if expr in subs:
        return subs[expr]

    match expr:
        case SymbolicExpression():
            return expr.subs(subs, simplify=simplify)
        case Number():
            return expr

def simplify_expr(expr: 'Expression') -> 'Expression':
    match expr:
        case SymbolicExpression():
            return expr.simplify()
        case Number():
            return expr

@dataclass(frozen=True)
class Symbol(SymbolicExpression):
    name: str

    def __repr__(self):
        return self.name

    def simplify(self):
        return self

    def subs(self, subs: 'Dict[Symbol, Expression]', simplify : bool = True) -> 'Expression':
        out = subs.get(self, self)
        if simplify:
            return simplify_expr(out) 
        else:
            return out

@dataclass(init=False)
class Sum(SymbolicExpression):
    terms : Tuple[Expression]

    def __init__(self, *args : Tuple[Expression], terms : Tuple[Expression] = None):
        if args and terms:
            raise ValueError("Cannot pass both args and terms")
        if terms:
            args = terms
        self.terms = tuple()
        for t in args:
            if isinstance(t, Sum):
                self.terms += t.terms
            else:
                self.terms += (t,)

    def __hash__(self):
        return hash(self.terms)

    def __str__(self):
        return " + ".join(map(str, self.terms))

    def simplify(self):
        terms_s = [simplify_expr(t) for t in self.terms]

        numeric_term = sum([t for t in terms_s if isinstance(t, Number)])
        non_numeric_terms = [t for t in terms_s if not isinstance(t, Number)]

        if numeric_term == 0:
            if len(non_numeric_terms) == 0:
                return 0
            if len(non_numeric_terms) == 1:
                return non_numeric_terms[0]
            else:
                return Sum(*non_numeric_terms)
        else:
            if len(non_numeric_terms) == 0:
                return numeric_term
            else:
                return Sum(numeric_term, *non_numeric_terms)

@dataclass(init=False)
class Product(SymbolicExpression):
    terms : Tuple[Expression]

    def __init__(self, *args : Tuple[Expression], terms : Tuple[Expression] = None):
        if args and terms:
            raise ValueError("Cannot specify both args and terms")
        if terms:
            args = terms
        self.terms = tuple()
        for t in args:
            if isinstance(t, Product):
                self.terms += t.terms
            else:
                self.terms += (t,)

    def __hash__(self):
        return hash(self.terms)

    def __str__(self):
        return " * ".join(map(str, self.terms))

    def simplify(self):
        terms_s = [simplify_expr(t) for t in self.terms]

        numeric_term = product([t for t in terms_s if isinstance(t, Number)])
        non_numeric_terms = [t for t in terms_s if not isinstance(t, Number)]

        if numeric_term == 0:
            return 0
        elif numeric_term == 1:
            if len(non_numeric_terms) == 0:
                return 1
            if len(non_numeric_terms) == 1:
                return non_numeric_terms[0]
            else:
                return Product(*non_numeric_terms)
        else:
            if len(non_numeric_terms) == 0:
                return numeric_term
            else:
                return Product(numeric_term, *non_numeric_terms)

@dataclass(frozen=True)
class Power(SymbolicExpression):
    base : Expression
    exponent : Expression

    def __repr__(self):
        return f'{self.base}^{self.exponent}'

    def simplify(self):
        base_s = simplify_expr(self.base)
        exponent_s = simplify_expr(self.exponent)
        if isinstance(base_s, Number) and isinstance(exponent_s, Number):
            return base_s ** exponent_s
        elif isinstance(base_s, Number):
            if base_s == 0:
                return 0
            if base_s == 1:
                return 1
            else:
                return Power(base_s, exponent_s)
        elif isinstance(exponent_s, Number):
            if exponent_s == 0:
                return 1
            elif exponent_s == 1:
                return base_s
            else:
                return Power(base_s, exponent_s)
        else:
            return Power(base_s, exponent_s)

@dataclass(frozen=True)
class Fraction(SymbolicExpression):
    numerator : Expression
    denominator : Expression

    def __repr__(self):
        return f'{self.numerator}/{self.denominator}'

    def simplify(self):
        numerator_s = simplify_expr(self.numerator)
        denominator_s = simplify_expr(self.denominator)
        if isinstance(denominator_s, Number) and denominator_s == 0:
            return float('inf')
        elif isinstance(numerator_s, Number) and isinstance(denominator_s, Number):
            return numerator_s / denominator_s
        elif isinstance(numerator_s, Number) and numerator_s == 0:
            return 0
        elif isinstance(denominator_s, Number) and denominator_s == 1:
            return numerator_s
        else:
            return Fraction(numerator_s, denominator_s)