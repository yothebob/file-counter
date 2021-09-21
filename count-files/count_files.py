import os 
from os import path

'''
A small utility to count all the files in a given master folder (main_dir)

- folders donot get added to count

	to use (in terminal locally) - 
		1. go to count_files folder (cd ~/path/to/count_files)
		2. type python3 -c "from count_files import main;main('/home/user/path/to/disired_file')"
'''
                


def main(main_dir=os.getcwd()):
    
    
    os.chdir(main_dir)
    final_count = 0


    def recursive_count_files(_dir):
        total_files=0
        os.chdir(_dir)
        for file in os.listdir():
            if path.isdir(file):
                total_files += recursive_count_files(_dir + '/' + file)
            else:
                total_files += 1
        
        return total_files


    for file in os.listdir():
        if path.isdir(file):
            #final_count += count_files(main_dir +'/'+ file)
            final_count += recursive_count_files(main_dir + '/' + file)
            os.chdir(main_dir)
        else:
            final_count += 1
            
            
    print("Total files in folder: ",final_count)


'''obsolete function that only counts one folder deep'''
 #def count_files(_dir):
        #os.chdir(_dir)
        #total_files = 0
        #for file in os.listdir():
            #total_files+= 1
        #return total_files
