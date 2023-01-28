import pymysql
import os
from dotenv import load_dotenv
import time
from colorama import init
from colored import attr
from colorama import Fore, Back, Style
from termcolor import colored

# load environment file and set variables for connection
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# set connection variable
connection = pymysql.connect(
     host,
     user,
     password,
     database
)

# set cursor variable
cursor = connection.cursor()

def main_menu():
    # Clear Terminal so menu is static
    # prints menu with options
    os.system('clear')
    print(colored("\033[31m"+"._________________________________________________________________________."))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                                "+Fore.GREEN+"Main Menu"+Fore.RED +"                                |"))
    print(colored("\033[31m"+"|_________________________________________________________________________|"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                            "+Fore.GREEN+"["+Fore.BLUE+"1"+Fore.GREEN+"] Dump All"+Fore.RED +"                                 |"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                            "+Fore.GREEN+"["+Fore.BLUE+"2"+Fore.GREEN+"] Dump Gamertags"+Fore.RED +"                           |"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                            "+Fore.GREEN+"["+Fore.BLUE+"3"+Fore.GREEN+"] Dump IPs"+Fore.RED +"                                 |"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                            "+Fore.GREEN+"["+Fore.BLUE+"4"+Fore.GREEN+"] Search"+Fore.RED +"                                   |"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                            "+Fore.GREEN+"["+Fore.BLUE+"5"+Fore.GREEN+"] Admin Options"+Fore.RED +"                            |"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                            "+Fore.GREEN+"["+Fore.BLUE+"6"+Fore.GREEN+"] Credits"+Fore.RED +"                                  |"))
    print(colored("\033[31m"+"|_________________________________________________________________________|"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                                "+Back.RED+"[0"+Fore.RED+"] Exit"+Back.BLACK+"                                 |"))
    print(colored("\033[31m"+"|_________________________________________________________________________|"))
    print('')
    print(colored(Fore.GREEN+"                              Enter an option"))
    option = int(input('                                  --> '))
    print("")
    if option == 0:
        print("                           Closing Connections...")
        cursor.close()
        connection.close()
        time.sleep(3)
        print("                                 Exiting...")
        time.sleep(1.3)
        print("")
        exit()
    elif option == 1:
        print("                            Generating Results...")
        time.sleep(4)
        cursor.execute("SELECT ID, gamertag, ip FROM Yutes;")
        for items in cursor:
            print(items)
        input(colored('                           '+Back.RED+'Press Enter To Continue'))
        main_menu()
    elif option == 2:
        print("                            Generating Results...")
        time.sleep(4)
        cursor.execute("SELECT ID, gamertag FROM Yutes;")
        for items in cursor:
            print(items)
        input(colored('                           '+Back.RED+'Press Enter To Continue'))
        main_menu()
    elif option == 3:
        print("                            Generating Results...")
        time.sleep(4)
        cursor.execute("SELECT ID, ip FROM Yutes;")
        for items in cursor:
            print(items)
        input(colored('                           '+Back.RED+'Press Enter To Continue'))
        main_menu()
    elif option == 4:
        search_menu()
    elif option == 5:
        admin_menu()
    elif option == 6:
        credits_menu()
    else:
        print(colored("                              "+Back.RED+"Input Invalid:"+Back.BLACK+f" {option}"))
        time.sleep(3)
        main_menu()

def credits_menu():
    # Clear Terminal so menu is static
    # prints credits menu with exit to main option
    os.system('clear')
    print(colored("\033[31m"+"._________________________________________________________________________."))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                              "+Fore.GREEN+"Credits Menu"+Fore.RED +"                               |"))
    print(colored("\033[31m"+"|_________________________________________________________________________|"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|    "+Fore.GREEN+"["+Fore.BLUE+"Welcome to the most over engineered collection of player data"+Fore.GREEN+"]"+Fore.RED +"      |"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                  "+Fore.GREEN+"["+Fore.BLUE+"Simply select an option in main menu"+Fore.GREEN+"]"+Fore.RED +"                 |"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                    "+Fore.GREEN+"["+Fore.BLUE+"This tool was made by "+Fore.YELLOW+"SpiceySec"+Fore.GREEN+"]"+Fore.RED +"                    |"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                             "+Fore.GREEN+"["+Fore.BLUE+"Version"+Fore.GREEN+" 1.0.0"+Fore.GREEN+"]"+Fore.RED +"                             |"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                      "+Fore.GREEN+"["+Fore.BLUE+"To exit this screen press "+Fore.RED+"0"+Fore.GREEN+"]"+Fore.RED +"                      |"))
    print(colored("\033[31m"+"|_________________________________________________________________________|"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                                "+Back.RED+"[0"+Fore.RED+"] Main Menu"+Back.BLACK+"                            |"))
    print(colored("\033[31m"+"|_________________________________________________________________________|"))
    print('')
    print(colored(Fore.GREEN+"                              Enter an option"))
    option = int(input('                                  --> '))
    print("")
    if option == 0:
        main_menu()
    else:
        print(colored("                              "+Back.RED+"Input Invalid:"+Back.BLACK+f" {option}"))
        time.sleep(3)
        credits_menu()

def search_menu():
    os.system('clear')
    print(colored("\033[31m"+"._________________________________________________________________________."))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                                "+Fore.GREEN+"Search Menu"+Fore.RED +"                              |"))
    print(colored("\033[31m"+"|_________________________________________________________________________|"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                            "+Fore.GREEN+"["+Fore.BLUE+"1"+Fore.GREEN+"] Seatch Via Name"+Fore.RED +"                          |"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                            "+Fore.GREEN+"["+Fore.BLUE+"2"+Fore.GREEN+"] Search Via IP"+Fore.RED +"                            |"))
    print(colored("\033[31m"+"|_________________________________________________________________________|"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                                "+Back.RED+"[0"+Fore.RED+"] Main Menu"+Back.BLACK+"                            |"))
    print(colored("\033[31m"+"|_________________________________________________________________________|"))
    print('')
    print(colored(Fore.GREEN+"                              Enter an option"))
    option = int(input('                                  --> '))
    print("")
    if option == 0:
        main_menu()
    elif option == 1:
        search_name()
    elif option == 2:
        search_ip()
    else:
        print(colored("                              "+Back.RED+"Input Invalid:"+Back.BLACK+f" {option}"))
        time.sleep(3)
        search_menu()

def admin_menu():
    os.system('clear')
    print(colored("\033[31m"+"._________________________________________________________________________."))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                                "+Fore.GREEN+"Admin Menu"+Fore.RED +"                               |"))
    print(colored("\033[31m"+"|_________________________________________________________________________|"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                            "+Fore.GREEN+"["+Fore.BLUE+"1"+Fore.GREEN+"] Update Database"+Fore.RED +"                          |"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                            "+Fore.GREEN+"["+Fore.BLUE+"2"+Fore.GREEN+"] Update Row"+Fore.RED +"                               |"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                            "+Fore.GREEN+"["+Fore.BLUE+"3"+Fore.GREEN+"] Delete a Row"+Fore.RED +"                             |"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                            "+Fore.GREEN+"["+Fore.BLUE+"4"+Fore.GREEN+"] Add a Row"+Fore.RED +"                                |"))
    print(colored("\033[31m"+"|_________________________________________________________________________|"))
    print(colored("\033[31m"+"|                                                                         |"))
    print(colored("\033[31m"+"|                               "+Back.RED+"[0"+Fore.RED+"] Main Menu"+Back.BLACK+"                             |"))
    print(colored("\033[31m"+"|_________________________________________________________________________|"))
    print('')
    print(colored(Fore.GREEN+"                              Enter an option"))
    option = int(input('                                  --> '))
    print("")
    if option == 0:
        main_menu()
    elif option == 1:
        print(colored(Fore.GREEN+'         To update database, place the csv file into the '+Back.BLUE+'data folder'))
        print(colored(Fore.GREEN+'           and run the '+Back.BLUE+'seperate_csv.py'+Back.BLACK+'programe, this will seperate'))
        print(colored(Fore.GREEN+'                      columns and insert into database.'))
        print('')
        input(colored('                           '+Back.RED+'Press Enter To Continue'))
        admin_menu()
    elif option == 2:
        cursor.execute("SELECT ID FROM Yutes")
        for item in cursor:
            print(item)
        print(colored(Fore.GREEN+'                     Select an ID you would like to edit'))
        select_id = int(input('                                  --> '))
        print(colored(Fore.GREEN+('                  Would you like to edit the gamertag? (y/n)')))
        select1 = input('                                  --> ')
        if select1.lower() == 'y':
            print(colored(Fore.GREEN+('                               Enter gamertag')))
            new_gt = input('                                  --> ')
            cursor.execute(f"UPDATE Yutes SET gamertag = '{new_gt}' WHERE ID = '{select_id}';")
        print(colored(Fore.GREEN+('                    Would you like to edit the IP? (y/n)')))
        select2 = input('                                  --> ')
        if select2.lower() == 'y':
            print('                        Enter IP')
            new_ip = input('                                  --> ')
            cursor.execute(f"UPDATE Yutes SET ip = '{new_ip}' WHERE ID = '{select_id}';")
        print(colored(Fore.GREEN+'                      Are you sure to make changes? (y/n)'))
        sure_q = input('                                  --> ')
        if sure_q.lower() == 'y':
            connection.commit()
            admin_menu()
        else:
            admin_menu()
    elif option == 3:
        cursor.execute("SELECT ID FROM Yutes")
        for item in cursor:
            print(item)
        print(colored(Fore.GREEN+'                   Select an ID you would like to delete'))
        select_id = int(input('                                  --> '))
        cursor.execute(f"DELETE FROM Yutes WHERE ID = '{select_id}';")
        print(colored(Fore.GREEN+'                      Are you sure to make changes? (y/n)'))
        sure_q = input('                                  --> ')
        if sure_q.lower() == 'y':
            connection.commit()
            admin_menu()
        admin_menu()
    elif option == 4:
        print(colored(Fore.GREEN+'                              Enter a gamertag'))
        add_gt = input('                                  --> ')
        print(colored(Fore.GREEN+'                                  Enter IP'))
        add_ip = input('                                  --> ')
        print(colored(Fore.GREEN+'                      Are you sure to make changes? (y/n)'))
        sure_q = input('                                  --> ')
        cursor.execute(f"INSERT INTO Yutes (gamertag, ip) values ('{add_gt}', '{add_ip}');")
        if sure_q.lower() == 'y':
            connection.commit()
            admin_menu()
        admin_menu()
    elif option == 5:
        print('maybe add an option for whitelisting an ip')
    else:
        print(colored("                              "+Back.RED+"Input Invalid:"+Back.BLACK+f" {option}"))
        time.sleep(3)
        admin_menu()
        
def search_name():
    print(colored(Fore.GREEN+'                                 Enter Name'))
    enter_name_variable = str(input('                                  --> '))
    cursor.execute(f"SELECT gamertag, ip FROM Yutes WHERE gamertag LIKE '%{enter_name_variable}%'")
    for items in cursor:
        print(items)
    print(colored(Fore.GREEN+'                         Would you like to select another? (y/n)'))
    select_another = str(input('                                  --> '))
    if select_another.lower() == 'y':
        search_name()
    elif select_another.lower() == 'n':
        main_menu()
    else:
        print(colored("                              "+Back.RED+"Input Invalid:"+Back.BLACK+f" {select_another}"))
        time.sleep(3)
        search_name()
        
def search_ip():
    print(colored(Fore.GREEN+'                                  Enter IP'))
    enter_ip_variable = str(input('                               --> '))
    cursor.execute(f"SELECT gamertag, ip FROM Yutes WHERE ip LIKE '%{enter_ip_variable}%'")
    for items in cursor:
        print(items)
    print(colored(Fore.GREEN+'                      Would you like to select another? (y/n)'))
    select_another = str(input('                               --> '))
    if select_another.lower() == 'y':
        search_ip()
    elif select_another.lower() == 'n':
        main_menu()
    else:
        print(colored("                              "+Back.RED+"Input Invalid:"+Back.BLACK+f" {select_another}"))
        time.sleep(3)
        search_ip()
   
init()
main_menu()