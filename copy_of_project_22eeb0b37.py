# -*- coding: utf-8 -*-
"""Copy of project 22eeb0b37.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JhwdQ5PgHW8KiQLeWm_ZCX_FFKqsNhIh
"""





y=int(input("no.of subjects:"))
t=0
subject=[]
credits=[]
for i in range(y):
    name=input("enter name of subject:")
    subject.append(name)
    g=int(input("no.of credits:"))
    credits.append(g)
    n=int(input("no.of students:"))
    q=int(input("no.of questions:"))
    user='nitw22'
    password='nitwcad'
    for i in range(4):
        u=input("enter username:")
        p=input("enter password:")
        if user==u and password==p:
           print("login suceessfully")
           break
        elif user==u and password!=p:
             print("password is incorrect try again")
        elif password==p and user!=u:
             print("user is incorrect try again")
        t=t+1
    if t==4:
       print("login unsucessful try again after few minutes")
       break
    import time
    k=0
    z=[]
    h=[]
    for i in range(n):
        m=0
        names=input("enter your name:")
        for j in range(q):
            ques=input("enter question:")
            a=input("first option:")
            b=input("enter second option:")
            c=input("third option:")
            d=input("fourth option:")
            ans=input("answer:")

            start=time.time()
            e=input("enter your choice")
            end=k+time.time()
            k=end-start
            if end-start<=20:
               if ans==e:
                  m=m+4
               elif e=="null":
                    m=m
               else:
                     m=m-1
        print("marks of",names,"in subject",name,"is :",str(m))
    for i in range(n):
        l=int(input("marks of students:"))
        z.append(l)
    sum=0
    for i in range(n):
        sum=sum+z[i]
    average=sum/n
    print("average marks of class:",average)
    std=0
    for i in range(n):
        std=std+(((average-z[i])**2)/n)**0.5
    print("standard deviation is:",std)
    j=[]
    o=[]
    for i in range(n):
        u=input("enter your name:")
        j.append(u)
        branch=input("enter your branch")
        o.append(branch)

        if z[i]>=average and z[i]<average+0.5*std:
           grade=7
        elif z[i]>=average+0.5*std and z[i]<average+0.75*std:
            grade=8
        elif z[i]>=average+0.75*std and z[i]<average+std:
             grade=9

        elif z[i]>=average+std and z[i]<=4*q:
              grade=10
        else:
              grade=6

        print("grade of student in subject",name,"for",u,"is:",str(grade))
        h.append(grade)
cr=0
for i in range(y):
    cr=cr+credits[i]
print("total no.of credits:",cr)
for i in range(n):
     gpa=0
     for x in range(y):
         gpa=gpa+h[x]*credits[x]
     d={
        "name":j[i],
        "branch":o[i],
        "gpa":gpa//cr
     }
     print(d)

from google.colab import drive
drive.mount('/content/drive')