import matplotlib.pyplot as plt
import numpy as np

x_data = np.array([ 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])
y_data = np.array([12, 17, 19, 21, 31, 34, 45, 56, 65, 79, 97, 128, 158, 225, 266])

log_y_data = np.log(y_data)

curve_fit = np.polyfit(x_data, log_y_data, 1)
#print(curve_fit)
#print(curve_fit[0])
#print(curve_fit[1])

#y = curve_fit[0]*x_data + curve_fit[1]
#plt.plot(x_data, log_y_data, "o")
#plt.plot(x_data, y)

z=np.exp(curve_fit[1])
b=curve_fit[0]
print(z)
print(b)

y =z*np.exp(b*x_data)

plt.plot(x_data, y_data, "o")
plt.legend(['Dato del Ministerio de Salud'])
plt.plot(x_data, y, "--")

plt.savefig('covid.png')

h = z * np.exp(b * 23)
print(h)
