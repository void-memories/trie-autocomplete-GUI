from Tkinter import *


class TrieNode(): 
	def __init__(self): 
		
		self.children = {} 
		self.last = False

class Trie(): 
	answer=[]
	def __init__(self): 
		
		self.root = TrieNode() 
		self.word_list = [] 

	def formTrie(self, keys): 
		
		for key in keys: 
			self.insert(key)  

	def insert(self, key): 
		
		node = self.root 

		for a in list(key): 
			if not node.children.get(a): 
				node.children[a] = TrieNode() 

			node = node.children[a] 

		node.last = True

	def search(self, key): 
		
		node = self.root 
		found = True

		for a in list(key): 
			if not node.children.get(a): 
				found = False
				break

			node = node.children[a] 

		return node and node.last and found 

	def suggestionsRec(self, node, word): 
		
		if node.last: 
			self.word_list.append(word) 

		for a,n in node.children.items(): 
			self.suggestionsRec(n, word + a) 

	def printAutoSuggestions(self, key): 
		
		node = self.root 
		not_found = False
		temp_word = '' 

		for a in list(key): 
			if not node.children.get(a): 
				not_found = True
				break

			temp_word += a 
			node = node.children[a] 

		if not_found: 
			return 0
		elif node.last and not node.children: 
			return -1

		self.suggestionsRec(node, temp_word) 
		#output.delete(1.0, END)
		for s in self.word_list:
			output.insert(END,s+ '\n')
		return 1
	


key=""

root = Tk()
root.geometry('500x500')
root.title("TRIE AUTOCOMPLETE")

label_0 = Label(root, text="TRIE AUTOCOMPLETE",width=20,font=("bold", 35))
label_0.pack(side=TOP, padx=15, pady=15)


label_1 = Label(root, text="Enter The Word",width=20,font=("bold", 10))
label_1.pack(side=TOP)

entry_1 = Entry(root)
entry_1.pack(side=TOP, padx=10, pady=0)

var = IntVar()



def rex():
	output.delete(1.0, END)

keys=[]



with open('dict2.txt', 'r') as filehandle:
	for line in filehandle:
		currentPlace = line[:-1]
		keys.append(currentPlace)




def butt_press():
	t = Trie() 
	t.formTrie(keys) 
	rex()
	key=entry_1.get()
	comp = t.printAutoSuggestions(key)

	if comp == -1: 
		output.insert(END,entry_1.get())
	elif comp == 0: 
		aas="No Match!!!"
		output.insert(END,aas)



def addd():
	rex()
	output.insert(END,"Successfully Added.")
	tempp=[]
	cf=entry_1.get()
	tempp.append(cf)
	with open("dict2.txt", "a") as myfile:
		myfile.write('\n'+ cf)
		keys.append(cf)

def info():
	about="A Creation Of :- "
	toplevel = Toplevel()
	label1 = Label(toplevel, text=about, height=0, width=100)
	space = Label(toplevel, text="", height=0, width=100)
	label2 = Label(toplevel, text="Naman Anand", height=0, width=100)
	label3 = Label(toplevel, text="Kirti Kunj Bajpai", height=0, width=100)
	label4 = Label(toplevel, text="Himanshu Mishra", height=0, width=100)
	label5 = Label(toplevel, text="Kiran Jarali", height=0, width=100)

	label1.pack()
	space.pack()
	label2.pack()
	label3.pack()
	label4.pack()
	label5.pack()


Button(root, text='Submit',width=20,bg='brown',fg='white',command=butt_press).pack(side=TOP)

output=Text(root,width=30,height=10,background='light grey')
output.pack(side=TOP,padx=5,pady=5)


Button(root, text='Add To The Dictionary',width=20,bg='brown',fg='white',command=addd).pack(side=TOP)
Button(root, text='Clear Screen',width=20,bg='brown',fg='white',command=rex).pack(side=TOP)
Button(root, text='About Us',width=20,bg='brown',fg='white',command=info).pack(padx=20,side=TOP)

root.mainloop()