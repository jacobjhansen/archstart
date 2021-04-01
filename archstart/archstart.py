import os,sys

# Global Variables
version = '0.1'
updated_date = '3-30-2021'
heading = """    _     ____    ____  _   _  ____   _____     _     ____   _____ 
   / \   |  _ \  / ___|| | | |/ ___| |_   _|   / \   |  _ \ |_   _|
  / _ \  | |_) || |    | |_| |\___ \   | |    / _ \  | |_) |  | |  
 / ___ \ |  _ < | |___ |  _  | ___) |  | |   / ___ \ |  _ <   | |  
/_/   \_\|_| \_\ \____||_| |_||____/   |_|  /_/   \_\|_| \_\  |_|  
                                                                   
"""

def get_input(question,choices):
    rows, columns = os.popen('stty size', 'r').read().split()
    columns = int(columns)
    rows = int(rows)
    splitstring = "-" * columns

    os.system('clear')
    if columns > 70:
        print(heading)
    else:
        print('ARCHSTART')
    print("Version:",version)
    print("Last Updated:",updated_date)
    print("\n\n")
    print(question)
    for index,item in enumerate(choices):
        print("\t" + str(index) + ": " + item)
    print("\n")

    userinput = input("Enter your choice: ")

    return userinput

def get_desired_architecture():
    program_name = get_input('What\'s your program\'s name?',[])
    return_dict = {'program_name':program_name}

    program_architecture = get_input('What architecture would you like to use?',['Main/Subroutine','Publisher/Subscriber','Client/Server'])
    

    if int(program_architecture) == 0:
        # MAIN/SUBROUTINE
        return_dict['architecture'] = 'main/sub'

        subroutine_num = int(get_input('How Many Subroutines?',[]))
        return_dict['subroutine_num'] = subroutine_num
    elif int(program_architecture) == 1:
        # PUBLISHER/SUBSCRIBER
        return_dict['architecture'] = 'pub/sub'

        subscriber_num = int(get_input('How Many Subscribers?',[]))
        return_dict['subscriber_num'] = subscriber_num

        publisher_num = int(get_input('How Many Publishers?',[]))
        return_dict['publisher_num'] = publisher_num

        topic_num = int(get_input('How Many Topics?',[]))
        return_dict['topic_num'] = topic_num
    elif int(program_architecture) == 2:
        # CLIENT/SERVER
        return_dict['architecture'] = 'client/server'
        
        client = int(get_input('How Many Clients?',[]))
        return_dict['client_num'] = client

        server_num = int(get_input('How Many Servers?',[]))
        return_dict['server_num'] = server_num
    else:
        raise Exception("Desired Architecture not Valid.")

    return return_dict

test = get_desired_architecture()
print(test)




