import os
import shutil

initial_dir = os.getcwd()

def initialise_express(user):
    try:
        os.system("npm install -g express-generator")
        os.system("express --view=hbs "+"./Temp_Outputs/"+user+"app")
        os.chdir("./Temp_Outputs/"+user+"app")
        os.system("npm install")

        src_dir = '../Resources'
        dest_dir = f'./{user}app'
        
        try:
            # Create the destination directory if it does not exist
            os.makedirs(dest_dir, exist_ok=True)
            
            # Iterate over all files in the source directory
            for filename in os.listdir(src_dir):
                src_file = os.path.join(src_dir, filename)
                dest_file = os.path.join(dest_dir, filename)
                
                # Copy each file to the destination directory
                if os.path.isfile(src_file):
                    shutil.copy(src_file, dest_file)
                    print(f"Copied: {src_file} to {dest_file}")
        except Exception as e:
            print(f"An error occurred: {e}")
        os.chdir(initial_dir)
       
    except Exception as err:
        print(err)
        return False

    return True