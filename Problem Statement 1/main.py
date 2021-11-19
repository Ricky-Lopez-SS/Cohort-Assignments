import logging
import numpy as np
import pandas as pd
import sys
import os

def replace_content(file) :

    new_file_content = ""

    for line in file :
        strip_line = line.strip()
        new_line = line.replace("Agent Writing Contract Start Date (Carrier appointment start date)" , "Agent Writing Contract Start Date")
        new_line = new_line.replace("Agent Writing Contract Status (actually active and cancelled\'s should come in two different files)" , "Agent Writing Contract Status")
        new_file_content += new_line + '\n'
    
    file.write(new_file_content)




if __name__ == '__main__' :

    nyl_list = []

    files = os.listdir('resources')

    files.sort()

    if files[0] == '.DS_Store' :
        files.remove('.DS_Store')

    print(files)

    curr_file_name = next_file_name = None

    for i, v in enumerate(files) :

        if not curr_file_name : #current file is non-existent; must be first file read. 
            curr_file_name = 'resources/' + v
            continue

        next_file_name = 'resources/' + v

        with open(curr_file_name, "r+") as curr_file, open(next_file_name, "r+") as next_file :

            curr_line_count = sum(1 for line in curr_file)
            next_line_count = sum(1 for line in next_file)

            if abs(curr_line_count - next_line_count) > 500 :

                curr_file_name = next_file_name
                continue

            else : 
                
                if curr_file_name in nyl_list :
                    
                    #print out that file has already been processed!
                    print("Then it should be in here for the rest of the time.")
                    continue

                else : #begin processing
                    
                    print("it should  get in here a couple of times. ")

                    nyl_list.append(curr_file_name)

                    #replace_content(curr_file)








    

    