
try:
	num = int(input("CAN JAZ:  ")) # сан енгизу болими
except:
	print("CAN ENGIZINIZ")    # сан жазбаган жагдайда прогр шыгарады
	exit()         

f=open('output.txt', 'w')



for i in range(num):   # for циклы аркылы енг3згер саннын сифрын шыгарат
	for j in range((num - i) + 5): #ушбурыштын сыртындагы коринбейтин обьекттер
		print(end=" ")   
	for j in range(i + 1):      #ушбурынтын басындагы точкасы нешеден басталатыны
		print("*", end=" ")   #
	print()  #сонгы натижесин шыгарат принт аркылы
	f.write(str(j)+"\n")
f.close()

