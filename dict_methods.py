'''
get()
proformat()
pprint()
setdefault()
'''
'''
d={'name':'kavya','contact':76769588,'city':'HRR'}
i=input('enter a key')
if i not in d.keys():
    k,v=input('enter a key val pair').split()
    d[k]=v
    print(d)
else:
    print(i,'is exist')



birthdays = { 'Harini' : 'April 13' , 'Srivani' : 'Oct 13' , 'Ravi' : 'Nov13', 'Tejaswini' : 'Oct6' }
i=input('enter a name')
if i in birthdays.keys():
    print('Harini\'s birthday is on',birthdays['Harini'])
else:
    d=input('enter date')
    birtdays=birthdays.get(i,d)
    print(birthdays)

    
birthdays = { 'Harini' : 'April 13' , 'Srivani' : 'Oct 13' , 'Ravi' : 'Nov13', 'Tejaswini' : 'Oct6' }
i=input('enter a name')
if i in birthdays.keys():
    print('Harini\'s birthday is on',birthdays['Harini'])
else:
    birthday=input('enter birthday')
    birthdays[i]=birthday
    print(birthdays)
'''

d={'hema':1,'manoj':1,'vidya':2,'jyothsna':3,'ravi':4,'karthik':6,'yashu':1.2,'harini':2.1,'prashanth':4.4}
new={}
d1={'hema':'BI','manoj':'QA','vidya':'QA','jyothsna':'QA','ravi':'DEV','karthik':'QA','yashu':'QA','harini':'BI','Prashanth':'QA'}
new1={}
QA={}
def comp(d,d1):
    for (k,v) in d.items(): #Traverse through first dictionary
        for (k1,v1) in d1.items():  #Traverse through second dictionary
            if (1<=v<=3) and (k in d1.keys()):  #condition1:experience should be 1-3yrs and condition2:emp should belongs to any one of teams
                if v==1:                        #if exp is 1yr then print emp name along with team name
                    new1[k]=v1
                new[k]=v
            if (2<=v<=3) and (v1=='QA'):    #if the exp is 2-3yrs and belongs to QA team then print emp name and team name
                QA[k]=v1
                #print(k,v,v1)
                #break
    print(new)
    print(new1)
    print(QA)
    
comp(d,d1)
            
        
