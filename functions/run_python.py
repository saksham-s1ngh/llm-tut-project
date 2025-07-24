import os, subprocess

def run_python_file(working_directory, file_path, args=[]):
    work_dir = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(work_dir, file_path))

    if not target_path.startswith(work_dir):
        # basically if the target file path lies outside the working directory (bounds), this condition will
        #   filter that out by comparing if the target file path starts with the same structure as the working directory.
        #   ex: work_dir = /home/xyz , filepath = docs/report.txt, target = /home/xyz/docs/report.txt
        #       result ==> target path does start with the work_dir file path
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(target_path):
        return f'Error: File "{file_path}" not found.'
    
    if not target_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        command = [target_path] + args
        completed_process = subprocess.run(command, capture_output=True, text=True, timeout=30) 
        output = ""
        output += f"""
        STDOUT: {completed_process.stdout}
        STDERR: {completed_process.stderr}
        """
        if completed_process.returncode != 0:
            output += f"""
            Process exited with code {completed_process.returncode}"""
        
        if not output:
            return "No output produced"

    except Exception as e:
        return f"Error: executing Python file: {e}"