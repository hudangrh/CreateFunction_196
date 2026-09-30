#Soal 1
def convert_temperature(temperatureValue, TemperatureUnit):
    if TemperatureUnit == "C":
        return (temperatureValue * 9/5) + 32
    elif TemperatureUnit == "F":
        return (temperatureValue - 32) * 5/9
    else:
        return "'C' atau 'F'"
temperatureValue = float(input("Masukkan nilai suhu: "))
temperatureUnit = input("Masukkan satuan suhu (C/F): ")
hasil = convert_temperature(temperatureValue, temperatureUnit)
print(hasil)

#Soal 2
import math
suhu = lambda r: round(math.pi * r**2, 2)
r = float(input("Masukkan jari-jari lingkaran: "))
print(suhu(r))


