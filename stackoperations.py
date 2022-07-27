import time

def isEmpty(stk):
	if stk==[]:
		return True
	else:
		return False

def Push(stk, item):
	stk.append(item)
	top=len(stk)-1

def Pop(stk):
	if isEmpty(stk):
		return "UNDERFLOW"
	else:
		item=stk.pop()
		if len(stk)==0:
			top=None
		else:
			top=len(stk)-1
		return item

def Peek(stk):
	if isEmpty(stk):
		return "UNDERFLOW"
	else:
		top=len(stk)-1
		return stk[top]

def Display(stk):
	if isEmpty(stk):
		print("STACK IS EMPTY")
	else:
		top=len(stk)-1
		print(stk[top], "<--TOP")
		for i in range(top-1, -1, -1):
			print(stk[i])


#__main__

Stack=[]
top=None

while True:
	print("\nSTACK OPERATIONS")
	print("1. PUSH")
	print("2. POP")
	print("3. PEEK")
	print("4. DISPLAY STACK")
	print("5. EXIT\n")

	ch=int(input("ENTER THE ELEMENT HERE : "))

	print("\n---->\n ")
	
	if ch==1:
		item=int(input("ENTER THE ITEM : "))
		Push(Stack, item)

	
	elif ch==2:
		item=Pop(Stack)
		if item=="UNDERFLOW":
			print("UNDERFLOW, THE STACK IS EMPTY")
		else:
			print("POPPED ITEM IS ", item)
	
	elif ch==3:
		item=Peek(Stack)
		if item=="UNDERFLOW":
			print("UNDERFLOW, STACK IS EMPTY")
		else:
			print("TOPMOST ITEM IS", item)
	elif ch==4:
		Display(Stack)
	elif ch==5:
		print("THANK YOU FOR USING")
		time.sleep(2)
		break
	else:
		print("INVALID CHOICE")