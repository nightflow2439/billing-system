import billing, card, query, standard

class Menu:
  def show_menu(self):
    print("欢迎使用计费管理系统")
    print("1.上下机管理")
    print("2.卡片管理")
    print("3.记录查询")
    print("4.计费标准管理")
    print("5.退出")
    return eval(input("请选择："))
  
if __name__ == "__main__":
  m = Menu()
  flag = True
  while flag:
    slt = m.show_menu()
    if slt == 1:
      m1 = billing.Menu()
      flag1 = True
      while flag1:
        slt1 = m1.show_menu()
        if slt1 == 4:
          m1.save_cards()
          m1.save_active_users()
          flag1 = False
        elif slt1 == 1:
          m1.check_in()
        elif slt1 == 2:
          m1.check_out()
        elif slt1 == 3:
          m1.show_machine_status()
    elif slt == 2:
      m2 = card.Menu()
      flag2 = True
      while flag2:
        slt2 = m2.show_menu()
        if slt2 == 6:
          m2.show_card_list()
        elif slt2 == 7:
          m2.save_cards()
          flag2 = False
        elif slt2 == 1:
          m2.add_card()
        elif slt2 == 2:
          m2.show_card()
        elif slt2 == 3:
          m2.del_card()
        elif slt2 == 4:
          m2.recharge()
        elif slt2 == 5:
          m2.refund()
    elif slt == 3:
      m3 = query.Menu()
      flag3 = True
      while flag3:
        slt3 = m3.show_menu()
        if slt3 == 1:
          m3.search_record()
        elif slt3 == 2:
          m3.calculate_total_revenue()
        elif slt3 == 3:
          flag3 = False
    elif slt == 4:
      m4 = standard.Menu()
      flag4 = True
      while flag4:
        slt4 = m4.show_menu()
        if slt4 == 2:
          m4.save_standard()
          flag4 = False
        elif slt4 == 1:
          m4.change_standard()
    elif slt == 5:
      flag = False