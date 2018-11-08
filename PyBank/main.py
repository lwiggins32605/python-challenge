import os
import csv

csvfile = os.path.join('budget_data.csv')
with open(csvfile) as csvfile:
    readcsv = csv.reader(csvfile, delimiter=',')
    print(readcsv)
    header = next(readcsv)
    print (header) 
    first_month = next(readcsv) 
    months = 1
    revenue = int (first_month [1])
    mean = []
    past_m = int (first_month [1])
    increase = 0
    decrease = 0
    for row in readcsv: 
        months +=1
        revenue +=int (row [1])
        mean.append (int (row [1])-past_m)
        past_m = int (row [1])
        if increase < int (row [1]): 
            increase = int (row [1])
            largest_m = (row [0])

        if decrease > int (row [1]):
            decrease = int (row [1])
            largest_dm = (row [0])



print (months)
print (revenue)   
print (sum (mean)/len (mean))
print (increase)
print (largest_m)
print (decrease)
print (largest_dm)




