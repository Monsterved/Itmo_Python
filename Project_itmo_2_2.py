Python 2.7.18 (tags/v3.10.4:9d38120, Apr 10 2022, 13:57:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import paramiko
router_ip = "192.168.1.1"
router_username = "Administrator"
router_password = "Qwerty123"
ssh = paramiko.SSHClient()
SyntaxError: invalid syntax
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(router_ip, username=router_username, password=router_password, look_for_keys=False )
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("copy running-config tftp://192.168.1.12")
