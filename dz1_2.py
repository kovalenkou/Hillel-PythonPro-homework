#!/usr/bin/python3
import subprocess

print('a. Copy file "dz1_1.py" to "dz1_run.py":')
subprocess.run('cp dz1_1.py dz1_run.py', shell=True)

print('b. Add access for the file "dz1_run.py" to run it from bash:')
subprocess.run('chmod u+x dz1_run.py', shell=True)
result = subprocess.run(['ls', '-ld', 'dz1_run.py'], capture_output=True, text=True)
print(f'stdout: {result.stdout}')

print('c. Change access for the file "dz1_run.py":')
subprocess.run('chmod u=rx,g=,o= dz1_run.py', shell=True)
result1 = subprocess.run(['ls', '-ld', 'dz1_run.py'], capture_output=True, text=True)
print(f'stdout: {result1.stdout}')

print('d. Run the file "dz1_run.py":')
subprocess.call('./dz1_run.py', shell=True)
