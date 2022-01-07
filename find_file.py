def find_file(folder_file_name, isfolder=False, isfile=False):
    import os
    from fuzzywuzzy import process
    path = None
    file_folder_opened = False
    listA = []
    list_of_paths = []
    list_of_dir = []
    list_of_file = []
    for root, dir_of_vedio, files in os.walk('/home/'):
        for file in os.listdir(root):

            listA.append(file.lower())

            list_of_paths.append(os.path.join(root, file))
            if os.path.isfile(os.path.join(root, file)):
                list_of_file.append(file.lower())
            else:
                list_of_dir.append(file.lower())
    # print(listA, '\n', list_of_paths)
    if isfolder:
        path = list_of_paths[listA.index(process.extractOne(folder_file_name, list_of_dir)[0])]
    elif isfile:
        path = list_of_paths[listA.index(process.extractOne(folder_file_name, list_of_file)[0])]
    else:
        appp = process.extract(folder_file_name, listA)
        for app in appp:
            if app[1] > 90:
                print(app)
                path = list_of_paths[listA.index(app[0])]
                os.system('xdg-open ' + path)
            else:
                pass
        file_folder_opened = True
    if not file_folder_opened:
        os.system('xdg-open ' + path)
    return path



