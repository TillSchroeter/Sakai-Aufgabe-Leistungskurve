
import numpy as np
import matplotlib.pyplot as plt
from sort import bubble_sort
from load_data import load_data

#ausprobieren
'''time = [1,2,3,4,5,6,7,8,9,10]
data = [10,9,8,7,6,5,4,3,2,1]
plt.plot(time, data)
plt.show
plt.savefig('plot.png')
print (load_data.Power_W_sorted)'''

if __name__ == "__main__":
    data = load_data('activity.csv')
    power_W = data['PowerOriginal']
    print(power_W)
    sorted_power_W = bubble_sort(power_W)
    print(sorted_power_W[::-1])


print (len(sorted_power_W))
# Gesamtanzahl der Zahlen im Array
num_points = 1804
# Dauer der Zeit in Sekunden (30 Minuten und 5 Sekunden)
total_seconds = 30 * 60 + 5
# Gleichmäßig verteilte Zeitpunkte generieren
time_points = np.linspace(0, total_seconds, num_points)
print (len(time_points))

plt.plot (time_points,sorted_power_W[::-1])
plt.xlabel('Zeit [sekunden]')
plt.ylabel('Leistung [Watt]')
plt.title('Leistungskurve')
plt.savefig('Leistungskurve.png')

print ('funktioniert')