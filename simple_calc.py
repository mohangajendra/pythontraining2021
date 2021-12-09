
#f_num, s_num=read_inputs()
# op=str(input("ënter operation you want to perform"))
def calculator1(oper,input1, input2):
	calc={}
	sum_=input1+input2
	product=input1*input2
	qu=input1/input2
	diff=input1-input2
	calc['add']=sum_
	calc['mul']=product
	calc['div']=qu
	calc['sub']=diff
	print(calc.get(oper, "not a valid arthiemtic operation"))

# Driver program
if __name__ == "__main__":
	oper=input("enter the operator:")
	input1=int(input("enter the 1st input:"))
	input2=int(input("enter the 2nd input:"))
	calculator1(oper,input1,input2)
