# import numpy as np
# dep = ["cs","cs",'dt','dcd','dt','as','as','ice','ice','ice']
# sno = ['0001' ,'0002','0003','0004','0005','0006','0007','0008','0009','0010']
# gpa = [2.10,3.50,4.50,2.70,3.00,3.15,4.00,0.00,3.25,3.70]
# dep = np.array(['cs','cs','dt','dcd','dt','as','as','ice','ice','ice'])
# sno = np.array(['0001' ,'0002','0003','0004','0005','0006','0007','0008','0009','0010'])
# gpa = np.array([2.10,3.50,4.50,2.70,3.00,3.15,4.00,0.00,3.25,3.70])
# print(dep.dtype)
import pandas as pd
dep= pd.Series(['cs','cs','dt','dcd','dt','as','as','ice','ice','ice'])
sno= pd.Series(['0001' ,'0002','0003','0004','0005','0006','0007','0008','0009','0010'])
gpa= pd.Series([2.10,3.50,4.50,2.70,3.00,3.15,4.00,0.00,3.25,3.70])
# sum =0.0
# for i in gpa:
#     sum = sum +i
# mean=sum/len(gpa)
# print('%.2f' %mean)
# print(gpa)
# print(np.mean(gpa))
# print(np.median(gpa))
# tb1 = pd.DataFrame(gpa)

print(gpa.mean())
# print(gpa.median())
# def median(list):
#     median = 0
#     list.sort()
#     print(list)
#     if len(list)%2==1:
#         median = list[len(list)//2]
#     else:
#         median = (list[(len(list)//2)-1] + list[len(list)//2])/2
#     return median
# print(median(gpa))
# tb2 = pd.DataFrame({"dep":dep,
#                     "sno":sno,
#                     "gpa":gpa})
# # print(tb2.sort_values(by="gpa",ascending=False)[2:3])
# grouped= tb2['gpa'].groupby(tb2['dep'])
# print(grouped.mean())
# print(grouped.max())
# # print(grouped.min())
# tb3 = pd.DataFrame({ 'dep' : ["cs", "cs", "dt", "dt", "dt", "as", "as", "cs", "dt", "as"],
# 'sno' : ["0001", "0002", "0003", "0004", "0005", "0006", "0007", "0008", "0009", "0010"], 'gpa' : [2.10, 3.50, 4.50, 2.70, 3.00, 3.20, 4.00, 0.00, 3.20, 3.70],
# 'year' : [2018, 2018, 2019, 2019, 2020, 2020, 2020, 2020, 2021, 2021]})
# a=tb3.groupby(['dep','year'],as_index = False).mean()
# print(a)
# print(a.pivot("dep",'year','gpa'))
# print(tb3_grouped.tail())
# tb4 = tb3_grouped.pivot(index='dep',columns='year')
# print(tb4)
# tb3_pviot= tb3.pivot_table(index = 'dep',columns='year',values='gpa')

# tb4_pviot= tb3.pivot(index = 'dep',columns='year',values='gpa')
# print(tb3_pviot)
