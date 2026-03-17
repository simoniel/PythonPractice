'''
scrip to test python feature, tips and tricks. each function a fidderent one. 
'''
import datetime
import re
import numpy as np

#try this exercise: https://www.youtube.com/watch?v=FjVSnnFEVs4
# https://www.youtube.com/watch?v=iaZQF8SLHJs
    

def practice_regex():
    txt = "The rain in Spain"
    x = re.search("[a-zA-Z0-9]", txt)
    print (x)

def practice_date():
    x = datetime.datetime.now()
    print(x) 
    print(x.strftime("%B")) 
    print(x.strftime("%A%B%Y")) 

def tot_sum(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s   

def car_info(**specs):
    print("All data: ", specs)

def multiplier(n):
  return lambda a : a * n
    
def func_practice():
    s1 = tot_sum(1,2,3)
    print("s1 = ", s1)
    s2 = tot_sum(3,5,8,9,10)
    print("s2 = ", s2)
    s3 = tot_sum()
    print("s3 = ", s3)

    numbers = [1,2]
    s4 = tot_sum(*numbers)
    print("s4 = ", s4)

    car_info(brand = "Fiat", model = "L", year=2020, color="blue")
    c2 = {
        'brand': 'xx',
        'model': 'x',
        'year': 2000,
        'color': 'red'
    }
    car_info(**c2)

    cars = {'c1' : dict(brand = "Fiat", model = "L", year=2020, color="blue"), 'c2' : c2}
    print(cars)


    doubler = multiplier(2)
    tripler = multiplier(3)

    print(doubler(11))
    print(tripler(11))

    # map() function applies a function to every item in an iterable

    numbers = [1, 2, 3, 4, 5]
    doubled = list(map(lambda x: x * 2, numbers))
    print(doubled)

    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
    print(odd_numbers)

    #Sort strings by length:
    words = ["apple", "pie", "banana", "cherry"]
    sorted_words = sorted(words, key=lambda x: len(x))
    print(sorted_words)

    print(sorted(cars.values(), key=lambda x: x["year"]))


def dict_practice():
    d = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    d["year"]=2026
    d["color"]="red"

    print("dict length = ", len(d))
    print("year = ", d["year"])
    print("-- keys = ", d.keys())
    print("-- values = ", d.values())
    print("-- items = ", d.items())

    for k,v in d.items():
        print("key = ", k)
        print("value = ", v)

    d2 = {
        "brand": "Fiat",
        "model": "L",
        "year": 2018,
        "color": "blue"
    }
    cars = {'c1' : d, 'c2' : d2}
    print(cars)
    
    template_car = ("brand", "model", "year", "color")
    y = 0
    d3 = dict.fromkeys(template_car, y)
    print(d3)

    cars['c3'] = d3


    for car, specs in cars.items():
        print(car, specs["color"])

def np_array_slice():

    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    '''
    slice function: [ (range)index ndim(rows), (range)index columns, step ]
    here specifically, for element 0 and 1 select 3rth element
    '''
    print(arr[0:2, 2]) #or print(arr[:, 2]) 



def revert_string():
    '''
    slice function: [ (range)index ndim(rows), (range)index columns, step ]
    so [::-1] means all array from start to end with step -1 
    '''

    s1 = 'test'
    print("original string = ", s1)
    print("reverted string = ", s1[::-1])


def find_prefix():
    '''
    find maximum common prefix for a list of strings
    '''

    strs = ["ciao", "cloud", "chips"]

    prefix=""  

    print("strs = ", strs)
    z = zip(*strs)
    print("zip(*strs) = ", list(z))

    for group in zip(*strs):
        print(group)
        c_set = set(group)
        if len(c_set)==1:
            prefix += group[0]
        else:
            break

    print("prefix = ", prefix)

def test():
    x = "Hello World"
    print(type(x))  


if __name__ == '__main__': 
    #np_array_slice()
    #revert_string()
    #find_prefix()
    #dict_practice()
    #func_practice()
    #practice_date()
    practice_regex()
    #test()
