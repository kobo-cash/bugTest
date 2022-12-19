class MyClass:
    def instance_method():  # Noncompliant. "self" parameter is missing.
        print("instance_method")

    @classmethod
    def class_method():  # Noncompliant. "cls" parameter is missing.
        print("class_method")