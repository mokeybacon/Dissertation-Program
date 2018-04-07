# Programme by Mike Baker
# In conjunction with Sheffield Hallam Univeristy
# As part of my final year project
import time
import requests
import sys

def main():
    user_choice()

def user_choice():
    # This function outlines the options the user can make for categories
    global choice
    global category_choice
    global option

    cat_list = (
        '1:Hard drive recovery', '2:Hard drive copying', '3:RAID', '4:Hard Drive Formatting/Wiping', '5:ISO Creation',
        '6:Encryption', '7:Word processing', '8:Programming', '9:Resource monitor', '10:Browsers', '11:Torrenting',
        '12:Photo Editing', '13:Compression', '14:Remote Desktop', '15:Virtual Machines')

    print('Here is the list of available options:')
    [print(i) for i in cat_list]
    # Getting them to choose a category option
    choice = input('Please enter the number of the operation you need help with:')
    if choice.isalpha():
        user_choice()
    acceptedchoices = int(choice) < len(cat_list)

    if acceptedchoices:
        correctedchoice = int(choice) - int(1)
        category_choice = cat_list[correctedchoice]
    else:
        print('Please select a valid number')
        user_choice()

    option = category_choice
    # Confirming user choice is what they wanted
    print('You have chosen option: ', option)
    yesorno()

def yesorno():
	#This function allows for error checking
    acceptance = input('Is that correct? ')
    nolist = acceptance.startswith('n') or acceptance.startswith('N')
    yeslist = acceptance.startswith('y') or acceptance.startswith('Y')

    # Check if acceptance occurs in either list, if not loop back to start
    if nolist:
        print('Sorry about that, here are those options again:')
        main()
    elif yeslist:
        software_options(choice, option)
    else:
        print('Input not recognised, please put Yes or No:')
        yesorno()


def software_options(choice, option):
	# This function lists the available options for software in each category
    if choice == '1':
        print('Here is a list of the possible tools for', option, ':')
        hard_drive_recovery_list = (
            '1:Recuva', '2:Stellar Data Recovery', '3:Undelete 360'
        )
        [print(i) for i in hard_drive_recovery_list]
        programme_choice = input("Which programme would you like to use?")
        prog_choice =int(programme_choice) - int(1)

        if programme_choice == '1':
            link = "https://download.ccleaner.com/rcsetup153.exe"
            file_name = "recuva.exe"
            download(link, file_name)
            print('You have selected option',hard_drive_recovery_list[prog_choice])
            recuva_instructions = (
            'Here are the instructions for Recuva','1. Install the program. The installer can be found in the same folder where you ran this programme from.',
            '2. Choose the data type of the file you want to restore (Picture, Video, Document etc).' ,
            '3. Choose where the file was located, there is an option if you do not know.' ,
            '4. Start the scan. If the scan fails the first time then select "Deep Scan".' , '5. Look through the files Recuva has found.' ,
            '6. If you find the correct file, select it and choose recover.' , '7. Select where you would like the file to be recovered to.' ,
            '8. Check the destination location to make sure the file has recovered.' ,
            '9. If you need to find another file then choose advanced settings rathan than begin the process again.'
            )
            [print (i) for i in recuva_instructions]
            endofprogramme()

        elif programme_choice == '2':
            print('You have selected option', hard_drive_recovery_list[prog_choice])
            stellar_data_recovery_instructions = (
            'Here are the instructions for Stellar Data Recovery', 'Step 1: ', 'Step 2:'

            )
            [print(i) for i in stellar_data_recovery_instructions]
            endofprogramme()
			
        elif programme_choice == '3':
            print('You have selected option', hard_drive_recovery_list[prog_choice])
            undelete360_instructions = (
            'Here are the instructions for Undelete360', 'Step 1: ', 'Step 2:'

            )
            [print(i) for i in undelete360_instructions]
            endofprogramme()
			
    elif choice == '2':
        print('Here is a list of the possible tools for', option, ':')
        hard_drive_copying_list = (
            '1:Ease US Backup Home', '2:Minitool Partition Wizard', '3:Clonezillar'
        )
        [print(i) for i in hard_drive_copying_list]
        programme_choice = input("Which programme would you like to use?")
        prog_choice = int(programme_choice) - int(1)
        if programme_choice == '1':
            print(hard_drive_copying_list[prog_choice])
			
        elif programme_choice == '2':
            link = "http://download1.minitool.com/10.2.2/pw102-free.exe"
            file_name = "minitool.exe"
            download(link, file_name)
            print('You have selected option', hard_drive_copying_list[prog_choice])
            minitool_instructions = ('Here are the instructions for Minitool Partition Wizard' , '1. Install the program. The installer can be found in the same folder where you ran this programme from' ,
            '2. Make sure all important data is backed up due to the original data being deleted during the transfer' ,
            '3. Select the drive or partition you wish to transfer' , '4. Right click the drive or partition and choose copy' ,
            '5. Select the destination drive or partition' , '6. Allocate partitions to the new drive if needed' ,
            '7. Read and understand the BIOS information, for more information visit http://www.boot-disk.com/boot_priority.htm' ,
            '8. Click apply'

            )
            [print(i) for i in minitool_instructions]
            endofprogramme()

	#The code below is commented out to aide in future work on the project
			
    # elif choice == '3':
        # print('Here is a list of the possible tools for', option, ':')
        # RAID_list = (
            # '1:Windows Software RAID', '2:Linux MDADM', '3:Mac OS Sierra Disk Utility'
        # )
        # [print(i) for i in RAID_list]
        # programme_choice = input("Which programme would you like to use?")
        # prog_choice = int(programme_choice) - int(1)
        # if programme_choice == '1':
            # print(RAID_list[prog_choice])


    # elif choice == '4':
        # print('Here is a list of the possible tools for', option, ':')
        # HDD_formatting_list = (
            # '1:DBAN',
        # )
        # [print(i) for i in HDD_formatting_list]
        # programme_choice = input("Which programme would you like to use?")
        # prog_choice = int(programme_choice) - int(1)
        # if programme_choice == '1':
            # print(HDD_formatting_list[prog_choice])


    # elif choice == '5':
        # print('Here is a list of the possible tools for', option, ':')
        # ISO_creation_list = (
            # '1:Rufus', '2:Etcher', '3:PowerISO'
        # )
        # [print(i) for i in ISO_creation_list_list]
        # programme_choice = input("Which programme would you like to use?")
        # prog_choice = int(programme_choice) - int(1)
        # if programme_choice == '1':
            # print(ISO_creation_list[prog_choice])


    # elif choice == '6':
        # print('Here is a list of the possible tools for', option, ':')
        # Encryption_list = (
            # '1:Windows Bitlocker', '2:Veracrypt'
        # )
        # [print(i) for i in Encryption_list]
        # programme_choice = input("Which programme would you like to use?")
        # prog_choice = int(programme_choice) - int(1)
        # if programme_choice == '1':
            # print(Encryption_list[prog_choice])


    # elif choice == '7':
        # print('Here is a list of the possible tools for', option, ':')
        # Word_processing_list = (
            # '1:Open Office', '2:Libre Office'
        # )
        # [print(i) for i in Word_processing_list]
        # programme_choice = input("Which programme would you like to use?")
        # prog_choice = int(programme_choice) - int(1)
        # if programme_choice == '1':
            # print(Word_processing_list[prog_choice])


def download(link, file_name):
	#This function downloads the installer of each file. The location of the installer is set before the instructions are written.
    with open(file_name, "wb") as f:
            print ("Downloading %s" % file_name)
            response = requests.get(link, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None: 
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
                    sys.stdout.flush()


def endofprogramme():
	#This function offers the possibility of a graceful closing
    print('Here are the options once you are done:')
    print('1: Return to main menu')
    print('2: Return to choosing a programme')
    print('3: Close the program')
    endchoice = input('Please choose what you would like to do:')

    if endchoice == '1':
        main()
    elif endchoice == '2':
        software_options(choice,option)
    elif '3':
        time.sleep(5)
    else:
        print('Please choose from the list provided')
        endofprogramme()


def passwordchecker():
	#A basic password checker for beta testing, would be utilised more if the programme became an .exe
    passwordcheck = input("Please enter the password:")

    if passwordcheck == 'Helloworld':
        print('Hello, what do you need help with today?')
        main()
    else:
        print("Password incorrect, please enter the correct password.")
        passwordchecker()

passwordchecker()
