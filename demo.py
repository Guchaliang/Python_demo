# coding: GBK

class student:

    def __init__(self, name, tel, QQ, id):
        self.name = name
        self.tel = tel
        self.QQ = QQ
        self.id = id

        # 使用times是因为我没有办法记录下时间，所以就使用次数
        # 但是在JavaScript中，可以记录下
        # 进入网站的此时时间，之后在关闭时，记录下关闭时间，就可以得到使用时长
        # 但是这个可能也有问题，所以需要更加细致
        self.times = 0

    def lab_times(self):
        self.times += 1

    def show_lab_times(self):
        print("%s 进入实验室 %d 次" % (self.name, self.times))


print("请依次输入姓名,电话,QQ,学号")

xiaoming = student("谁", 123456, 123456, 123456)

xiaoming.lab_times()

xiaoming.show_lab_times()
