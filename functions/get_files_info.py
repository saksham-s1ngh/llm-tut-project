import os

def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir

    # 
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))

    #  
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    try :
        files_info = [] # list to append the string outputs
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename) # creating an absolute path with all the files in target_dir
            file_size = 0
            is_dir = os.path.isdir(filepath) # check if the filepath is a directory
            file_size = os.path.getsize(filepath) # get filesize of the filepath 
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)

    except Exception as e:
        return f"Error: {e}"
