import paramiko
import subprocess, os, socket
hostname = "google.com"
output_file = "output.txt"
import sys

print('Number of arguments:', len(sys.argv), 'arguments')
print('Argument List:', str(sys.argv))


# Initializing required variables
pkey = '~/.ssh/id_rsa'
# Paramiko.SSHClient can be used to make connections to the remote ssh server
ssh = paramiko.SSHClient()
privatekeyfile = os.path.expanduser(pkey)
mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)



def exec_commands(ssh):
    command_0 = "who"
    _, stdout, stderr = ssh.exec_command(command_0)
    if stdout:
        ssh_cmd_output = stdout.read()
    elif stderr:
        ssh_cmd_output = stderr.read()
    print(ssh_cmd_output)

def ssh_connect(IP, UserName):
    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(IP, username=UserName, pkey=mykey, timeout=5, allow_agent=True, look_for_keys=True)
        #ssh.connect(IP, username=UserName,password="12345678", pkey=mykey, timeout=5, allow_agent=True, look_for_keys=True)
        exec_commands(ssh)
        ssh.close()

    except paramiko.AuthenticationException:
        status = "Authentication failed, please verify your credentials"
    except paramiko.SSHException as sshException:
        status = "Could not establish SSH connection: " + str(sshException)
    except socket.timeout:
        status = "Connection timed out"
    except Exception as exception:
        status = "Exception in connecting because " + str(exception)
    else:
        status = "success"



def command_executor(command):
    """ Executes the command and returns the output """

    try:
        with open(output_file, "a") as file:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)  # Execute the command
            process.wait()
            stdout, stderr = process.communicate()

            if stdout:
                output = stdout.decode("ASCII")
            elif stderr:
                output = stderr.decode("ASCII")

            file.write(output)

            print("output:\n",output)
    except Exception as Error:
        print("Command Executor - Execution failed for the command :: ", command)
        print("Command Executor - Error : ", Error)


print("command executor")

traceroute =  "traceroute " + hostname
ping = "ping " + hostname + " -c 2"
commands = [traceroute, ping ]
for command in commands:
    command_executor(command)




"""
import paramiko


# Initializing required variables
pkey = '~/.ssh/id_rsa'

# Paramiko.SSHClient can be used to make connections to the remote ssh server
ssh = paramiko.SSHClient()
privatekeyfile = os.path.expanduser(pkey)
mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)


def ssh_connect(IP, UserName, os):
    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(IP, username=UserName, pkey=mykey, timeout=5, allow_agent=True, look_for_keys=True)
        exec_commands(ssh, IP, UserName)
        ssh.close()

    except paramiko.AuthenticationException:
        status = "Authentication failed, please verify your credentials"
        conn_status_list.extend([IP, UserName, status])
    except paramiko.SSHException as sshException:
        status = "Could not establish SSH connection: " + str(sshException)
        conn_status_list.extend([IP, UserName, status])
    except socket.timeout:
        status = "Connection timed out"
        conn_status_list.extend([IP, UserName, status])
    except Exception as exception:
        status = "Exception in connecting because " + str(exception)
        conn_status_list.extend([IP, UserName, status])
    else:
        conn_status_list.extend([IP, UserName, 'success'])

    return conn_status_list
    
    
def exec_commands():
    command_0 = "who"
    _, stdout, stderr = ssh.exec_command(command_0)
    if stdout:
        ssh_cmd_output = stdout.read()
    elif stderr:
        ssh_cmd_output = stderr.read()


"""