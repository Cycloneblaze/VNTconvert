##  VNT Converter
##  by Cycloneblaze
##  v1.0
##
##      description:
##          The .vnt file extension is created by various proprietary note-taking
##          applications developed by Samsung for their smartphones - for example
##          the Samsung Galaxy Mini. I am not aware of what phones use it these
##          days, but there are still application out there which create VNOTE
##          files. Such files cannot be opened by regular editors such as Notepad
##          but a more advanced editor like Notepad++ will reveal that the
##          structure of these files is simple, involving tags denoting the date
##          of creation and of modification, as well as the text in hexadecimal
##          values.
##
##          This python script will accept .vnt files and output .txt files which
##          are readable by any common editor or program.
##          Right now it should be placed in the folder containing the files that
##          are to be converted.
##
##      version history:
##          0.0 | started work on the program
##              | will it happen?
##              | we shall see
##          1.0 | the program works
##              | converts all files in the directory in which it exists
##
##      to-do:
##          - think of things to do
##          - good enough for now.

import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
path = os.getcwd()

hexlist = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0A', '0B', '0C', '0D', '0E', '0F', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1A', '1B', '1C', '1D', '1E', '1F', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2A', '2B', '2C', '2D', '2E', '2F', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3A', '3B', '3C', '3D', '3E', '3F', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4A', '4B', '4C', '4D', '4E', '4F', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5A', '5B', '5C', '5D', '5E', '5F', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6A', '6B', '6C', '6D', '6E', '6F', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7A', '7B', '7C', '7D', '7E', '7F', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8A', '8B', '8C', '8D', '8E', '8F', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9A', '9B', '9C', '9D', '9E', '9F', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'DA', 'DB', 'DC', 'DD', 'DE', 'DF', 'E0', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'EA', 'EB', 'EC', 'ED', 'EE', 'EF', 'F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'FA', 'FB', 'FC', 'FD', 'FE', 'FF']
count = 0
listed = 0
number = 0

def main():
    for file in os.listdir():
        dontdelete = 0
        if os.path.isfile(file) and file.lower().endswith(".vnt"):
            with open(file, mode='r+t') as infile:
                lines = list(infile)
                if (lines[1]) != 'VERSION:1.1\n':
                    print("Warning: the VNOTE version is not 1.1.\n> The format may be different to expected.\n> This program may not operate as intended.\n> This warning outputs for every file processed.")
                    print("Still continue?")
                    really = str(input("Enter 'y' to proceed, any other key to exit: "))
                    if really == 'y' or really == "Y":
                        None
                    else:
                        print("Okay, exiting.")
                        exit()
                infile.seek(0)
                contents = infile.read()
                contents = contents.replace("BEGIN:VNOTE\nVERSION:1.1\nBODY;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:", "")
                dates = []
                seq1 = contents.splitlines()
                for line in seq1:
                    if 'DCREATED' in line:
                        line = line.replace('DCREATED:', '')
                        dates.append(line)
                    if 'LAST-MODIFIED:' in line:
                        line = line.replace('LAST-MODIFIED:', '')
                        dates.append(line)
                seq1 = seq1[0:-3]
                contents = "\n".join(seq1)
                contents = contents.replace('\n=', '')
                contents = contents.replace('=', '', 1)
                seq2 = contents.split('=')
                for i in range(len(seq2)):
                    global hexlist
                    if seq2[i] in hexlist:
                        seq2[i] = chr(int(seq2[i], 16))
                text = ''.join(seq2)
                seq3 = text.splitlines()
                dates[0] = dates[0].split('T')
                dates[0][0] = dates[0][0][0:4] + '-' + dates[0][0][4:6] + '-' + dates[0][0][6:8]
                dates[0][1] = dates[0][1][0:2] + ':' + dates[0][1][2:4] + ':' + dates[0][1][4:6]
                dates[1] = dates[1].split('T')
                dates[1][0] = dates[1][0][0:4] + '-' + dates[1][0][4:6] + '-' + dates[1][0][6:8]
                dates[1][1] = dates[1][1][0:2] + ':' + dates[1][1][2:4] + ':' + dates[1][1][4:6]
                filename = seq3[0] + '.txt'
                illegal = ('\\' '/' ':' '*' '?' '"' '<' '>' '|')
                for i in illegal:
                    filename = filename.replace(i, '-')
                seq3[0] = seq3[0] + ' [Created on ' + dates[0][0] + ' at ' + dates [0][1] + ' | Last modified on ' + dates[1][0] + ' at ' + dates[1][1] + ']'
                text = '\n'.join(seq3)
                with open(filename, mode='a+') as outfile:
                    try:
                        outfile.write(text)
                    except(UnicodeEncodeError):
                        print('\n1 file failed to convert! It was not deleted.\nCharacters which could not be converted found in:', file, '\n')
                        dontdelete = 1
                        pass
                    except(OSError):
                        print('\n1 file failed to convert! It was not deleted.\nAn unspecified error occurred when converting:', file, '\n(probably the output file could not be created)\n')
                        dontdelete = 1
                        pass
                if dontdelete == 1:
                    os.remove(filename)
            if infile.closed == True:
                if dontdelete != 1:
                    os.remove(file)
                    global count
                    count = count + 1
    fintext = str(count) + " files were converted and removed.\npython code by Cycloneblaze, 2016\nPress any key to finish."
    fin = input(fintext)
    if fin:
        exit()

def start():
    if listed == 0:
        print("Directory is", path, "\n\nAll VNOTE files in this directory will now be converted to text files.\nThis cannot be undone.\nOkay to continue?\n")
        proceed = str(input("Enter 'y' to proceed, 'ls' to list files, any other key to quit: "))

        ls = ('ls', 'Ls', 'lS', 'LS')
        if proceed == "y" or proceed == "Y":
            main()
        elif proceed in ls:
            print('\n', "Files to be converted:\n", sep='', end='')
            for file in os.listdir():
                if file.lower().endswith(".vnt"):
                    global number
                    number  = number + 1
                    print(file)
            print('\n', end='')
            global listed
            listed = 1
            start()
        else:
            exiting = input("The files will not be converted.\nPress any key to exit. ")
            if exiting:
                exit()
    else:
        print("These", number, "files will now be converted to text files.\nThis cannot be undone.\nOkay to continue?\n")
        proceed = str(input("Enter 'y' to proceed, any other key to quit: "))

        if proceed == "y" or proceed == "Y":
            main()
        else:
            exiting = input("These files will not be converted.\nPress any key to exit. ")
            if exiting:
                exit()

start()
