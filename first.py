# # print("hello world")
# # a = 9
# # b=9
# # c = a+b
# # print(c)
# # print("here\\n heyyy")
# # var = "ROOOOO"
# # print(var + var)
# # #print("heyyyy"+ b)
# # def cube(nu,ni):
 # # inw = 1
 # # while ni!=0:
  # # inw=inw*nu
  # # ni=ni-1
 
 # # return inw
 
# # re=cube(3,4)
# # print("here")
# # print(re)

# def tran(word):
 # res=""
 # for letter in word:
  # if letter in " ":
   # res = res + "_"
  # else:
   # res=res+letter
 # return res
 
# print(tran(input("Enter \n")))
emp = open("text.txt","a")
emp.write("This will or will not be in next line")
print("heyyy")
emp.close();