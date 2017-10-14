import os
import sys


def main():
    print_header()
    folder = sys.argv[1]
    folder = get_folder_from_user(folder)
    if not folder:
        print(folder)
        print("Sorry we can't search that location.")
        return

    file_type = sys.argv[2]

    if not file_type.strip():
        print("We can't search for nothing!")
        return

    print("Searching {} for {} type files".format(folder, file_type))

    matches = search_folders(folder, file_type)
    for m in matches:
        print(m)


def find_media_files(folder, file_type):
    #print_header()
    folder = get_folder_from_user(folder)
    if not folder:
        print(folder)
        print("Sorry we can't search that location.")
        return


    if not file_type.strip():
        print("We can't search for nothing!")
        return

    print("Searching {} for {} type files".format(folder, file_type))

    matches = search_folders(folder, file_type)
    return matches


def print_header():
    print('-------------------------------------')
    print('           FILE SEARCH APP')
    print('-------------------------------------')


def get_folder_from_user(folder):
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def search_folders(folder, file_type):
    # all_matches = []
    print("Searching {} for {} type files".format(folder, file_type))
    items = os.listdir(folder)


    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folders(full_item, file_type)
        else:
            yield from search_file(full_item, file_type)
            # all_matches.extend(matches)
            # for m in matches:
            #     yield m

    # return all_matches


def search_file(filename, file_type):
    # matches = []
    if filename.endswith(file_type):
        yield filename[: len(filename) - len(file_type) - 1]


if __name__ == '__main__':
    main()