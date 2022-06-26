#!/usr/bin/python3
import subprocess

print('a. Outputs the current user name:')
subprocess.run('whoami')

print('b. Outputs the current work directory:')
subprocess.run(['pwd', ])

# print('c. Creates directory with name "dz1" in the current directory:')
# subprocess.run('mkdir dz1', shell=True)
#
# print('d. Creates files with name "dd-mm-yyyy.log" in the directory "dz1":')
# create_files_command = ['touch']
# file_names = ['./dz1/' + f'{i:0{2}}' + '-06-2022.log' for i in range(1, 31)]
# create_files_command.extend(file_names)
# subprocess.run(create_files_command)

print('e. Changes the owner for directory "dz1" on root:')
subprocess.run('', shell=True)
result = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(f'stdout: {result.stdout}')
