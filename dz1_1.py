#!/usr/bin/python3
import random
import subprocess

print('a. Outputs the current user name:')
subprocess.run('whoami')

print('b. Outputs the current work directory:')
subprocess.run(['pwd', ])

print('c. Creates directory with name "dz1" in the current directory:')
subprocess.run('mkdir dz1', shell=True)

print('d. Creates files with name "dd-mm-yyyy.log" in the directory "dz1":')
create_files_command = ['touch']
file_names_1 = ['./dz1/' + f'{i:0{2}}' + '-06-2022.log' for i in range(1, 31)]
create_files_command.extend(file_names_1)
subprocess.run(create_files_command)

print('e. Changes the owner for directory "dz1" on root:')
subprocess.run('sudo chown -R root ./dz1', shell=True)
result = subprocess.run(['ls', '-ld', './dz1'], capture_output=True, text=True)
print(f'stdout: {result.stdout}')

print('f. Deletes five random files in directory "dz1":')
result = subprocess.run(['ls', 'dz1'], capture_output=True, text=True)
files = result.stdout.split('\n')
files.remove('')
delete_files_command = ['rm']
file_names_2 = ['./dz1/' + random.choice(files) for i in range(5)]
delete_files_command.extend(file_names_2)
print(delete_files_command)
subprocess.run(delete_files_command)
