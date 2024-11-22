#LATIHAN


print(" KALKULATOR SUHU ")
print('1. Celcius')
print('2. Reamur')
print('3. Fahrenheit')
print('4. Kelvin')

suhu = int(input('suhu awal : '))
if suhu == 1:
    celcius = float(input('Masukkan suhu dalam Celcius : '))
    reamur = (celcius * 4) / 5
    fahrenheit = ((celcius * 9) / 5) + 32
    kelvin = celcius + 273.15

    print(f"suhu reamur adalah {reamur:.2f} Reamur")
    print(f"suhu fahrenheit adalah {fahrenheit:.2f} Fahrenheit")
    print(f"suhu kelvin adalah {kelvin:.2f} Kelvin")

elif suhu == 2:
    reamur = float(input('Masukkan suhu dalam Reamur : '))
    celcius = (5 / 4) * reamur
    fahrenheit = (9 / 4) * reamur + 32
    kelvin = celcius + 273.15

    print(f"suhu celcius adalah {celcius:.2f} Celcius")
    print(f"suhu fahrenheit adalah {fahrenheit:.2f} Fahrenheit")
    print(f"suhu kelvin adalah {kelvin:.2f} Kelvin")

elif suhu == 3:
    fahrenheit = float(input('Masukkan suhu dalam Fahrenheit : '))
    celcius = ((fahrenheit - 32) * 5) / 9
    reamur = ((fahrenheit - 32) * 4) / 9
    kelvin = celcius + 273.15

    print(f"suhu celcius adalah {celcius:.2f} Celcius")
    print(f"suhu Reamur adalah {reamur:.2f} Reamur")
    print(f"suhu kelvin adalah {kelvin:.2f} Kelvin")

elif suhu == 4:
    kelvin = float(input('Masukkan suhu dalam Kelvin : '))
    celcius = kelvin - 273.15
    reamur = (celcius * 4) / 5
    fahrenheit = (9 / 5) * celcius + 32

    print(f"suhu celcius adalah {celcius:.2f} Celcius")
    print(f"suhu Reamur adalah {reamur:.2f} Reamur")
    print(f"suhu fahrenheit adalah {fahrenheit:.2f} Fahrenheit")

else:
    print('TOLONG MASUKKAN SESUAI PILIHAN DIATAS !')
