import time
import re
import math
import os, sys, inspect
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"Core")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)
import querytexts
from makefilesizeextpatharray import my_list
from buildindex import BuildIndex
from querytexts import Query
import webbrowser as wb
exit=1
choice=0
while (exit==1):
    os.system('cls')
    read_files=[]
    print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
    print '++++++++++++++++   FILE SYSTEM  SEARCH ENGINE   ++++++++++++++++'
    print '++++            BY ADITYA JAGDEV AND FAIZAN KHAN            ++++'
    print '++++++++++++++++     14BCE0185     14BCE0187    ++++++++++++++++'
    print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
    counter = 0
    print '\n1. Search for text in files\n2. Search for files\n3. Exit\n\nYour Choice : ',
    choice = input()
    if (choice == 1):                                                       #Text Search Module Begin
        print 'Creating Index...'
        for (dir, _, files) in os.walk("./"):
            for f in files:
                path = os.path.join(dir, f)
                if os.path.exists(path):
                    container = path                    
                    ext = container.rsplit( ".", 1 )[ 1 ]
                    ext=ext.lower()
                    if (ext == 'txt'):
                        read_files.append(path)
        query=Query(read_files) 
        s=raw_input('\nSearch in files for : ')
        s=s.lower()
        if ' ' in s:
            test_oneword=query.phrase_query(s)
        else:
            test_oneword=query.one_word_query(s)
        if not test_oneword:
            print 'No Results Found'
        else:
            found1 = str(test_oneword)
            found1 = found1.rsplit("'",1)[0]
            found1 = found1.split("/",1)[1]
            full_path = os.getcwd()
            full_path = full_path + '\\'
            full_path = full_path + found1
            print 'Phrase found in file \'' + (str(test_oneword).rsplit("\\",1)[1]).rsplit("'",1)[0] + '\''
            choice1 = input('\nEnter 1 to open the file\nEnter 2 to open the containing folder\nEnter 3 to Continue\n\nYour Choice : ')
            if(choice1 == 1):
                wb.open(full_path)
            if(choice1 == 2):
                wb.open(full_path.rsplit("\\",1)[0])                        #Text Search Module Ends                
    elif(choice == 2):                                                      #File Search Module Begins 
        print 'Creating Index...'
        filenames=['Name.searchenginedb']
        query=Query(filenames)                                  #printing the names path again
        s=raw_input('\nType filename to search for : ')         #TAKING INPUT FROM USER HERE
        s=s.lower()
        if ' ' in s:
            test_phrase=query.phrase_query(s)
        else:
            test_phrase=query.one_word_query(s)
        get_fp = open('Path.searchenginedb')
        get_fs = open('Size.searchenginedb')
        get_ff = open('Format.searchenginedb')
        get_fn = open('Name.searchenginedb')
        for i in range(len(my_list)):
            if s in my_list[i]:
                print '\nFile Name   : ',
                for j, line in enumerate(get_fn):
                    if j == i:
                        print line,
                        break
                print 'File Format : ',
                for j, line in enumerate(get_ff):
                    if j == i:
                        print line,
                        break
                print 'File Size   : ',
                for j, line in enumerate(get_fs):
                    if j == i:
                                                                            #File Size Unit Begin
                        fsize = int(line)
                        if(fsize<=1024):
                            pwr = 0
                            term = "Bytes"
                        elif((fsize/1024) <= 1024):
                            pwr = 1
                            term = "KiloBytes"
                        elif(((fsize/1024)/1024) <= 1024):
                            pwr = 2
                            term = "MegaBytes"
                        elif((((fsize/1024)/1024)/1024) <= 1024):
                            pwr = 3
                            term = "GigaBytes"
                                                                            #File Size Unit End
                        print str(fsize) + " " + term
                        break
                print 'File Path   : ',
                for j, line in enumerate(get_fp):
                    if j == i:
                        print line
                        break
                full_path = os.getcwd()                                     #File Open Module Ends
                full_path = full_path + '\\'
                full_path = full_path + str(line).split("/",1)[1]
                choice1 = input('\nEnter 1 to open the containing folder\nEnter 2 to Continue\n\nYour Choice : ')
                if(choice1 == 1):
                    wb.open(full_path.rsplit("\\",1)[0])                    #File Open Module Ends
                counter = counter + 1
        print '\nFound ' + str(counter) + ' result(s)'
        get_fp.close()
        get_fs.close()
        get_fn.close()
        get_ff.close()                                                      #File Search Module Ends 
    elif ( choice ==3 ):
        exit = 0
    else:
        print 'Invalid Input'
    if (exit != 0):
        exit=input('\nEnter 1 to Make Another Search : ')
print '\nHave ',
time.sleep(0.3)
print 'a ',
time.sleep(0.3)
print 'Nice ',
time.sleep(0.3)
print 'Day !!! '
time.sleep(0.3)
print '+++++++++++++++++'
time.sleep(0.1)
