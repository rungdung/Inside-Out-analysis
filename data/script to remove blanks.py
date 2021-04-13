
f=open("transcript.txt","r")
mystr=list(f)
mystr.split('\n')
[line for line in mystr.split('\n') if line.strip() != '']

