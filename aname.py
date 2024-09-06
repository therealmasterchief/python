class lstring:
    def __init__(self):
        self.str1=""
    def getinputs(self):
        self.str1=input("enter a word\n")
    def display(self):
        print("uppercase",self.str1.upper())

x=lstring()
x.getinputs()
x.display()