class Demo:
    def disp(self):
        print('Inside disp with 0 para')
    def disp(self,a):
        print('Inside disp with 1 para')
    #Only last method with 2 para is exceuted.
    def disp(self,a,b):
        print('Inside disp with 2 para')
d = Demo()
# d.disp() Error
# d.disp(10) Error
d.disp(20, 30)

