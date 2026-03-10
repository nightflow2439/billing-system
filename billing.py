import time, os, math
from datetime import datetime, timedelta
from card import Card

class ActiveUser:
  def __init__(self, user_num, machine_num, check_in_time):
    self.user_num = user_num
    self.machine_num = machine_num
    self.check_in_time = check_in_time

class Menu:
  def __init__(self):
    self.active_users = []
    self.card_list = []
    self.load_cards()
    self.load_active_users()
    self.load_standard()

  def load_standard(self):
    self.rate = 10
    if os.path.isfile("standard.txt"):
      with open("standard.txt", "r", encoding="utf-8") as f:
        str = f.read().strip()
        if str and int(str) > 0:
          self.rate = int(str)

  def load_active_users(self):
    if os.path.isfile("active_users.txt"):
      with open("active_users.txt", "r", encoding="utf-8") as f:
        for au_str in f.readlines():
          au_prop_list = au_str.strip().split("\t\t")
          au = ActiveUser(int(au_prop_list[0]), int(au_prop_list[1]), datetime.fromisoformat(au_prop_list[2]))
          self.active_users.append(au)

  def save_active_users(self):
    with open("active_users.txt", "w", encoding="utf-8") as f:
      for au in self.active_users:
        au_str = "{0}\t\t{1}\t\t{2}\n".format(au.user_num, au.machine_num, au.check_in_time.isoformat())
        f.write(au_str)

  def show_menu(self):
    print("欢迎使用上下机管理系统")
    print("1.上机")
    print("2.下机")
    print("3.查询用机情况")
    print("4.退出")
    return eval(input("请选择："))

  def load_cards(self):
    if os.path.isfile("cards.txt"):
      with open("cards.txt", "r", encoding="utf-8") as f:
        for c_str in f.readlines():
          c_prop_list = c_str.strip().split("\t\t")
          c = Card(c_prop_list[0], int(c_prop_list[1]), int(c_prop_list[2]))
          self.card_list.append(c)

  def save_cards(self):
    with open("cards.txt", "w", encoding="utf-8") as f:
      for c in self.card_list:
        c_str = "{0}\t\t{1}\t\t{2}\n".format(c.name, c.number, c.balance)
        f.write(c_str)

  def get_card(self, number):
    for c in self.card_list:
      if c.number == number:
        return c
    return None

  def check_machine(self, machine_num):
    for au in self.active_users:
      if au.machine_num == machine_num:
        return au
    return None

  def check_in(self):
    user_num = eval(input("请输入卡号："))
    c = self.get_card(user_num)
    if c is None:
      print("未找到该卡")
      return
    if c.balance < self.rate:
      print("余额不足")
      return
    machine_num = eval(input("请输入机号："))
    if self.check_machine(machine_num) is not None:
      print("该机已上机")
      return
    check_in_time = datetime.now()
    self.active_users.append(ActiveUser(user_num, machine_num, check_in_time))
    print("上机成功")                                         

  def check_out(self):
    machine_num = eval(input("请输入机号："))
    check_out_time = datetime.now()
    for au in self.active_users:
      if au.machine_num == machine_num:
        self.calculate_cost(au.user_num, au.machine_num, au.check_in_time, check_out_time)
        self.active_users.remove(au)
        print("下机成功")
        return
    print("未找到该机上机记录")

  def calculate_cost(self, user_num, machine_num, check_in_time, check_out_time):
    duration = int((check_out_time - check_in_time).total_seconds())
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60
    print("使用时间：%d小时%d分钟%d秒"%(hours, minutes, seconds))
    billing_hours = math.ceil(duration / 3600)
    rate = self.rate * billing_hours
    print("消费金额：%d"%rate)
    c = self.get_card(user_num)
    c.balance -= rate
    print("卡上余额：%d"%c.balance)
    with open("records.txt", "a", encoding="utf-8") as f:
      r_str = "{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}\t\t{5}\n".format(user_num, machine_num, check_in_time.isoformat(), check_out_time.isoformat(), rate, c.balance)
      f.write(r_str)

  def show_machine_status(self):
    machine_num = eval(input("请输入机号："))
    au = self.check_machine(machine_num)
    if au is None:
      print("状态：下机")
    else:
      print("状态：上机")
      duration = int((datetime.now() - au.check_in_time).total_seconds())
      hours = duration // 3600
      minutes = (duration % 3600) // 60
      seconds = duration % 60
      print("使用者卡号：%d"%au.user_num)
      print("使用时间：%d小时%d分钟%d秒"%(hours, minutes, seconds))

if __name__ == "__main__":
  m = Menu()
  flag = True
  while flag:
    slt = m.show_menu()
    if slt == 4:
      m.save_cards()
      m.save_active_users()
      flag = False
    elif slt == 1:
      m.check_in()
    elif slt == 2:
      m.check_out()
    elif slt == 3:
      m.show_machine_status()