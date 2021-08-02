import os
import time
import sys
soru = input("Important Information and Reminder Information and programs in all repositories are created for testing purposes. Any legal responsibility belongs to the person or organization that uses it? Y/N:")
if soru.lower().startswith("y"):
    pass
else:
    print("is ending....")
    sys.exit()
ipadresi = input("target ip :")
print("turn off q")
os.system("clear")
time.sleep(4)
def cleartraces():
    os.system("rm necessary.txt")
    print("see you .")
def scanning(ip):
    global a
    os.system("nmap -n -sV -p- {}".format(ip))
def explanation():
    a = """
    

 ███

███████╗██╗  ██╗██████╗ ██╗   ██╗██╗     ███████╗███████╗██████╗ 
██╔════╝╚██╗██╔╝██╔══██╗██║   ██║██║     ██╔════╝██╔════╝╚════██╗
█████╗   ╚███╔╝ ██████╔╝██║   ██║██║     ███████╗█████╗   █████╔╝
██╔══╝   ██╔██╗ ██╔═══╝ ██║   ██║██║     ╚════██║██╔══╝  ██╔═══╝ 
███████╗██╔╝ ██╗██║     ╚██████╔╝███████╗███████║███████╗███████╗
╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝
                                                                 
starting....

    """
    print(a)
    time.sleep(1)
    print("""
     Automatically finds and exploits nmap scripts..""")
def findexploitanduse():
    global ipadresi
    bul = input("Servis Name:")
    if bul =="q":
        sys.exit()
    else:
        pass



    a = open("necessary.txt","a")
    de = os.listdir("/usr/share/nmap/scripts")
    time.sleep(3)
    os.system("clear")
    for yazdır in de:
        a.write("{} \n".format(yazdır))
    print("""Available Scripts:""")
    os.system("grep {} necessary.txt".format(bul))
    secim = input("Do You Want to Apply y/n:")

    secim = secim.lower()
    if secim.startswith("y"):
       ismial = input(":The Name of The Script You Want to Use:")

       os.system(f"nmap -n -sV -p- {ipadresi} --script {ismial[:-4]}")


explanation()
scanning(ipadresi)
findexploitanduse()
time.sleep(8)
cleartraces()
