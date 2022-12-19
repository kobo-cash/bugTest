# In python 3 the following fails
# In python 2.7.16 on MacOs, "open" will just ignore the "w" flag
with open("test.txt", "aw") as f:  # Noncompliant
    pass