import sys
import subprocess
import argparse

def run_id_ssh(ip_addresses, username, key_file):
    with open(ip_addresses) as file:
        for ip in file:
            clr_ip = ip.strip()
            try:
                subprocess.check_output(
                    ['proxychains', '-q', 'ssh', '-o', 'StrictHostKeyChecking=no', '-o', 'BatchMode=yes', '-i', key_file, f'{username}@{clr_ip}', 'id'], 
                    universal_newlines=True,
                    stderr=subprocess.DEVNULL
                )
                print(clr_ip)
            except subprocess.CalledProcessError:
                pass

def main():
    parser = argparse.ArgumentParser(description='Выполнение команды `id` на удалённых хостах через SSH.')
    parser.add_argument('ip_addresses', help='Файл с IP-адресами хостов')
    parser.add_argument('username', help='Имя пользователя для SSH')
    parser.add_argument('key_file', help='Файл с приватным ключом для SSH')

    args = parser.parse_args()

    run_id_ssh(args.ip_addresses, args.username, args.key_file)

if __name__ == "__main__":
    main()
