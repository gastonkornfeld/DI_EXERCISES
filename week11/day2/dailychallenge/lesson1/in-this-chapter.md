


# Args And **Kwargs
## Table Of Contents

* What are the point of asterisk ?
    * Feedback

---

### Args And **Kwargs
## What Are The Point Of Asterisk ?

`Python has a special syntax, * (unpacking operator) and * (unpacking operator), that lets you pass a variable number of arguments to a function.
By convention, these are written as args and *kwargs, but only the asterisks are important; you could equally write vars and **vars to achieve the same result.
`

1. *Args

`\*args is useful when we don’t know in advance how many arguments we need to pass in a function.
`
```Python
def check_arguments(*args):
    print(f"These are the arguments {args}")
check_arguments(1, 2, 'hey')
>> These are the arguments (1, 2, 'hey') // You get a tuple
```
`
*args: is a tuple of args.
`
```Python
def check_tuple(a,b):
    # Returns the sum of 'a' and 'b'
    return sum((a,b))

print(check_tuple(10,30))

>> 40
```
```Python
# Multiple *args
def check_multiple_arguments(*args):
    return sum(args)

print(check_multiple_arguments(10,20,100,30))

>> 160
```

2. \**Kwargs

`
**kwargs is useful when we don’t know in advance how many keyworded arguments we need to pass in a function.
`
`
**kwargs: is a dictionary of args (keywords).
`
```Python
def  check_keywordedarguments(**kwargs):
    print(kwargs)
check_keywordedarguments(name="Sarah", age=24)
>> {'name': 'Sarah', 'age': 24} // You get a dictionary
```
```Python 
def check_keywordedarguments(**kwargs):
    for key, value in kwargs.items():
        print(key,":",value)
check_keywordedarguments(name="Sarah", age=24)
>> 
name : Sarah
age : 24
```
```Python
def check_keywordedarguments(**kwargs):
    return kwargs

print(check_keywordedarguments(fruit='apple', ordered= 2))

>> {'fruit': 'apple', ordered: 2}
```

3. \*Args And **Kwargs Together
`
Often args and *kwargs are used together in a function where we have at least one required argument.
`
`
In these cases, order matters.*args and **kwargs are placed after any required arguments.
`
```Python
def check_arguments_keywordedarguments (required_arg, *args, **kwargs):
    print(required_arg)
    if args:
        print(args)
    if kwargs:
        print(kwargs)
check_arguments_keywordedarguments("required argument")
check_arguments_keywordedarguments("required argument", 1, 2, 'hey')
check_arguments_keywordedarguments("required argument", 1, 2, 'hey', name="Sarah", age=24)
```
`
You have to preserve the order !
`
```Python
def check_arguments_keywordedarguments(*args,**kwargs):
    print('*args', args)
    print('**kwargs', kwargs)

check_arguments_keywordedarguments(10,20,30,name='John',surname='Doe')

>>
*args (10, 20, 30)
**kwargs {'name': 'John', 'surname': 'Doe'}

check_arguments_keywordedarguments(10,20,30,name='John',surname='Doe', 2)

>> SyntaxError: positional argument follows keyword argument
```

`
When we declare a starred parameter such as *param, then all the positional arguments from that point till the end are collected as a tuple called param.
`
`
When we declare a double-starred parameter such as **param, then all the keyword arguments from that point till the end are collected as a dictionary called param.
`
```Python
def check(a, *numbers, **person):
    print('Greetings : ', a)

    #iterate through all the items in tuple
    for num in numbers:
        print('num - ', num)

    #iterate through all the items in dictionary    
    for key, value in person.items():
        print(key + ': ' + value)

check("hello", 1,2,3,name="John",surname="Doe")

>> Greetings :  hello
num -  1
num -  2
num -  3
name: John
surname: Doe
```

---


## Feedback

`
Tell us what you thought about the chapter
`   

