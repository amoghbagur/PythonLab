def countwords(fn):
	with open(fn) as f:
		l1=f.read().split()
		d1={}
		for i in range(len(l1)):
			d1.update({l1[i]:i})
		return len(d1.keys())
print("No. of words in the file:",countwords("endgame.txt"))
