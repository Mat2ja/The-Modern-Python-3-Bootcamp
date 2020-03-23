times = 1
while times < 20: # till 19 in a row, 10 rows
    spaces = 20 - times
    sides = spaces // 2
    print(" " * sides + "A" * times + " " * sides)
    times += 2

'''
          A
         AAA
        AAAAA
       AAAAAAA
      AAAAAAAAA
     AAAAAAAAAAA
    AAAAAAAAAAAAA
   AAAAAAAAAAAAAAA
  AAAAAAAAAAAAAAAAA
 AAAAAAAAAAAAAAAAAAA

'''







# times = 1
# while times < 22: # till 21 in a row
#     spaces = 21 - times
#     sides = spaces // 2
#     print(" " * sides + "\U0001f600" * times + " " * sides)
#     times += 2