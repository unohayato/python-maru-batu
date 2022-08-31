




field = [
  ["0", "1","2",],
  ["3", "4","5",],
  ["6", "7","8",],
  ]
for i in field:
  print(i)


#縦、横、斜めのどれかが揃っていたらTrueそれ以外False
def judge(field):
  ret = False
  for x in field: #縦
    if x[0] == x[1] == x[2]:
      ret = True
      
  for y in range(3):#横
    if field[y][0] == field[y][1] == field[y][2]:
      ret = True
      
  if field[0][0] == field[1][1] == field[2][2]:#右下斜線
    ret = True
  
  if field[0][2] == field[1][1] == field[2][0]:#右上斜線
    ret = True
  
  return ret

field[0] = ["●", "●", "✖️"]

print(judge(field))