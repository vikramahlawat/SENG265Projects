
def split(argv):
	inp=""
	lang=""
	if(argv[0]=='-e'):
		lang = argv[1]
		inp = argv[2]
	else:
		inp=argv[0]
		lang = argv[2]
	return inp,lang




import sys
import re

PATTERN = r'''^((\w|\-)+$'''

class KWOC:

	def __init__(self, filename, exceptions):
		self.filename = filename
		self.exception_file = exceptions


	def get_exception(self,file_name):
		li =[]
		if(file_name==None):
			return li
		file = open(file_name,"r")
		
		for line in file:
			for word in line.split():
				li.append(word.upper())
		return li
		
	def invalid(self,word,except_words):
		if word in except_words:
			return True;
		if(word.find("--")>0):
			return True;
		if(word[len(word)-1]=="-"):
			return True;
		
		return False;
	def trim_word(self,word):
		punc = ['"',',','.',':',';','!','?']
		out="";
		for i in word:
			if i not in punc:
				out+=i; 
		return out
	#def write_file(self,dic,inp_file,length):
		#out_file = open("out"+inp_file[2:],"x")
		
		#for key in sorted(dic):
		#	temp = dic[key]
		#	for value in temp:
				
		#		print key.upper().ljust(length),value.split("_")[1],"({})".format(value.split("_")[0])
				#out_file.write(key.upper().ljust(length)+value.split("_")[1]+"({})".format(value.split("_")[0])+"\n")
	
		

	
	





	def concordance(self):
		dic = {};
	
		inp_file =  self.filename
		lang_file = self.exception_file
		except_words = self.get_exception(lang_file)	
		length=0;
		file = open(inp_file,"r")
		line_no=1;
		for line in file:
			for word in line.split():
				word=word.upper()
				word=self.trim_word(word)
				if self.invalid(word,except_words):
					continue;
				if(length<len(word)):
					length=len(word) 
				if word not in dic:		
					dic[word]=[str(line_no)+"_"+line.rstrip("\n")]
					#print(dic[word],word)
				else:
					dic_values=dic.get(word)
					#print(dic_values)
					boo = False;
					val=0
					for t in dic_values:
						#print(t)
						tmp_line_no = t.split("_")[0]
						if(tmp_line_no[len(tmp_line_no)-1]=='*'):
							tmp_line_no=tmp_line_no[:len(tmp_line_no)-1]
						if(int(tmp_line_no) == line_no):
							boo=True;
							break;
						val+=1;
					if(boo):
						dic_values[val] = (str(line_no)+"*_"+line.rstrip("\n"))
					else:
						dic_values.append(str(line_no)+"_"+line.rstrip("\n"))
			line_no+=1;
		length+=1;
		
		list2 = []
		for key in sorted(dic):
			temp = dic[key]
			for value in temp:
				str2 =''
				str2 = str2 +(key.upper().ljust(length+1)+value.split("_")[1]+" "+"({})".format(value.split("_")[0]))
				
				list2.append(str2)
		
		return list2	
