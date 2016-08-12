'''this file iterates through each row of xlsx file,
    and stores its values in database'''

import os
from xlrd import open_workbook
from .models import Area, Company, Delivery


def open_excel():
    col = 0   # taking col so that if in futire we have to add mode company we can easily add
    wb = open_workbook(os.getcwd() + '/Pincode _list.xlsx')
    for s in wb.sheets():

        for row in range(1, s.nrows):
            print s.cell(row, col).value, s.cell(row, col+1).value
            pincode = int(s.cell(row, col).value)
            delhivery = s.cell(row, col+1).value
            delhivery_limit = s.cell(row, col+2).value
            fedex = s.cell(row, col+3).value
            fedex_limit = s.cell(row, col+4).value
            dotzot = s.cell(row, col+5).value
            dotzot_limit = s.cell(row, col+6).value
            dtdc = s.cell(row, col+7).value
            indiapost = s.cell(row, col+8).value
            pref1 = s.cell(row, col+9).value
            pref2 = s.cell(row, col+10).value
            pref3 = s.cell(row, col+11).value
            pref4 = s.cell(row, col+12).value
            pref5 = s.cell(row, col+13).value

            pin = Area.objects.get_or_create(pincode=pincode)

            if delhivery == 'Y':
                comp_d = Company.objects.get(name='Delhivery')
                if pref1 == comp_d.name:
                    prefrence = 1
                elif pref2 == comp_d.name:
                    prefrence = 2
                elif pref3 == comp_d.name:
                    prefrence = 3
                elif pref4 == comp_d.name:
                    prefrence = 4
                else:
                    prefrence = 5

                delhivery_data = Delivery.objects.get_or_create(
                    pincode = pin[0],
                    company = comp_d,
                    price = delhivery_limit,
                    prefrence= prefrence
                )

            if fedex == 'Y':
                comp_d = Company.objects.get(name='Fedex')
                if pref1 == comp_d.name:
                    prefrence = 1
                elif pref2 == comp_d.name:
                    prefrence = 2
                elif pref3 == comp_d.name:
                    prefrence = 3
                elif pref4 == comp_d.name:
                    prefrence = 4
                else:
                    prefrence = 5

                fedex_data = Delivery.objects.get_or_create(
                    pincode=pin[0],
                    company=comp_d,
                    price=fedex_limit,
                    prefrence=prefrence
                )

            if dotzot == 'Y':
                comp_d = Company.objects.get(name='Dotzot')
                if pref1 == comp_d.name:
                    prefrence = 1
                elif pref2 == comp_d.name:
                    prefrence = 2
                elif pref3 == comp_d.name:
                    prefrence = 3
                elif pref4 == comp_d.name:
                    prefrence = 4
                else:
                    prefrence = 5

                dotzot_data = Delivery.objects.get_or_create(
                    pincode=pin[0],
                    company=comp_d,
                    price=dotzot_limit,
                    prefrence=prefrence
                )

            if dtdc == 'Y':
                comp_d = Company.objects.get(name='DTDC')
                if pref1 == comp_d.name:
                    prefrence = 1
                elif pref2 == comp_d.name:
                    prefrence = 2
                elif pref3 == comp_d.name:
                    prefrence = 3
                elif pref4 == comp_d.name:
                    prefrence = 4
                else:
                    prefrence = 5

                dtdc_data = Delivery.objects.get_or_create(
                    pincode=pin[0],
                    company=comp_d,
                    price=0,
                    prefrence=prefrence
                )

            if indiapost == 'Y':
                comp_d = Company.objects.get(name='Indiapost')
                if pref1 == comp_d.name:
                    prefrence = 1
                elif pref2 == comp_d.name:
                    prefrence = 2
                elif pref3 == comp_d.name:
                    prefrence = 3
                elif pref4 == comp_d.name:
                    prefrence = 4
                else:
                    prefrence = 5

                indiapost_data = Delivery.objects.get_or_create(
                    pincode=pin[0],
                    company=comp_d,
                    price=0,
                    prefrence=prefrence
                )


open_excel()