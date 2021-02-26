#This opens a file and then closes file
#with open('genericTxtfile.txt', 'r') as f:
#   print(f.read()) 
    #print(f.read(2)) reads 2 characters in file
    #print(f.readlines()) reads all lines 
    #print(f.readline().strip()) reads first line removing whitespaces
    #print(f.readline().strip('\n')) reads second line removing newlines

    #for line in f:
        #print(line) #prints lines with spaces between them
        #f.seek(0) # to go back to the line specified
#with open('genericTxtfile.txt', 'a') as f:
 #   f.write("\n fifth line")


import os
def prepend_multiple_lines(file_name, list_of_lines):
    """Insert given list of strings as a new lines at the beginning of a file"""
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open given original file in read mode and dummy file in write mode
    with open(file_name , 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Iterate over the given list of strings and write them to dummy file as lines
        for line in list_of_lines:
            write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)

    def main():
        print('*** Insert a line at the top of a file ***')
    # Insert a line before the first line of a file 'sample.txt'
        a_list.insert("sample.txt", "This is a first line")
        print('*** Insert multiple lines at the beginning of a file ***')
        list_of_lines = ['New Line 1', 'New Line 2']
    # Insert strings in a list as new lines at the top of file 'sample.txt'
        prepend_multiple_lines("sample.txt", list_of_lines)
    if __name__ == '__main__':
   main()