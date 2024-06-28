import os
import shutil



initial_dir = os.getcwd()

def initialise_express(user):
    
    try:
        os.system("npm install -g express-generator")
        os.system("express --view=hbs "+"./Temp_Outputs/"+user+"app")
        os.chdir("./Temp_Outputs/"+user+"app")
        os.system("npm install")
        os.system("npm i dotenv")

        # Create .env file
        with open(".env", "w") as env_file:
            env_file.write(f'PORT={8080}\n')  # Add your environment variables here
        
        with open("app.js", 'r') as file:
            lines = file.readlines()

        # Insert `require('dotenv').config();` at line 6 (index 5 in zero-based index)
        lines.insert(5, "require('dotenv').config();\n")

        # Write the modified lines back to the file
        with open("app.js", 'w') as file:
            file.writelines(lines)

        # Create .gitignore file
        with open(".gitignore", "w") as gitignore_file:
            gitignore_file.write("node_modules/\n")  # Ignore node_modules directory

        
        os.chdir(initial_dir)
       
    except Exception as err:
        print(err)
        return False

    return True