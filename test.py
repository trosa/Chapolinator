from chapolinator import Chapolinator

chapo = Chapolinator()
for x in range(100):
	talk = chapo.talk()
	print talk.decode('latin-1').encode('utf-8'), len(talk.split(' ')), len(talk)
