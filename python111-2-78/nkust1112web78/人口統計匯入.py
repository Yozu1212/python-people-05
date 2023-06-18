import csv
import os
import django
import requests
y=63
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nkust1112web78.settings')
django.setup()
from mysite import models
models.cpdata.objects.all().delete()
y_data=str(y)+".csv"

for i in range(63, 112):

    filename = y_data
    with open(filename, encoding='utf-8') as fp:
        All = [*csv.DictReader(fp)]

    I1 = 1
    N1 = 7
    N2 = 6
    N3 = 8
    for item1 in All:
        #print(item1)

        I1 = I1+1
        if I1 == N1 :
            N1 = N1+3
            Place2 = item1["\ufeff區  域  別 "]
            Gender2 = item1[" 性別 "]
            Number2 = item1[" 總     計 "]
            I2 = 1
            I3 = 1
            for item2 in All:
                I2 = I2+1
                if  I2 == N2:
                    N2 = N2+3
                    Place1 = Place2
                    Gender1 = item2[" 性別 "]
                    Number1 = item2[" 總     計 "]
                    break
            for item3 in All:
                I3 = I3+1
                if I3 == N3:
                    N3 = N3+3
                    Place3 = Place2
                    Gender3 = item3[" 性別 "]
                    Number3 = item3[" 總     計 "]
                    break

            new_rec = models.cpdata(
                year = y,
                title = str(y) + Place2 + Gender1,
                place = Place1,
                gender = Gender1,
                number = Number1)
            new_rec.save()
            new_rec = models.cpdata(
                year = y,
                title = str(y) + Place2 + Gender2,
                place = Place2,
                gender = Gender2,
                number = Number2)
            new_rec.save()
            new_rec = models.cpdata(
                year = y,
                title = str(y) + Place2 + Gender3,
                place = Place3,
                gender = Gender3,
                number = Number3)
            new_rec.save()
    y=y+1
print("Done!")
