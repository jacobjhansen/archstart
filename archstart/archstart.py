import os,sys,re
from FileCreation import FileCreation
from FileCreation import main_subroutine_main,main_subroutine_sub
from FileCreation import pub_sub_pub,pub_sub_sub,pub_sub_topic,pub_sub_driver

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

    if not program_name.endswith('.py'):
        program_name = program_name + '.py'

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

def generate_main_sub(arch_dict):
    current = FileCreation(arch_dict['program_name'])

    for i in range(1,arch_dict['subroutine_num']+1):
        subroutine_name = 'subroutine' + str(i)
        current.addSection(main_subroutine_sub,[subroutine_name])

    current.addSection(main_subroutine_main,["subroutine1"])

def generate_pub_sub(arch_dict):
    current = FileCreation(arch_dict['program_name'])

    current.addSection(pub_sub_pub,[])
    current.addSection(pub_sub_sub,[])
    current.addSection(pub_sub_topic,[])
    current.addSection('\n',[])

    for i in range(1,arch_dict['publisher_num']+1):
        publisher_name = 'publisher' + str(i)
        current.addSection('PUB = Publisher()\n',[publisher_name])

    for i in range(1,arch_dict['subscriber_num']+1):
        subscriber_name = 'subscriber' + str(i)
        current.addSection('SUB = Subscriber()\n',[subscriber_name])

    for i in range(1,arch_dict['topic_num']+1):
        topic_name = 'topic' + str(i)
        current.addSection('TOPIC = Topic()\n',[topic_name])

    current.addSection(pub_sub_driver,['publisher1','topic1','topic1','subscriber1','publisher1'])


def generate_client_server(arch_dict):
    pass

def main():
    arch_dict = get_desired_architecture()
    print(arch_dict)

    assert arch_dict['architecture'] == 'main/sub' or arch_dict['architecture'] == 'pub/sub' or arch_dict['architecture'] == 'client/server'

    if arch_dict['architecture'] == 'main/sub':
        generate_main_sub(arch_dict)
    elif arch_dict['architecture'] == 'pub/sub':
        generate_pub_sub(arch_dict)
    elif arch_dict['architecture'] == 'client/server':
        generate_client_server(arch_dict)




if __name__ == "__main__":
    main()