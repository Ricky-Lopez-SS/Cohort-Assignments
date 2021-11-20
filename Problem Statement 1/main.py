import logging
import numpy as np
import pandas as pd
import sys
import os
import phonenumbers
from validate_email import validate_email
from phonenumbers import geocoder, NumberParseException


def replace_content(file) :
    ''' Finds and changes headers into proper format. in place conversion, returns None '''

    new_file_content = ""

    for line in file :
        strip_line = line.strip()
        new_line = line.replace("Agent Writing Contract Start Date (Carrier appointment start date)" , "Agent Writing Contract Start Date")
        new_line = new_line.replace("Agent Writing Contract Status (actually active and cancelled\'s should come in two different files)" , "Agent Writing Contract Status")
        new_file_content += new_line + '\n'
    
    file.write(new_file_content)

def validate_us_numbers(df) :
    '''takes in dataframe and validates phone number elements within phone number columns. '''

    are_invalid_numbers = False

    for column in df.columns :

        if 'Phone Number' in column :
            
            for index, element in enumerate(df[column]) :
                
                try:
                    if element:
                        number = phonenumbers.parse(element, "US")
                except NumberParseException:
                    logging.debug(f"Invalid phone number entry FOUND at index value: {index} of column: {column} of element: [{element}]")
                    are_invalid_numbers = True


                if geocoder.country_name_for_number(number, "en") != 'United States' :
                    logging.warning(f"Invalid US number FOUND: {number} at index value: {index} in column: {column}")
                    are_invalid_numbers = True
                    
            if are_invalid_numbers :
                logging.warning("Invalid numbers found")

def validate_email_id(df) :
    '''determines whether the emails in the dataframe are in valid format.'''
    
    for email_val in df['Agent Email Address'] :
        if not(validate_email(email_address= email_val, check_format=True) ) :
            logging.warning(f"Invalid email found : {email_val}")



if __name__ == '__main__' :

    logging.basicConfig(filename = "logfile.log", filemode='w', format='[%(asctime)s][%(levelname)s] %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

    logging.info("Program has started")

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

                    df = pd.read_csv(curr_file_name)

                    print(df['Agent License State (active)'])

                    validate_us_numbers(df)

                    #TODO: write logic for state valdiation!















    

    