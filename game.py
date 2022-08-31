

field = [
  ["0", "1", "2"],
  ["3", "4", "5"],
  ["6", "7", "8"]
  ]

#フィールド描画
def draw_field(field):
  print("---------------------")
  for i in field:
    print(i)

#適切に選択して描画
def our_select(field):

  while True:
    s = int(input("マスの番号を選択してください。"))
    
    if s == 0 or s == 1 or s == 2:
      if field[0][s] == "●" or field[0][s] == "✖️":
        print('空いている適切なマスを選択してください。')
        continue
      else:
        field[0][s] = "●"
        break
      
    elif s == 3 or s == 4 or s == 5:
      if field[1][s-3] == "●" or field[1][s-3] == "✖️":
        print('空いている適切なマスを選択してください。')
        continue
      else:
        field[1][s-3] = "●"
        break
      
    elif s == 6 or s == 7 or s == 8:
      if field[2][s-6] == "●" or field[2][s-6] == "✖️":
        print('空いている適切なマスを選択してください。')
        continue
      else:
        field[2][s-6] = "●"
        break
    else:
      print('空いている適切なマスを選択してください。')
      continue
    
    
  return field
        
      

  
        
  
  


#縦、横、斜めのどれかが揃っていたらTrueそれ以外False
def judge(field):
  
  for x in field: #縦
    if x[0] == x[1] == x[2]:
      return True
      
  for y in range(3):#横
    if field[y][0] == field[y][1] == field[y][2]:
      return True
      
  if field[0][0] == field[1][1] == field[2][2]:#右下斜線
    return True
  
  if field[0][2] == field[1][1] == field[2][0]:#右上斜線
    return True
  


while True:
  draw_field(field)
  
  our_select(field)
  
  draw_field(field)
  
  