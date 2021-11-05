import os
from typing import Type

os.system("cls")

def esBisiesto (year: int=0) -> bool:
    try:
        if year>=0:
            if year%4==0 and year%100!=0 or year%400==0:
                return True
            else:
                return False
    
        return None
    except TypeError:
        return None

