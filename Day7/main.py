
class Folder:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.folders = []
        self.parent = None

    def add_folder(self, folder):
        self.folders.append(folder)

    def add_file(self, file):
        self.files.append(file)

    def get_size(self):
        size = 0
        # print("get size for: ", self.name)
        for file in self.files:
            # print(size, " + ", file.size, " = ", size + file.size)
            size += file.size
        return size

    def get_subfolders_size(self):
        size = 0
        size += self.get_size()
        for folder in self.folders:
            size += folder.get_subfolders_size()
        return size
    
    def get_folder(self, folder_name):
        for folder in self.folders:
            if folder.name == folder_name:
                return folder
        return None

class File:
    def __init__(self, size, name):
        self.size = size
        self.name = name

def traverse_folder(folder : Folder, the_chosen_one: Folder, total_space_to_free_up: int):
    for f in folder.folders:
        # print(inline + " - " + f.name, "size:", f.get_subfolders_size())

        # for file in f.files:
        print(" - " , f.name, "size:", f.get_subfolders_size())
        if(f.get_subfolders_size() > total_space_to_free_up):
            print("checking folder:", f.name, "size:", f.get_subfolders_size())
        if f.get_subfolders_size() >= total_space_to_free_up and f.get_subfolders_size() < the_chosen_one.get_subfolders_size():
            print("found a better folder to delete:", f.name, "size:", f.get_subfolders_size())
            print("old folder:", the_chosen_one.name, "size:", the_chosen_one.get_subfolders_size())
            the_chosen_one = f

        the_chosen_one = traverse_folder(f,the_chosen_one, total_space_to_free_up)

    return the_chosen_one

f = open("input.txt", "r")

root = Folder("/")
current_folder = root
for line in f:
    if line.startswith("$ cd"):
        # print("Action: ", line)
        if line == "$ cd /":
            current_folder = root
        elif line.startswith("$ cd .."):
            current_folder = current_folder.parent
        else:
            folder_name = line[4:-1].strip()

            existing_folder = current_folder.get_folder(folder_name)
            if existing_folder:
                current_folder = existing_folder
            else:
                new_folder = Folder(folder_name)
                new_folder.parent = current_folder
                current_folder.add_folder(new_folder)
                current_folder = new_folder

    elif line.startswith("$ ls"):
        print("do nothing, its just ls")
    else:
        if line.startswith("dir"):
            splitted_line = line.split(" ")
            instruction = splitted_line[0]
            folder_name = line[4:-1].strip()
            new_folder = Folder(folder_name)
            new_folder.parent = current_folder
            current_folder.add_folder(new_folder)
        else:
            file_size = line.split(" ")[0]
            file_name = line.split(" ")[1]
            new_file = File(int(file_size), file_name)
            current_folder.add_file(new_file)
            # print("adding file:", new_file.name, " with size:", new_file.size)
    # print("current folder: ", current_folder.name, 
    # "files:", len(current_folder.files), 
    # "folders:", len(current_folder.folders),
    # "parent:", current_folder.parent.name if current_folder.parent else "None")

total_disk_space = 70000000
total_space_needed = 30000000
total_space_used = root.get_subfolders_size()
total_unused_space = total_disk_space - total_space_used
total_space_to_free_up = total_space_needed - total_unused_space 

print("total space used:", total_space_used)
print("total space to free up:", total_space_to_free_up)

print(root.get_subfolders_size())
print(traverse_folder(root, root, total_space_to_free_up).get_subfolders_size())

