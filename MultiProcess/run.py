from subprocess import Popen, PIPE

p = Popen('./test1.py', stdin=PIPE, stdout=PIPE)
p.stdin.write('hello\n')
print p.stdout.readline()
