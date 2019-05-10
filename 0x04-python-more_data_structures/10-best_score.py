#!/usr/bin/python3
def best_score(a_dictionary):
        max_val = None
        max_key = None

        for k, v in dict.items():
                if max_val is None or max_val < v:
                        max_val = v
                        max_key = k
                return max_key
