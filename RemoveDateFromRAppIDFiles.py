import os
def del_from_file(path):
    with open(path, 'r') as f:
        file_list = f.readlines();
        try:
            index = file_list[0].index('/*')
            if index == 0:
                for list_index in range(len(file_list)):
                    try:
                        index = file_list[list_index].index('*/')
                        if index == 0:
                            break
                    except Exception as e:  #Attention: Should not catch all exception.
                        pass
                    if file_list[list_index].find('Project Last Save Date') < 0 and file_list[list_index].find('Created on Date') < 0:
                        #print(file_list[list_index].strip())
                        pass
                    else:
                        file_list[list_index] = ' *\n'
        except Exception as e:  #Attention: Should not catch all exception.
            pass
    with open(path, 'w') as f:
        f.writelines(file_list)
    
print('Hello, Python!')
WORK_DIR = 'RAppIDSrc'
files_name_list = [x for x in os.listdir(WORK_DIR) if os.path.isfile(os.path.join(WORK_DIR, x))]
for file_name in files_name_list:
    print('Processing "' + file_name + '"')
    del_from_file(os.path.join(WORK_DIR, file_name))
print('Process accomplished!')