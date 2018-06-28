class UI:
    def input(self):
        q=GPA()
        n=int(input("Enter number of Semesters : "))
        for i in range(n):
            s=int(input("Enter number of courses : "))
            for i in range(s):
                c=int(input("Enter credit : "))
                g=str(input("Enter grade: "))

                q.add_credit(c)
                q.add_grade(g)

                #q. g_c()
        return q

                




class GPA:
    def __init__(self):
        self.credit=[]
        self.grade=[]

    def add_credit(self,c):
        self.credit.append(c)
        print(self.credit)

    def add_grade(self,g):
        self.grade.append(g)
        print(self.grade)

    #def g_c(self):
        #gc=[a= 4.0,a- =3.7,b+ =3.3,b=3.0,b- =2.7,c+ =2.3,c=2.0,c- =1.7,d+ =1.3,d=1.0,f=0.0]
        #print(gc)
            
        
    
z=UI()
z.input()

#GPA.g_c(g)
