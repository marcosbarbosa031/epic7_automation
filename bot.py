import os
import time
import msvcrt
import sys


# Functions
def format_devices(d):
    return d.split("device")[0].strip()


def loop(battleTime):
    cont = 1
    while 1:
        try:
            print("Turn: " + str(cont))
            # Team
            print("Clicking Select Team")
            os.system("adb shell input tap 1136 668")
            time.sleep(3)

            # Cure all
            print("Clicking Cure all")
            os.system("adb shell input tap 71 552")
            time.sleep(2)

            # Confirm
            print("Clicking Confirm")
            os.system("adb shell input tap 695 493")
            time.sleep(2)

            # Start
            print("Clicking Start")
            os.system("adb shell input tap 1136 668")
            print("Waiting for battle (1:40 min)")
            time.sleep(battleTime)

            # Stage Clear
            print("Clicking Stage Clear")
            os.system("adb shell input tap 1136 668")
            time.sleep(3)

            # Cancel Event Quest
            print("Canceling Event Quest if happen")
            os.system("adb shell input tap 537 512")
            time.sleep(1)

            # Cancel (Friend request)
            print("Canceling friend request if asked")
            os.system("adb shell input tap 537 512")
            time.sleep(1)

            # Confirm
            print("Clicking Confirm")
            os.system("adb shell input tap 1136 668")
            time.sleep(3)

            # Cancel Quest
            print("Canceling Quest")
            os.system("adb shell input tap 537 512")
            time.sleep(1)

            # Again
            print("Clicking Try Again")
            os.system("adb shell input tap 1136 668")
            time.sleep(3)

            if cont % 10 == 0 and sellEquipments:
                print("Going to sell equipments")

                # Back
                print("Clicking <")
                os.system("adb shell input tap 36 34")
                time.sleep(2)

                # Back
                print("Clicking Back")
                os.system("adb shell input tap 115 663")
                time.sleep(2)

                # Backpack
                print("Clicking Backpack")
                os.system("adb shell input tap 1062 36")
                time.sleep(2)

                # All
                print("Selecting All")
                os.system("adb shell input tap 188 162")
                time.sleep(2)

                # Sell
                print("Clicking Sell")
                os.system("adb shell input tap 1089 162")
                time.sleep(3)

                # Auto Select
                print("Clicking Auto Select")
                os.system("adb shell input tap 216 162")
                time.sleep(2)

                # Select
                print("Clicking Select")
                os.system("adb shell input tap 823 575")
                time.sleep(2)

                # Sell(n)
                print("Clicking Sell(n)")
                os.system("adb shell input tap 368 162")
                time.sleep(2)

                # Confirm
                print("Clicking Confirm")
                os.system("adb shell input tap 739 500")
                time.sleep(2)

                # Close
                print("Clicking Close")
                os.system("adb shell input tap 642 695")
                time.sleep(2)

                # Ready
                print("Clicking Ready")
                os.system("adb shell input tap 1038 660")
                time.sleep(3)

            cont = cont + 1
            os.system('cls')

        except KeyboardInterrupt:
            cond = True
            while cond:
                print("Script Stopped. If you want to restart type Y else Type N to exit.")
                while msvcrt.kbhit():
                    msvcrt.getch()
                opt = str(msvcrt.getch()).upper()
                if opt == "B'N'":
                    print("Number of runs automated: " + str(cont))
                    os.system('pause')
                    sys.exit()
                elif opt != "B'Y'":
                    print("Invalid option. Type Y or N only")
                else:
                    cond = False;


f = open("config.ini", "r")
config = f.readline()
path = config.rsplit("noxPath: ")
try:
    if path[1] != '':
        path = path[1] + '\\bin'
    else:
        print("NoxPath not found!")
        sys.exit()
except IndexError:
    print("NoxPath not found!")
    sys.exit()

if len(sys.argv) > 1:
    sellEquipments = False
    try:
        battleTime = int(sys.argv[1])
    except ValueError:
        print("Invalid argument type. First argument has to be an integer (Battle delay)")
        sys.exit()

    if '-s' in sys.argv:
        sellEquipments = True

    # Change diretory to adb's
    os.chdir(path)

    # iniciate loop
    loop(battleTime)

else:
    print("No arguments!")
