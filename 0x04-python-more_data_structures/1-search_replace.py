#!/usr/bin/python3
def search_replace(my_list, search, replace):
        new_list = []

        for _, v in enumerate(my_list):
                # using enumerate function and list comprehension
                new_list.append(replace if v == search else v)

        return (new_list)
