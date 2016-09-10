#Ashvin Fernandes, June 2nd 2016
import re

def convertBrackets(equation):
	"""Takes a string representing one side of an equation and returns a string with all brackets removed."""
	leftmost = equation.find("(")
	if leftmost == -1:
		return equation

	x = leftmost
	bracketcount = 1
	while x < len(equation) and bracketcount != 0:
		x += 1
		if equation[x] == "(":
			bracketcount += 1
		elif equation[x] == ")":
			bracketcount -= 1
		   
	if (leftmost == 0) or (equation[leftmost - 2] == "+"):
		retEquation = equation[:leftmost] + equation[leftmost+1:x] + equation[x+1:len(equation) + 1]	
	else:
		replacement = equation[leftmost+1:x]
		replacement = replacement.replace("-", "!")
		replacement = replacement.replace("+", "-")
		replacement = replacement.replace("!", "+")
		retEquation = equation[:leftmost] + replacement + equation[x+1:len(equation) + 1]
		
	return convertBrackets(retEquation)

def equationToDict(equationInput):
	"""Takes a string representing one side of an equation. 
	Returns a dictionary with the variables of the equation as keys and the coefficients as values. 
	Numbers without variables are keyed to ""  """
	
	equation = equationInput.split(" ")
	sign = 1
	dict ={}
	for summand in equation:
		
		term = re.split(r'(^\d+(?:\.\d+)?)', summand, 1)

		if len(term) == 1:
			if term[0] == "+":
				pass
			elif term[0] == "-":
				sign = -1
				continue
			elif not(term[0].isdigit()): #single variable
				if term[0] in dict:
					dict[term[0]] += 1.0 * sign
				else:
					dict[term[0]] = 1.0 * sign
			else:
				if "" in dict:
					dict[""] += float(term[0]) * sign
				else:
					dict[""] = float(term[0]) * sign
			sign = 1
			continue

			
		coeff = float(term[1])
		var = term[2]
		if var in dict:
			dict[var] += coeff * sign
		else:
			dict[var] = coeff * sign
			
		sign = 1
		
	return dict
	
def mergeCanonDict(LS, RS):
	"""Takes two dictionaries referring to two sides of an equation and returns a dictionary merging them together"""
	canon = {}
	for var in LS:
		if var in RS:
			canon[var] = LS[var] - RS[var]
		else: 
			canon[var] = LS[var]
			
	for var in RS:
		if var not in LS:
			canon[var] = RS[var] * -1
			
	return canon

def canonToString(canon):
	"""Takes a dictionary representing a canonical equation and returns the equation in string form"""
	retString = ""
	sortedCanon = sortCanon(list(canon.keys()))
	
	for var in sortedCanon:
		if canon[var] == 1 and var != "":
			retString += " + " + var
		elif canon[var] == -1 and var != "":
			retString += " - " + var
		elif canon[var] < 0:
			retString += " - " + ("%0.1f" % (canon[var] * -1.0)) + var
		elif canon[var] > 0:
			retString += " + " + "%0.1f" % canon[var] + var
			
			
	if len(retString) > 0 and retString[1] == "+":
		retString = retString[3:(len(retString) + 1)]
			
	retString += " = 0"
	
	if retString == " = 0":
		retString = "0 = 0"
	
	return retString
	
	
def convertToCanon(input):
	"""Takes a string representing an equation and returns a string with that equation in canonical form."""
	
	sides = input.split(" = ")
	LS = sides[0]
	RS = sides[1]
	LS = convertBrackets(LS)
	RS = convertBrackets(RS)
	canon = mergeCanonDict(equationToDict(LS), equationToDict(RS))
	return canonToString(canon)
	
def sortCanon(varList):
	"""Takes a list of keys representing variables and returns them in a sorted list.
	Variables with the highest power are given priority, and variables with equal power are sorted alphabetically"""
	
	if len(varList) <= 1:
		return varList
	
	power = 0 
	maxPower = 0
	highest = [] #A list of all variables with the highest power
	
	for var in varList:
		if var != "":
			power = (re.findall(r'\d+', var))
			power = sum(map(int, power))
			if power > maxPower:
				maxPower = power
				highest = []
				highest.append(var)
			elif power == maxPower:
				highest.append(var)
		
	retList = highest
		
	leftovers = list(set(varList) - set(retList)) 
	return  sorted(retList) + sortCanon(leftovers)

	
def inputMode():
	"""Prompt user for equation, and print that equation in canonical form"""
	while 1:
		equationInput = input("Enter equation: ")
		print(convertToCanon(equationInput))
		
def fileMode():
	"""Prompt user for file containing equations. Create a file with those equations in canonical form"""
	filepath = input("Please enter filepath: ")
	inputFile = open(filepath)
	outputFile = open("output.out", "w")

	for line in inputFile:
		line = line.rstrip("\n")
		outputFile.write(convertToCanon(line) + "\n")
	
	print("complete")	
	inputFile.close()
	outputFile.close()


if __name__ == "__main__":
	
	choice = -1
	while choice != "1" and choice != "2":
		choice = input("Enter 1 for input mode, 2 for for file mode: ")
		try:
			if int(choice) == 1:
				mode = 1
				inputMode()
			elif int(choice) == 2:
				mode = 2
				fileMode()
			else:
				print("Invalid selection")
		except ValueError:
			print("Invalid selection")
