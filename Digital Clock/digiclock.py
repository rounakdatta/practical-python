import time
import sys

def one():
	print ("\t \n\t\b  |\n\t\b  |",end="")

def two():
	print ("\t_\n\t\b _|\n\t\b|_ ",end="")

def three():
	print ("\t_\n\t\b _|\n\t\b _|",end="")

def four():
	print ("\t \n\t\b|_|\n\t\b  |",end="")

def five():
	print ("\t_\n\t\b|_ \n\t\b _|",end="")

def six():
	print ("\t_\n\t\b|_ \n\t\b|_|",end="")

def seven():
	print ("\t_\n\t\b  |\n\t\b  |",end="")

def eight():
	print ("\t_\n\t\b|_|\n\t\b|_|",end="")
	#print("\033[F\033[F")

def nine():
	print ("\t_\n\t\b|_|\n\t\b _|",end="")

def zero():
	print ("\t_\n\t\b| |\n\t\b|_|",end="")


def options(x):
	if(x=='1'):
		one()
	elif(x=='2'):
		two()
	elif(x=='3'):
		three()
	elif(x=='4'):
		four()
	elif(x=='5'):
		five()
	elif(x=='6'):
		six()
	elif(x=='7'):
		seven()
	elif(x=='8'):
		eight()
	elif(x=='9'):
		nine()
	else:
		zero()


def run():
	print("\033c")
	#fulltime=time.strftime('%l:%M%p %Z on %b %d, %Y')
	now=time.strftime('%X')
	#print(now)
	options(now[0])
	#print("\033[F\033[F\t\t\t\t\t\thello",end="")
	print("\n")
	options(now[1])
	print("\n")
	options(now[3])
	print("\n")
	options(now[4])
	print("\n")
	options(now[6])
	print("\n")
	options(now[7])






def update():
    
    while True:
        run()
        time.sleep(1)

update()