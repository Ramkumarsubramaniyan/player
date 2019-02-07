def itr(num):
        if(num == 1): return "I"
        if(num == 4): return "IV"
        if(num == 5): return "V"
        if(num == 9):  return "IX"
        if(num == 10): return "X"
        if(num == 40): return "XL"
        if(num == 50): return "L"
        if(num == 90): return "XC"
        if(num == 100): return "C"
        if(num == 400): return "CD"
        if(num == 500): return "D"        
        if(num == 900): return "CM"
        if(num == 1000): return "M"        

        for h in [1000, 100, 10, 1]:            
            for c in [9*h, 5*h, 4*h, h]:
                if(num>=c):
                    return itr(c) + itr(num-c) 
