import os
from core.Models import generate_response, check_if_ok


if check_if_ok():
    print("Model ok")


def generate_page(page_data):
    if not check_if_ok():
        print("Model not ok")
        return False
    
    os.chdir("./user1app/views")
    os.system("mkdir pages")
    return True

def create_content(page_data,page_name,user):
    try:
        #os.chdir("./user1app/views/pages")
        lines = generate_response(page_data)
        # Create the destination directory if it does not exist
        destination_dir = f'./pages'
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