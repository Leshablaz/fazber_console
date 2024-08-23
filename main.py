from colorama import init

init()
from colorama import Fore, Back, Style

while True:
    print("FazberEnterteiment 1985-1999 work command srting copyright")
    print("Write HELP for view comands and files for work")
    command = input()
    if command == "HELP":
        print("VIDEO REBUT-rebut cameras")
        print("AUDIO REBUT-rebut audio on cameras")
        print("Files for work on pc:")
        print("about_company.exe")
        print("programming_game.exe")
        print("check_cameras.exe-просматривает камеры и говорит обстановку")
        print("for start file write name of file")
    # else:
    # print("Commad not found")
    if command == "VIDEO REBUT":
        video_rebuting = 0
        while video_rebuting < 120:
            print("Rebuting")
            video_rebuting += 1

        if video_rebuting == 120:
            print("done")

    if command == "AUDIO REBUT":
        audio_rebuting = 0
        while audio_rebuting < 120:
            print("rebuting")
            audio_rebuting += 1
        if audio_rebuting == 120:
            print("done")

    if command == "about_company.exe":
        print("Mechanic-Henry")
        print("Owner:William Afton")
        print("Company name:Fredy Fazber's Pizza")
        print("Format:Pizzeria")

    #if command == "programming_game.exe":
        #language = input()
        #print("select language(python;c++;js;c)")
        #print("сложите 2 переменные a и b")

    if command == "check_cameras.exe":
        camera_number = input()
        print("напишите номер камеры")
        if(camera_number==1):
            print("3 аниматроника на месте")

