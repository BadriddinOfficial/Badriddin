import os, sys
def clearscreen():
    if sys.platform == "linux2":
        os.system("clear")
    elif sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
        
clearscreen()
banner = """\033[1;31m _     _         ______               
   ___          __    _    __   ___    
  / _ )___ ____/ /___(_)__/ /__/ (_)__ 
 / _  / _ `/ _  / __/ / _  / _  / / _ \
/____/\_,_/\_,_/_/ /_/\_,_/\_,_/_/_//_/                                       
 	  """"""\033[1;32mcreated by @Badriddin_Official"""
print(banner)
