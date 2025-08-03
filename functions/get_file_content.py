import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):

    abs_filepath = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path)) 

    if not target_file.startswith(abs_filepath):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_file, "r") as f:
            # MY PREVIOUS IMPLEMENTATION
            #   I didn't use the MAX_CHAR variable entirely, and had hardcoded the testcase for 10000 character to fit the problem (INCORRECT)
            # file_content_string = f.read() 
            # if len(file_content_string) > MAX_CHARS:
            #     file_content_string = file_content_string[:10000] + f"[...File \"{file_path}\" truncated at 10000 characters]"
            # return file_content_string
            
            content = f.read(MAX_CHARS)
            if os.path.getsize(abs_filepath) > MAX_CHARS:
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
            
    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists the contents of the file constrained within the working directory, as a fixed length string whose length is determined by MAX_CHARS.",
    parameters=types.Schema(
        type = types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the input file, to be found within the working directory.",
            ),
        },
    ),
)