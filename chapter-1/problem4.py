import os

def list_directory_contents(path):
    """
    List the contents of the directory specified by 'path'.
    
    Parameters:
    path (str): The path of the directory to list.
    
    Returns:
    None
    """
    try:
        # Open the directory specified by 'path'
        with os.scandir(path) as entries:
            # Iterate over each entry in the directory
            for entry in entries:
                # Print the name of the entry
                print(entry.name)
    except FileNotFoundError:
        # Handle the case where the directory does not exist
        print(f"The directory {path} does not exist.")
    except PermissionError:
        # Handle the case where permission is denied to access the directory
        print(f"Permission denied to access {path}.")

# Replace 'your_directory_path' with the path of the directory you want to list
directory_path = '/'
# Call the function to list the contents of the specified directory
list_directory_contents(directory_path)