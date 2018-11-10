import sunflower_ll

print('Importing:  ', sunflower_ll.name)


import sunflower_ll.translator as translator
t = translator.Translator()

print(t.magnetometer_data())

t.set_magnetometer_data('mag_1', 10)

t.magnetometer_data()


