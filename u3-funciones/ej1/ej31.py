import math

def calcula_area_triangulo(b,a):
    try:
        if b<0 or a<0:
            return None
        else:
            area = (b*a)/2
            if math.isnan(area):
                return math.nan
            else:
                return area
        
    except TypeError:
        return None

print(4,-3)