import os

class Card:
  def __init__(self, name, number, balance):
    self.name = name
    self.number = number
    self.balance = balance

  def show_info(self):
    print("%s\t\t%d\t\t%d"%(self.name, self.number, self.balance))

class Menu:
  def load_data(self):
    if os.path.isfile("card.db"):
      with open("card.db", "r", encoding="utf-8") as f:
        for c_str in f.readlines():
          c_prop_list = c_str.strip().split("\t\t")
          c = Card(c_prop_list[0], int(c_prop_list[1]), int(c_prop_list[2]))
          self.card_list.append(c)

  def save_data(self):
    with open("card.db", "w", encoding="utf-8") as f:
      for c in self.card_list:
        c_str = "{0}\t\t{1}\t\t{2}\n".format(c.name, c.number, c.balance)
        f.write(c_str)

  def __init__(self):
    self.card_list = []
    self.load_data()

  def show_menu(self):
    print("欢迎使用卡片管理系统")
    print("1.添加卡")
    print("2.查询卡")
    print("3.注销卡")
    print("4.卡片充值")
    print("5.卡片退费")
    print("6.显示所有卡")
    print("7.退出")
    return eval(input("请选择："))
  
  def get_card(self, number):
    for c in self.card_list:
      if c.number == number:
        return c
    return None
    
  def show_card(self):
    number = eval(input("请输入卡号："))
    c = self.get_card(number)
    if c is None:
      print("未找到该卡")
    else:
      print("姓名\t\t卡号\t\t余额")
      c.show_info()
  
  def show_card_list(self):
    print("姓名\t\t卡号\t\t余额")
    for c in self.card_list:
      c.show_info()

  def add_card(self):
    name = input("请输入姓名：")
    if len(self.card_list) == 0:
      n = 1
    else:
      n = self.card_list[len(self.card_list) - 1].number + 1
    self.card_list.append(Card(name, n, 0))

  def del_card(self):
    number = eval(input("请输入卡号："))
    c = self.get_card(number)
    if c is None:
      print("未找到该卡")
    else:
      self.card_list.remove(c)
      print("删除成功")

  def recharge(self):
    number = eval(input("请输入卡号："))
    c = self.get_card(number)
    if c is None:
      print("未找到该卡")
    else:
      amount = eval(input("请输入充值金额："))
      c.balance += amount
      print("充值成功")

  def refund(self):
    number = eval(input("请输入卡号："))
    c = self.get_card(number)
    if c is None:
      print("未找到该卡")
    else:
      amount = eval(input("请输入退费金额："))
      if amount > c.balance:
        print("余额不足，退费失败")
      else:
        c.balance -= amount
        print("退费成功")

if __name__ == "__main__":
  m = Menu()
  flag = True
  while flag:
    slt = m.show_menu()
    if slt == 6:
      m.show_card_list()
    elif slt == 7:
      m.save_data()
      flag = False
    elif slt == 1:
      m.add_card()
    elif slt == 2:
      m.show_card()
    elif slt == 3:
      m.del_card()
    elif slt == 4:
      m.recharge()
    elif slt == 5:
      m.refund()