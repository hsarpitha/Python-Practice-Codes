class Demo1:
    def disp1(self):
        print('Inside disp1')
class Demo2(Demo1):
    def disp2(self):
        pass

d2 = Demo2()
d2.disp1() #Inside disp1


