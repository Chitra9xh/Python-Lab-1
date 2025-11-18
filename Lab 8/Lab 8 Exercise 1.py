text=input("Enter a line of text: ").lower().split()
freq={}
for w in text: freq[w]=freq.get(w,0)+1
for k,v in freq.items(): print(k,":",v)
