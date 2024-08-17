from collections import Counter
from math import gcd
from functools import reduce

def hasGroupsSizeX(deck):
  
    count = Counter(deck)
    

    def find_gcd_of_list(lst):
        return reduce(gcd, lst)

    values = list(count.values())
    overall_gcd = find_gcd_of_list(values)
    

    return overall_gcd > 1


print(hasGroupsSizeX([1,2,3,4,4,3,2,1]))  
print(hasGroupsSizeX([1,1,1,2,2,2,3,3]))  
