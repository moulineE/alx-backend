```markdown
# 0x01. Caching

## Back-end Project

**By: Guillaume, CTO at Holberton School**

**Weight: 1**

Project duration: Jan 30, 2024, 4:00 AM - Feb 1, 2024, 4:00 AM

Checker release: Jan 30, 2024, 4:00 PM

Auto review will be launched at the deadline

## Background Context

In this project, you will learn about different caching algorithms.

## Resources

Read or watch:

- [Cache replacement policies - FIFO](#)
- [Cache replacement policies - LIFO](#)
- [Cache replacement policies - LRU](#)
- [Cache replacement policies - MRU](#)
- [Cache replacement policies - LFU](#)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- What the purpose of a caching system is
- What limits a caching system has

## Requirements

### Python Scripts

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)

## More Info

### Parent class `BaseCaching`

All your classes must inherit from `BaseCaching` defined below:

```python
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data is stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

## Tasks

### 0. Basic dictionary (mandatory)

Create a class `BasicCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- This caching system doesn’t have a limit

```python
def put(self, key, item):
    """ Add an item in the cache
    """
    # Must assign to the dictionary self.cache_data the item value for the key key.
    # If key or item is None, this method should not do anything.

def get(self, key):
    """ Get an item by key
    """
    # Must return the value in self.cache_data linked to key.
    # If key is None or if the key doesn’t exist in self.cache_data, return None.
```

#### Example

```python
BasicCache = __import__('0-basic_cache').BasicCache

my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
```

### 1. FIFO caching (mandatory)

Create a class `FIFOCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- The `put` method:
    - Must assign to the dictionary `self.cache_data` the item value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
        - You must discard the first item put in cache (FIFO algorithm)
        - You must print `DISCARD:` with the key discarded and following by a new line
- The `get` method:
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

#### Example

```python
FIFOCache = __import__('1-fifo

_cache').FIFOCache

my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
```

### 2. LIFO Caching (mandatory)

Create a class `LIFOCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- The `put` method:
    - Must assign to the dictionary `self.cache_data` the item value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
        - You must discard the last item put in cache (LIFO algorithm)
        - You must print `DISCARD:` with the key discarded and following by a new line
- The `get` method:
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

#### Example

```python
LIFOCache = __import__('2-lifo_cache').LIFOCache

my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
```

### 3. LRU Caching (mandatory)

Create a class `LRUCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- The `put` method:
    - Must assign to the dictionary `self.cache_data` the item value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
        - You must discard the least recently used item (LRU algorithm)
        - You must print `DISCARD:` with the key discarded and following by a new line
- The `get` method:
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

#### Example

```python
LRUCache = __import__('3-lru_cache').LRUCache

my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
```

### 4. MRU Caching (mandatory)

Create a class `MRUCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- The `put` method:
    - Must assign to the dictionary `self.cache_data` the item value for the key `key`.
    - If `key` or `item` is `None`, this method should not do anything.
    - If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`:
        - You must discard the most recently used item (MRU algorithm)
        - You must print `DISCARD:` with the key discarded and following by a new line
- The `get` method:
    - Must return the value in `self.cache_data` linked to `key`.
    - If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

#### Example

```python
MRUCache = __import__('4-mru_cache').MRUCache

my_cache = MRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
```
