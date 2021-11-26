import logging
import numpy as np
import pandas as pd
import sys
import os
import phonenumbers
from validate_email import validate_email
from phonenumbers import geocoder, NumberParseException
import matplotlib.pyplot as plt

def remove_spaces(list) :

    ret_str = ""

    for i in range(0, len(list)) :
        if list[i] :
            ret_str += list[i] + ' '
        
    return ret_str

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
                    logging.debug(f"Invalid US number FOUND: {number} at index value: {index} in column: {column}")
                    are_invalid_numbers = True
                    
            if are_invalid_numbers :
                logging.warning("Invalid numbers found")

def validate_email_id(df) :
    '''determines whether the emails in the dataframe are in valid format.'''
    
    for index, email_val in enumerate(df['Agent Email Address']) :

        is_valid = validate_email(
            email_address=email_val,
            check_format=True,
            check_blacklist=False,
            check_dns=False,
            dns_timeout=10,
            check_smtp=False,
            smtp_timeout=10,
            smtp_helo_host='my.host.name',
            smtp_from_address='my@from.addr.ess',
            smtp_skip_tls=True,
            smtp_tls_context=None,
            smtp_debug=True)

        if not is_valid :
            logging.warning(f"Invalid email found : {email_val} at index: {index}")

def validate_states(df):
    '''Checks all columns regarding state in dataframe and logs any invalid states.'''

    contains_invalid_states = False

    state_list = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']


    states = df[['Agent State', 'Agency State']]

    for column in states :
        for  index, element in enumerate(states[column]) :
            if element not in state_list:

                if not contains_invalid_states:
                    contains_invalid_states = True

                logging.debug(f"Invalid State found at index {index} : {element}")
    
    if contains_invalid_states : 
        logging.warning(f"Invalid states found")


if __name__ == '__main__' :

    logging.basicConfig(filename = "logfile.log", filemode='w', format='[%(asctime)s][%(levelname)s] %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

    logging.info("Program has started")

    nyl_list = []
    is_first_file = False

    files = os.listdir('resources')

    files.sort()

    if files[0] == '.DS_Store' :
        files.remove('.DS_Store')

    curr_file_name = next_file_name = None

    for i, v in enumerate(files) : 

        curr_file_name = 'resources/' + v
        
        if not i : #the first file in the folder

            with open(curr_file_name, "r+") as curr_file : 
                nyl_list.append(curr_file_name)

                #replace_content(curr_file)

                df = pd.read_csv(curr_file_name)

                validate_us_numbers(df)

                validate_email_id(df)

                validate_states(df)

                prev_file_name = curr_file_name
        
        else:

            with open(curr_file_name, "r+") as curr_file, open(prev_file_name, "r+") as prev_file:
                
                prev_line_count = sum(1 for line in prev_file)
                curr_line_count = sum(1 for line in curr_file)

                if abs(curr_line_count - prev_line_count) > 500 :
                    prev_file_name = curr_file_name
                    continue

                else:

                    if curr_file_name in nyl_list : 

                        logging.debug(f"file {curr_file_name} has already been processed.")
                        print("Sorry, the file has already been processed. ")

                    else: 

                        print("Currently running...")

                        nyl_list.append(curr_file_name)

                        #replace_content(curr_file)

                        df = pd.concat([df, pd.read_csv(curr_file_name)], axis = 0)

                        validate_us_numbers(df)

                        validate_email_id(df)

                        validate_states(df)

                        prev_file_name = curr_file_name


    print(f"\n9. Dataframe 1\n\n{df}\n")

    group_by_agency_state = df.groupby("Agency State").count()

    print(f"10. group by agency state\n\n {group_by_agency_state}\n" )

    group_by_agency_state['Agency State'] = group_by_agency_state.index

    df['Agent Full Name'] = df['Agent First Name'] + df['Agent Middle Name'] + df['Agent Last Name']

    df['Agent Full Name'] = df['Agent Full Name'].apply(lambda x : remove_spaces(x.split(" ")) )

    agent_info = df[['Agent Full Name' , 'Agent Writing Contract Start Date', 'Date when an agent became A2O']]

    print(f"11. Agent info\n\n{agent_info}")

    df.hist()

    group_by_agency_state.plot(x='Agency State' , y='Agent Id', kind='bar', legend='False', title='Group By Agency State')
    plt.show()
    

















    

    