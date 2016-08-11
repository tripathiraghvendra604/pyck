'''this file iterates through each row of xlsx file,
    and stores its values in database'''

import os
from xlrd import open_workbook
from .models import Info


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


            data = Info(
                pincode=pincode,
                delhivery=delhivery,
                delhivery_limit=delhivery_limit,
                fedex=fedex,
                fedex_limit=fedex_limit,
                dotzot=dotzot,
                dotzot_limit=dotzot_limit,
                dtdc=dtdc,
                indiapost=indiapost,
                pref1=pref1,
                pref2=pref2,
                pref3=pref3,
                pref4=pref4,
                pref5=pref5,
            )
            data.save()



open_excel()