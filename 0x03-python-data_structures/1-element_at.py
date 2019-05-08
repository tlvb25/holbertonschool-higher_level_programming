#!/usr/bin/python3
def element_at(my_list, idx):
        if idx < 0:
                return (None)
        elif idx > len(my_list):
                return (None)
        else:
                res_list = [my_list[i] for i in idx]
                return(res_list)
