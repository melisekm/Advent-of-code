import timeit


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.folders = {}
        self.parent = parent
        self.files = []
        self.size = 0


class File:
    def __init__(self, size, name):
        self.size = int(size)
        self.name = name


def load_input(file_name="in.txt"):
    root = None
    curr_folder = None
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            split = line.split()
            if line[0] == "$":
                command = split[1]
                if command == "cd":
                    folder_name = split[2]
                    if folder_name == "..":
                        curr_folder = curr_folder.parent
                        continue
                    if curr_folder and folder_name in curr_folder.folders:
                        curr_folder = curr_folder.folders[folder_name]
                    else:
                        new_folder = Directory(folder_name, curr_folder)
                        if root is None:
                            root = new_folder
                        curr_folder = new_folder
                elif command == "ls":
                    pass
            else:
                if split[0] == 'dir':
                    folder_name = split[1]
                    new_folder = Directory(folder_name, curr_folder)
                    if folder_name not in curr_folder.folders:
                        curr_folder.folders[folder_name] = new_folder
                else:
                    curr_folder.files.append(File(split[0], split[1]))

    return root


def traverse(root, all_folders):
    all_folders.add(root)
    root.size = sum(file.size for file in root.files)
    for folder in root.folders.values():
        traverse(folder, all_folders)
        root.size += folder.size


def solve_pt1():
    root = load_input()
    all_folders = set()
    traverse(root, all_folders)
    return sum(folder.size for folder in all_folders if folder.size <= 100000)


def solve_pt2():
    root = load_input()
    all_folders = set()
    traverse(root, all_folders)
    need_size = 30000000 - (70000000 - root.size)
    return min(folder.size for folder in all_folders if folder.size >= need_size)


def run_part(solve_fn, part_idx):
    start = timeit.default_timer()
    result = solve_fn()
    end = timeit.default_timer()
    print(result)
    print(f"Total time pt{part_idx}: {(end - start):.3f} sec")


run_part(solve_pt1, 1)
run_part(solve_pt2, 2)
