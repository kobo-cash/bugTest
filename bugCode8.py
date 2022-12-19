class A:
    pass

dict(**A())  # Noncompliant
{'a': 10, 'b': 20, **A()}  # Noncompliant