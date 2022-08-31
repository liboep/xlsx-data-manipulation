#!/usr/bin/env python
# coding: utf-8



import pandas as pd


xl_all = pd.read_excel('datafile1.xlsx', sheet_name=None)

#create new columns using pandas.mean() func for each semester and subject

#Semester 1 avg

xl_all['HISTORY']['Average Score Sem1'] = xl_all['HISTORY'][['semester1', 'final_exam']].mean(axis=1, numeric_only=True)
xl_all['MATHEMATICS']['Average Score Sem1'] = xl_all['MATHEMATICS'][['semester1', 'final_exam']].mean(axis=1, numeric_only=True)

#Semester 2 avg

xl_all['HISTORY']['Average Score Sem2'] = xl_all['HISTORY'][['semester2', 'final_exam']].mean(axis=1, numeric_only=True)
xl_all['MATHEMATICS']['Average Score Sem2'] = xl_all['MATHEMATICS'][['semester2', 'final_exam']].mean(axis=1, numeric_only=True)



#find max and then combine it the student's name

#Semester 1 best

column = xl_all['HISTORY']["Average Score Sem1"]
max_value = column.max()
h_best = xl_all['HISTORY']['names'].where(xl_all['HISTORY']['Average Score Sem1'] == max_value)
h_best = h_best.dropna()
print("Στο μάθημα Ιστόρια ο καλύτερος μαθητής της τάξης είναι ο/η", h_best.to_string(index=False), "με βαθμό", "{:.2f}".format(max_value), "για το τετράμηνο Α.")

column = xl_all['MATHEMATICS']["Average Score Sem1"]
max_value = column.max()
h_best = xl_all['MATHEMATICS']['names'].where(xl_all['MATHEMATICS']['Average Score Sem1'] == max_value)
h_best = h_best.dropna()
print("Στο μάθημα Μαθηματικά ο καλύτερος μαθητής της τάξης είναι ο/η", h_best.to_string(index=False), "με βαθμό", "{:.2f}".format(max_value), "για το τετράμηνο Α.")

#Semester 2 best

column = xl_all['HISTORY']["Average Score Sem2"]
max_value = column.max()
h_best = xl_all['HISTORY']['names'].where(xl_all['HISTORY']['Average Score Sem2'] == max_value)
h_best = h_best.dropna()
print("Στο μάθημα Ιστόρια ο καλύτερος μαθητής της τάξης είναι ο/η", h_best.to_string(index=False), "με βαθμό", "{:.2f}".format(max_value), "για το τετράμηνο B.")

column = xl_all['MATHEMATICS']["Average Score Sem2"]
max_value = column.max()
h_best = xl_all['MATHEMATICS']['names'].where(xl_all['MATHEMATICS']['Average Score Sem2'] == max_value)
h_best = h_best.dropna()
print("Στο μάθημα Μαθηματικά ο καλύτερος μαθητής της τάξης είναι ο/η", h_best.to_string(index=False), "με βαθμό", "{:.2f}".format(max_value), "για το τετράμηνο B.")


#create new columns using pandas.mean() func again

xl_all['HISTORY']['Average Score'] = xl_all['HISTORY'].mean(axis=1, numeric_only=True)
xl_all['MATHEMATICS']['Average Score'] = xl_all['MATHEMATICS'].mean(axis=1, numeric_only=True)

#use pandas.plot() func to create the histograms

xl_all['HISTORY'].plot.bar(x='names', y='Average Score', title='HISTORY')
xl_all['MATHEMATICS'].plot.bar(x='names', y='Average Score', title='MATHEMATICS')


#create a copy of dataframe with selected columns

task_3 = xl_all['HISTORY'][['names', 'Average Score']].copy()

#rename columns to avoid name collision

task_3.rename(columns = {'Average Score':'Average Score History'}, inplace = True)

#add column from mathematics sheet

task_3['Average Score Mathematics'] = xl_all['MATHEMATICS'][['Average Score']]
task_3['Average Score'] = task_3[['Average Score History', 'Average Score Mathematics']].mean(axis=1, numeric_only=True)

#convert dataframe to 2d list

names_arr = task_3[['names']].to_numpy()
avrg_arr = task_3[['Average Score']].to_numpy()
list2d = list(zip(names_arr, avrg_arr))

#sort func for 2d list

def sort_stud_score(list2d):
    list2d = sorted(list2d,key=lambda l:l[1], reverse=True)
    return list2d

sorted2d_sc = sort_stud_score(list2d)

#print results

print("Οι μαθητές με φθίνουσα σειρά συνολικής βαθμολογίας:")
for i in sorted2d_sc:
    print('\t'.join(map(str, i)))


#same as previous but sorted by name

def sort_stud_name(list2d):
    list2d = sorted(list2d,key=lambda l:l[0])
    return list2d
    
sorted2d_nm = sort_stud_name(list2d)
print("Οι μαθητές με αλφαβιτική σειρά:")
for i in sorted2d_nm:
    print('\t'.join(map(str, i)))


#count all students and declare limit to 5

count_stud = xl_all['HISTORY'][['names']].count().iloc[0]
limit = 5

#count studs with final exam >5, find percentage and print it

col_history = xl_all['HISTORY'][['final_exam']]
count_hist = col_history[col_history > limit].count().iloc[0]

perc_hist = (count_hist*100)/count_stud

print("Το ποσοστό των μαθητών με βαθμό εξέτασης μεγαλύτερο του 5 στην Ιστορία είναι ", perc_hist, ".", sep='')

col_mathematics = xl_all['MATHEMATICS'][['final_exam']]
count_maths = col_mathematics[col_mathematics > limit].count().iloc[0]

perc_maths = (count_maths*100)/count_stud

print("Το ποσοστό των μαθητών με βαθμό εξέτασης μεγαλύτερο του 5 στα Μαθηματικά είναι ", perc_maths, ".", sep='')




