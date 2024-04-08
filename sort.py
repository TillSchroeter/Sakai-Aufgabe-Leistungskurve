
def bubble_sort(power_W):
   
    n = len(power_W)
    for i in range(n):
        # Letzte i Elemente sind bereits sortiert, daher können wir sie überspringen
        for j in range(0, n-i-1):
            if power_W[j] > power_W[j+1]:
                # Tausche die Elemente, wenn sie in der falschen Reihenfolge sind
                power_W[j], power_W[j+1] = power_W[j+1], power_W[j]
    return power_W


