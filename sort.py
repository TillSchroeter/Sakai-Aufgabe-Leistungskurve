
def bubble_sort(power_W):
   
    n = len(power_W)
    for i in range(n):
        
        for j in range(0, n-i-1):
            if power_W[j] > power_W[j+1]:
                power_W[j], power_W[j+1] = power_W[j+1], power_W[j]
    
    return power_W


