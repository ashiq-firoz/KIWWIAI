import os
from core.Models import generate_response, check_if_ok
import threading


running_ports = []
start_port = 49152
open_port = 49152 

initial_dir = os.getcwd()

serverON = False

if check_if_ok():
    print("Model ok")


def generate_page(page_data,repoId,user):
    if not check_if_ok():
        print("Model not ok")
        return False
    
    os.chdir("./Temp_Outputs/"+user+repoId+"app/views")
    os.system("mkdir pages")
    os.chdir(initial_dir)
    return True

def create_content(page_data,page_name,user,repoId):
    try:
        #os.chdir("./user1app/views/pages")
        lines = generate_response(page_data)
        # Create the destination directory if it does not exist
        destination_dir = "./Temp_Outputs/"+user+repoId+"app/views"+f'./pages'
        os.makedirs(destination_dir, exist_ok=True)

        # Construct the full file path
        file_path = os.path.join(destination_dir, f"{page_name}.hbs")

        # Write the lines to the file
        with open(file_path, "w") as f:
            f.write("\n".join(lines))
        
        return True
    
    except Exception as err:
        print(err)
        return False

def serverStart(repoId,user):
    try:
        serverON = True
        os.chdir('./Temp_Outputs/'+f'{user}{repoId}app')
        with open(".env", "w") as env_file:
            env_file.write(f'PORT={open_port}\n')
        os.system("npm start")
        os.chdir(initial_dir)
        
        return "Stopped"
    except Exception as err:
        print(err)
        return False

def start_server_thread(repoId,user):
    
    server_thread = threading.Thread(target=serverStart, args=(repoId,user))
    server_thread.start()
    serverON = True
    return server_thread


def get_page(page_name : str,repoId:str,user:str):
    """
    page_name : "/page_name"
    """
    global serverON, open_port  # Declare global variables

    if not serverON:
        start_server_thread(repoId,user)
        port = open_port
        open_port += 1
        return f'http://localhost:{port+1}/{page_name}'
    
    if serverON:
        return f'http://localhost:{port+1}/{page_name}'


