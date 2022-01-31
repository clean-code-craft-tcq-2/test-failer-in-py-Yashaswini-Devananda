
def size(cms):
    if cms <= 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'

for x in range (50):
    if x <= 38:
        assert(size(x) == 'S')
    elif  38 < x < 42:
        assert(size(x) == 'M')
    else:
        assert(size(x) == 'L')
        
print("All is well (maybe!)\n")
