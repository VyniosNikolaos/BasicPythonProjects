class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = None

    def set_value(self, value):
        self.value = value

class LoggingMeta(type):
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value):
                attrs[attr_name] = cls.log_method(attr_value)
        return super().__new__(cls, name, bases, attrs)

    @staticmethod
    def log_method(method):
        def wrapper(*args, **kwargs):
            print(f"Calling method: {method.__name__}")
            return method(*args, **kwargs)
        return wrapper

class MyClass(metaclass=LoggingMeta):
    def method1(self):
        print("This is method1")

    def method2(self):
        print("This is method2")

if __name__ == "__main__":
    # Testing Singleton
    s1 = Singleton()
    s2 = Singleton()
    print(f"Are s1 and s2 the same object? {s1 is s2}")

    s1.set_value(42)
    print(f"s1 value: {s1.value}")
    print(f"s2 value: {s2.value}")

    # Testing LoggingMeta
    obj = MyClass()
    obj.method1()
    obj.method2()

"""
This script demonstrates the use of metaclasses in Python:
1. Implementing a Singleton pattern using a metaclass
2. Creating a logging metaclass that adds logging to all methods of a class

Key points:
- Metaclasses are classes for classes
- They can be used to modify class creation behavior
- The metaclass attribute specifies the metaclass to use when creating a class

Applications:
1. Implementing design patterns (e.g., Singleton)
2. Adding functionality to classes automatically
3. Modifying class creation behavior
4. Creating domain-specific languages
5. Implementing abstract base classes
"""