def categorize(split_list) : 

	lexical_map = {

		"p" : 1,
		"q" : 1,
		"r" : 1,
		"s" : 1,
		"not" : 2, 
		"and" : 3, 
		"or" : 4,
		"xor" : 5,
		"if" : 6,
		"then" : 7,
		"iff" : 8,
		"(" : 9,
		")" : 10

	}

	result = []
	for word in split_list : 
		if (lexical_map.get(word) != None) :
			result.append(lexical_map.get(word))
		else : 
			result.append(lexical_map.get(word, "Error"))
			break

	return result




def tokenize(text) :


	result_list = []
	i = 0 
	while i < len(text) :
		if (text[i] == 'p' or text[i] == 'q' or text[i] == 'r' or text[i] == 's') : 
			temp = (text[i])

		elif text[i] == 'n' :
			try : 
				if text[i+1] == 'o' and text[i+2] == 't':
					temp = (text[i] + text[i+1] + text[i+2])
					i += 2 
				else : 
					result_list.append('Error')
					break
			except : 
				result_list.append('Error')
				break


		elif text[i] == 'x' :
			try : 
				if text[i+1] == 'o' and text[i+2] == 'r' :
					temp = (text[i] + text[i+1] + text[i+2])
					i += 2 
				else : 
					result_list.append('Error')
					break
			except : 
				result_list.append('Error')
				break

		elif text[i] == 'o' :
			try : 
				if text[i+1] == 'r' :
					temp = (text[i] + text[i+1])
					i += 1
				else : 
					result_list.append('Error')
					break
			except : 
				result_list.append('Error')
				break

		elif text[i] == 'a' :
			try : 
				if text[i+1] == 'n' and text[i+2] == 'd' :
					temp = (text[i] + text[i+1] + text[i+2])
					i += 2 
				else : 
					result_list.append('Error')
					break
			except : 
				result_list.append('Error')

				break
		elif text[i] == 't' :
			try : 
				if text[i+1] == 'h' and text[i+2] == 'e' and text[i+3] == 'n':
					temp = (text[i] + text[i+1] + text[i+2] + text[i+3])
					i += 3
				else : 
					result_list.append('Error')
					break
			except : 
				result_list.append('Error')
				break

		elif text[i] == 'i' : 
			try : 
				if text[i+1] == 'f' and text[i+2] == 'f' and text[i+3] == ' ': 
					temp = (text[i] + text[i+1] + text[i+2])
					i += 2
				elif text[i+1] == 'f' : 
					temp = (text[i] + text[i+1])
					i += 1
				else : 
					result_list.append('Error')
					break
			except : 
				try :
					if text[i+1] == 'f' :
						temp = (text[i] + text[i+1])
						break
					else : 
						result_list.append('Error')
						break
				except:
					result_list.append('Error')
					break

		elif text[i] == '(' or text[i] == ')' : 
			temp = (text[i])


		try : 
			if text[i+1] == ' ':
				result_list.append(temp) 
				i += 2 
			elif text[i+1] == ')':
				result_list.append(temp) 
				i += 1
			elif text[i] == '(':
				result_list.append(temp) 
				i += 1

			else : 
				result_list.append('Error')
				break
			
		except : 
			if (temp != None) : 
				result_list.append(temp)
				break 
			else :
				break

	return result_list


def parse(token_lexic) :
	err = False
	result = []
	state = "i"
	result.append("#")
	state = "p"
	result.append("S")  # 
	state = "q"         # #RRR
	symbol = token_lexic[0]
	while result[-1] != "#" and not err: 
		if (result[-1] == "S") :
			if symbol == 1 :
				result.pop()
				result.append("R")
				result.append("1")	
			elif symbol == 2 : 
				result.pop()
				result.append("R")
				result.append("S")
				result.append("2")
			elif symbol == 6 :
				result.pop()
				result.append("R")
				result.append("S")
				result.append("7")
				result.append("S")
				result.append("6")
			elif symbol == 9 : 
				result.pop()
				result.append("R")
				result.append("10")
				result.append("S")
				result.append("9")
			else : 
				err = True
				break
			
		elif (result[-1] == "R") : 
			if symbol == 3 : 
				result.pop()
				result.append("S")
				result.append("3")
			elif symbol == 4 : 
				result.pop()
				result.append("S")
				result.append("4")
			elif symbol == 5 : 
				result.pop()
				result.append("S")
				result.append("5")
			elif symbol == 8 : 
				result.pop()
				result.append("S")
				result.append("8")
			else : 
				result.pop()
		elif (result[-1] == "1"):
			if symbol == 1:

				result.pop()
				token_lexic.pop(0)
			else : 
				err = True
				break
		elif (result[-1] == "2"):
			if symbol == 2:
				result.pop()
				token_lexic.pop(0)
			else : 
				err = True
				break
		elif (result[-1] == "3"):
			if symbol == 3:
				result.pop()
				token_lexic.pop(0)
			else : 
				err = True
				break
		elif (result[-1] == "4"):
			if symbol == 4:
				result.pop()
				token_lexic.pop(0)
			else : 
				err = True
				break
		elif (result[-1] == "5"):
			if symbol == 5:
				result.pop()
				token_lexic.pop(0)
			else : 
				err = True
				break
		elif (result[-1] == "6"):
			if symbol == 6:
				result.pop()
				token_lexic.pop(0)
			else : 
				err = True
				break
		elif (result[-1] == "7"):
			if symbol == 7:
				result.pop()
				token_lexic.pop(0)
			else : 
				err = True
				break
		elif (result[-1] == "8"):
			if symbol == 8:
				result.pop()
				token_lexic.pop(0)
			else : 
				err = True
				break
		elif (result[-1] == "9"):
			if symbol == 9:
				result.pop()
				token_lexic.pop(0)
			else : 
				err = True
				break
		elif (result[-1] == "10"):
			if symbol == 10:
				result.pop()
				token_lexic.pop(0)
			else : 
				err = True
				break
	
		print(token_lexic)
		print(result)

		if (len(token_lexic) != 0) :
			symbol = token_lexic[0]
		
	if (err) :
		print ("Not Valid")
	else :
		print("Valid")
		

if __name__ == "__main__" : 

	# 2 1 3 9 6 1 5 1 7 9 1 5 9 1 3 2 9 1 3 1 10 10 10 10
	text_1 = "p and q or r"
	text_2 = "if p then (not q s)"
	text_3 = "p xor (q and not (p and q))"
	text_4 = "(p and q ifg (r or s))"
	test = "p q r"

	tokenized_text = tokenize(test)
	categorized_text = categorize(tokenized_text)
	print(tokenized_text)
	print(categorized_text)
	if (categorized_text[-1] != "Error") :
		parse(categorized_text)
	else :
		print("Not Valid")


	



	
