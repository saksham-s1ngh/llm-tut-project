# tests.py -> for functions
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def test():
    # # GET_FILES_INFO TESTS
    # result = get_files_info("calculator", ".")
    # print("Result for current directory:")
    # print(result)
    # print("")

    # result = get_files_info("calculator", "pkg")
    # print("Result for 'pkg' directory:")
    # print(result)

    # result = get_files_info("calculator", "/bin")
    # print("Result for '/bin' directory:")
    # print(result)

    # result = get_files_info("calculator", "../")
    # print("Result for '../' directory:")
    # print(result)
    #result = get_file_content("calculator", "lorem.txt")
    #print(f"Result for lorem.txt: {result}")
    
    # # GET_FILE_CONTENT TESTS
    # result = get_file_content("calculator", "main.py")
    # print(f"Result for main.py: {result}")

    # result = get_file_content("calculator", "pkg/calculator.py")
    # print(f"Result for pkg/calculator.py: {result}")

    # result = get_file_content("calculator", "/bin/cat")
    # print(f"Result for /bin/cat: {result}")

    # # WRITE_FILE TESTS
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"Result for lorem.txt: {result}")

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"Result for morelorem.txt: {result}")

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"Result for temp.txt: {result}")

if __name__ == "__main__":
    test()
