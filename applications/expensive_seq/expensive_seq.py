seq_dict = {}
def expensive_seq(x, y, z):
    a,b = expensive_internal(x,y,z)
    return a + b
    
def expensive_internal(x,y,z):
    try:
        (old_y,y_sum),(old_z,zsum) = seq_dict[x]
        new_y_sum = y_sum + 3*(y-old_y)
        new_z_sum = (z/old_z)*zsum
        return new_y_sum, new_z_sum
        
    except KeyError:
        if x <= 0:
            return y,z
        else:
            y_sum1, z_sum1 = expensive_internal(x-1,y+1,z) 
            y_sum2, z_sum2 = expensive_internal(x-2,y+2,2*z)
            y_sum3, z_sum3 = expensive_internal(x-3,y+3,3*z)
            y_tot = y_sum1 + y_sum2 + y_sum3
            z_tot = z_sum1 + z_sum2 + z_sum3
            seq_dict[x] = ((y,y_tot),(z,z_tot))
            return y_tot, z_tot

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
