# Author: Vincent McIntosh
# Date: 9/30/20
# Description: Creates person objects and provides the mean, median and mode of their ages.

from statistics import mean, median, mode

class Person:

    def __init__(self, name, age):
        """Creates a person with name and age"""
        self._name = name
        self._age = age

    def get_age(self):
        """Returns the person's age"""
        return self._age

def basic_stats(list):
    """Creates a tuple showing the mean, median, and mode of the ages of the people listed"""
    ages = []
    for human in list:
        age = Person.get_age(human)
        ages.append(age)

    return (mean(ages), median(ages), mode(ages))







#p1 = Person("Kyoungmin", 73)
#p2 = Person("Mercedes", 24)
#p3 = Person("Avanika", 48)
#p4 = Person("Marta", 24)

#person_list = [p1, p2, p3, p4]
#print(basic_stats(person_list))  # should print a tuple of three values
