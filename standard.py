import os

class Menu:
  def __init__(self):
    self.load_standard()

  def load_standard(self):
    self.rate = 10
    if os.path.isfile("standard.txt"):
      with open("standard.txt", "r", encoding="utf-8") as f:
        str = f.read().strip()
        if str and int(str) > 0:
          self.rate = int(str)

  def save_standard(self):
    with open("standard.txt", "w", encoding="utf-8") as f:
      f.write(str(self.rate))

  def show_menu(self):
    print("欢迎来到计费标准管理系统")
    rate = 10
    print("当前计费标准：%d元/时（不足1小时部分按1小时计算）"%self.rate)
    print("1.更改计费标准")
    print("2.退出")
    return eval(input("请选择："))
  
  def change_standard(self):
    new_rate = eval(input("新的计费标准为（单位：元/时）："))
    if new_rate <= 0:
      print("更改无效")
      return
    self.rate = new_rate
    print("更改成功")

if __name__ == "__main__":
  m = Menu()
  flag = True
  while flag:
    slt = m.show_menu()
    if slt == 2:
      m.save_standard()
      flag = False
    elif slt == 1:
      m.change_standard()