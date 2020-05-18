import subprocess,time,speedtest,os
from termcolor import cprint

os.system("clear")

print('''

	INTERNET SPEED TEST

	Code:gurkan._guler

	'''.center(60,' '))




sptest = subprocess.check_output(["speedtest-cli","--bytes"]).decode("utf-8").split("\n")



cprint("[+] PLEASE WAIT ","red")

for data in sptest:
	time.sleep(0.5)
	cprint("# ",end=" ",flush=True)
	print(data)
	