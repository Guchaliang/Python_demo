# coding: GBK

class student:

    def __init__(self, name, tel, QQ, id):
        self.name = name
        self.tel = tel
        self.QQ = QQ
        self.id = id

        # ʹ��times����Ϊ��û�а취��¼��ʱ�䣬���Ծ�ʹ�ô���
        # ������JavaScript�У����Լ�¼��
        # ������վ�Ĵ�ʱʱ�䣬֮���ڹر�ʱ����¼�¹ر�ʱ�䣬�Ϳ��Եõ�ʹ��ʱ��
        # �����������Ҳ�����⣬������Ҫ����ϸ��
        self.times = 0

    def lab_times(self):
        self.times += 1

    def show_lab_times(self):
        print("%s ����ʵ���� %d ��" % (self.name, self.times))


print("��������������,�绰,QQ,ѧ��")

xiaoming = student("˭", 123456, 123456, 123456)

xiaoming.lab_times()

xiaoming.show_lab_times()
