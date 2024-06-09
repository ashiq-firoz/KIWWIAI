import os
from core.Models import generate_route_response

def add_route(page_name, page_data, user):
    try:
        # Generate the new lines to be added
        
        
        # Define the path to the index.js file
        file_path = f'../routes/index.js'
        
        # Read the current content of the file
        with open(file_path, "r") as f:
            content = f.readlines()
        
        content = generate_route_response(page_data, f'pages/{page_name}.hbs',content)
        # Write the updated content back to the file
        with open(file_path, "w") as f:
            f.write("\n".join(content) + "\n")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
