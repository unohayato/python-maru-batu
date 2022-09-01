
import random
#import time
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
  return field

#適切に選択して描画
def our_select(field):

  while True:
    s = int(input("マスの番号を選択してください。"))
    
    if s == 0 or s == 1 or s == 2:
      if field[0][s] == "o" or field[0][s] == "x":
        print('空いている適切なマスを選択してください。')
        continue
      else:
        field[0][s] = "o"
        break
      
    elif s == 3 or s == 4 or s == 5:
      if field[1][s-3] == "o" or field[1][s-3] == "x":
        print('空いている適切なマスを選択してください。')
        continue
      else:
        field[1][s-3] = "o"
        break
      
    elif s == 6 or s == 7 or s == 8:
      if field[2][s-6] == "o" or field[2][s-6] == "x":
        print('空いている適切なマスを選択してください。')
        continue
      else:
        field[2][s-6] = "o"
        break
    else:
      print('空いている適切なマスを選択してください。')
      continue
  
  return field

#cpuの選択
def cpu_select(field):
  while True:
    y = random.randint(0, 2)
    x = random.randint(0, 2)
    
    if field[y][x] == "o" or field[y][x] == "o":
      continue
    else:
      field[y][x] = "x"
      break
    
  return field
      
      
  
        
      

#縦、横、斜めのどれかが揃っていたらTrueそれ以外False
def judge(field):
  ans1 = "あなたの勝ちです。"
  
  #縦
  for x in range(3):  
    if field[0][x] == field[1][x] == field[2][x]:
      if field[0][x] == "o":
        print(ans1)
        
  #横
  
  """

  
  ans1 = "あなたの勝ちです。"
  ans2 = "CPUの勝ちです。"
  
  for y in range(3): #横
    if field[y][0] == field[y][1] and field[y][1] == field[y][2]:
      if field[y][0] == "o":
        print(ans1)
    
      elif field[y][0] == "x":
        print(ans2)
    
      
  for i in range(3):#縦
    if field[i][0] == field[i][0] and field[i][0] == field[i][0]:
      if field[i][0] == "o":
        print(ans1)
      
      elif field[i][0] == "x":
        print(ans2)
      
        
  if field[0][0] == field[1][1] and field[1][1] == field[2][2]:#右下斜線
    if field[0][0] == "o":
      print(ans1)
  
    elif field[0][0] == "x":
      print(ans2)
      
      
  if field[0][2] == field[1][1] and field[1][1] == field[2][0]:#右上斜線
    if field[0][2] == "o":
      print(ans1)
      
    elif field[0][2] == "x":
      print(ans2)
      
  """
  
    
    

turn = 0
draw_field(field)
while True:
  
  
  our_select(field)
  judge(field)
  turn += 1
  if turn == 5:
    exit()
  
  cpu_select(field)
  #judge(field)
  
  draw_field(field)
  