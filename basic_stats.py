# Author: Rebecca Starr
# Date: 1/5/2020
# Description: Creates a class called "Person" with name and age as attributes.
# Then the function "basic_stats" takes a list of people and returns a tuple of
# the mean, median, and mode of the ages of the people in the list.


from statistics import mean, median, mode


class Person:
    """Represents a person.
     attributes: name, age"""

    def __init__(self, name, age):
        """Creates a bank account object with an account ID and balance."""
        self.name = name
        self.age = age


def basic_stats(person_list):
    # Takes in a list of people and returns a tuple of the mean, median, and mode
    # of their ages

    age_list = []
    for pers in person_list:
        age_list.append(pers.age)

    age_mean = mean(age_list)
    age_median = median(age_list)
    age_mode = mode(age_list)

    return age_mean, age_median, age_mode

