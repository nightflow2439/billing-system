import os

class Record:
  def __init__(self, user_num, machine_num, check_in_time, check_out_time, rate, balance):
    self.user_num = user_num
    self.machine_num = machine_num
    self.check_in_time = check_in_time
    self.check_out_time = check_out_time
    self.rate = rate
    self.balance = balance

  def show_info(self):
    print("卡号：%d"%self.user_num)
    print("机器号：%d"%self.machine_num)
    print("上机时间：%s"%self.check_in_time)
    print("下机时间：%s"%self.check_out_time)
    print("消费金额：%d"%self.rate)
    print("余额：%d"%self.balance)
    print("")

class Menu:
  def __init__(self):
    self.records = []
    self.load_records()

  def load_records(self):
    if os.path.isfile("records.txt"):
      with open("records.txt", "r", encoding="utf-8") as f:
        for r_str in f.readlines():
          r_prop_list = r_str.strip().split("\t\t")
          r = Record(int(r_prop_list[0]), int(r_prop_list[1]), r_prop_list[2], r_prop_list[3], int(r_prop_list[4]), int(r_prop_list[5]))
          self.records.append(r)

  def show_menu(self):
    print("欢迎来到记录查询系统：")
    print("1.查询消费记录")
    print("2.统计总营业额")
    print("3.退出")
    return eval(input("请选择："))
  
  def search_record(self):
    user_num = eval(input("请输入卡号："))
    for r in self.records:
      if r.user_num == user_num:
        r.show_info()

  def calculate_total_revenue(self):
    total_revenue = sum([r.rate for r in self.records])
    print("总营业额为：%d"%total_revenue)
    

if __name__ == "__main__":
  m = Menu()
  flag = True
  while flag:
    slt = m.show_menu()
    if slt == 1:
      m.search_record()
    elif slt == 2:
      m.calculate_total_revenue()
    elif slt == 3:
      flag = False