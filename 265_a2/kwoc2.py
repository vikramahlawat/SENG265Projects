import sys,getopt

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
def get_exception(file_name):
	file = open(file_name,"r")
	li =[]
	for line in file:
		for word in line.split():
			li.append(word.upper())
	return li
		
def invalid(word,except_words):
	if word in except_words:
		return True;
	if(word.find("--")>0):
		return True;
	if(word[len(word)-1]=="-"):
		return True;
		
	return False;
def write_file(dic,inp_file,length):
	out_file = open("out"+inp_file[2:],"x")
	                                           
	for key in sorted(dic):
		temp = dic[key]
		for value in temp:
			#print(key.upper().ljust(length),value.split("_")[1],"({})".format(value.split("_")[0]))
			out_file.write(key.upper().ljust(length)+value.split("_")[1]+"({})".format(value.split("_")[0])+"\n")
	
		
def main():
	dic = {};
	
	inp_file ,lang_file = split(sys.argv[1:])
	except_words = get_exception(lang_file)	
	length=0;
	file = open(inp_file,"r")
	line_no=1;
	for line in file:
		for word in line.split():
			word=word.upper()
			if invalid(word,except_words):
				continue;
			if(length<len(word)):
				length=len(word) 
			if word not in dic:		
				dic[word]=[str(line_no)+"_"+line.rstrip("\n")]
			else:
				dic_values=dic.get(word)
				boo = False;
				val=0
				for t in dic_values:
					tmp_line_no = t.split("_")[0]
					if(int(tmp_line_no) == line_no):
						boo=True;
						break;
					val+=1;
				if(boo):
					dic_values[val] = (str(line_no)+"*_"+line.rstrip("\n"))
				else:
					dic_values.append(str(line_no)+"_"+line.rstrip("\n"))
		line_no+=1;
	length+=2;
	write_file(dic,inp_file,length);
	
	
if  __name__ == "__main__":
	main()

