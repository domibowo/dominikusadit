from collections import Counter 

def groupStrings(input): 
	dict={} 
	
	for kata in input: 
		kataDict=Counter(kata)

		huruf = kataDict.keys()
		huruf = sorted(huruf)		
		huruf = ''.join(huruf)
		
		if huruf in dict.keys():
			dict[huruf].append(kata) 
		else: 
			dict[huruf]=[] 
			dict[huruf].append(kata)
    
	for (huruf,value) in dict.items(): 
		print (','.join(dict[huruf]))
		
if __name__ == "__main__": 
        input=["cat", "listen", "code", "act", "silent", "tac"] 
        groupStrings(input) 
