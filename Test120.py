# 120-Multiplication test, Metapontum.
# September 2018 Philippe Martinet, Tatyana Magnusson.
# 120 uppgifter från Erik Johansson, Öckerö
# 2018-09-24 Version 1.0
   

import time
import re

test_120 = [
[6,6],[8,4],[6,3],[2,2],[5,9],[7,5],
[3,7],[9,9],[8,6],[6,7],[3,8],[9,4],
[4,8],[6,4],[7,7],[9,3],[4,6],[6,8],
[3,9],[8,8],[9,6],[4,7],[5,8],[8,3],
[6,9],[7,3],[4,9],[3,6],[7,4],[10,10],
[7,7],[8,6],[1,5],[8,8],[6,9],[0,7],
[5,3],[9,9],[8,7],[7,3],[3,2],[4,8],
[6,7],[8,7],[7,3],[3,2],[4,8],[9,7],
[3,8],[4,7],[6,8],[3,6],[5,9],[4,6],
[9,6],[3,0],[7,6],[8,4],[3,7],[5,5],
[6,0],[7,6],[1,1],[4,6],[8,7],[7,3],
[9,9],[8,6],[6,3],[6,9],[8,8],[9,6],
[7,4],[3,8],[7,9],[6,5],[9,8],[6,6],
[8,9],[6,7],[2,4],[9,4],[7,7],[4,8],
[3,9],[7,8],[6,8],[9,7],[1,4],[9,2],
[7,4],[9,6],[7,8],[9,9],[7,6],[8,3],
[6,6],[4,9],[8,8],[4,7],[9,3],[7,7],
[7,9],[4,6],[8,4],[9,7],[8,6],[7,3],
[6,4],[9,8],[6,7],[8,9],[3,7],[6,9],
[6,8],[2,0],[8,7],[6,3],[7,2],[10,1]]


results = []

def test():
	nb_wrong = 0
	nb_correct = 0
	n=0
	stat = []
	res = []
	t1 = time.time()
	for v in test_120:
		a = v[0]
		b = v[1]
		n += 1
		ans = input("{}x{} = ".format(a,b))
		t3 = time.time()
		if(ans == "q"):
			break
			
		tmp = t3-t1
		mn = int(tmp/60.0)
		sec = int(tmp - mn*60)
		#print(tmp)
		tid = "{}:{}".format(mn,sec)
		if(int(ans) == a*b):
			tmp = "   Rätt!! {}x{} = {} Tid: {}".format(a,b,a*b,tid)
			print(tmp)
			results.append([1,a,b,a*b,tid])
			fileout.write(tmp+"\n")
			nb_correct += 1
		else:
			tmp = "   {}x{} != {} Fel!! Tid: {}".format(a,b,int(ans),tid)
			print(tmp)
			results.append([-1,a,b,int(ans),tid])
			fileout.write(tmp+"\n")
			if(a*b != 0 and a != 1 and b != 1):
				stat.append(max(a,b))
		
			nb_wrong += 1
			
	t2=time.time()
	tmp = t2-t1
	mn = int(tmp/60.0)
	sec = int(tmp - mn*60)

	tid = "{}:{}".format(mn,sec)
	success = nb_correct*1.0/n*100.0
	tmp = "Rätt: {0} ({1:3.1f}%) Fel: {2} ({3:3.1f}%) Tid: {4}".format(nb_correct,success,nb_wrong,100.0-success,tid)
	print(tmp)
	results.append([nb_correct,success,nb_wrong,100.0-success,tid])
	fileout.write(tmp+"\n")
	
	if(success <= 90.0):
		
		stat.sort(reverse=True)
		#print(stat)
		m1 = m2 = m3 = 0
		for m in range(0,12):
			res.append(stat.count(m))
			
		m1 = res.index(max(res))
		#print(res)
		res[m1] = -1
		m2 = res.index(max(res))
		#print(res)
		res[m2] = -1
		m3 = res.index(max(res))
		#print(m1,m2,m3)
		
		# for i in range(len(stat)):
			# n = 0
			# for j in range(len(stat)):
				# if(stat[j] == stat[i]):
					# n += 1
			# res.del()
			# res.append([stat[i],n])
			
		if( m1 >= 2 and m2 < 2  and m3 < 2):
			tmp = "Du behöver öva multiplikationstabellen {} varje dag!!".format(m1)
			results.append([m1])
		if(m2 >= 2 and m1 >= 2 and m3 < 2):
			tmp = "Du behöver öva multiplikationstabellen {} och {} varje dag!!".format(m1,m2)
			results.append([m1,m2])
		if (m3 >= 2 and m1 >= 2 and m3 >= 2):
			tmp = "Du behöver öva multiplikationstabellen {}, {} och {} varje dag!!".format(m1,m2,m3)
			results.append([m1,m2,m3])
		print(tmp)
		fileout.write(tmp+"\n")
		
	else:
		
		tmp = "Du kan verkligen multiplicera!! Du är klart med multiplikationer :-)"
		print(tmp)
		fileout.write(tmp+"\n")
		results.append("Klart!")
		
		

namn = input("Skriv ditt namn: ")		
datum = input("Datum: ")

p = re.compile('(\\\|\/|-)')
date = p.sub('_',datum)

fileout = open(namn+"_"+date,"w")
fileout.write(namn+"\n")
fileout.write(datum+"\n")
fileout.write("\n")

results.append(namn)
results.append(datum)

print("Hur många uppgifter klarar du på 5 min?")

test()
fileout.write(str(results))

print("Resultat sparade i filen: " + namn + "_"+date)
print("Press Q och 'Enter' fär att avsluta testet")

fileout.close()

ans = input()
if(ans == "q"):
	exit()
elif(ans == "r"):
	test()
input()
