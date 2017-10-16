import os
import sys
import subprocess


def main():
    if len(sys.argv) == 4:
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
        if len(sys.argv) == 4:
            dir_to_save = sys.argv[3]
            dir_to_save = get_folder_from_user(dir_to_save)
            if dir_to_save:
                for m in matches:
                    print(m)
                    video_name = os.path.basename(m)
                    input_folder = os.path.dirname(m)
                    convert_video_to_mp4(video_name, file_type, input_folder, dir_to_save=dir_to_save)
            else:
                print("Sorry we can't search there")
        else:
            for m in matches:
                print(m)
                video_name = os.path.basename(m)
                input_folder = os.path.dirname(m)
                convert_video_to_mp4(video_name, file_type, input_folder)
    else:
        for arg in sys.argv:
            print(arg)
        print("You did not provide the correct arguments: 1. inpupt_dir 2. file_type [3. out_directory]")
        return


def print_header():
    print('-------------------------------------')
    print('           FILE SEARCH APP')
    print('-------------------------------------')


def get_folder_from_user(folder):
    """
    Check that the given pathway is a directory
    :param folder: pathway to check
    :return: None if folder if not a director. The absolute path of the folder if it is a directory
    """
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def search_folders(folder, file_type):
    """
    Search a folder for files of the given file extention
    :param folder: directory to search
    :param file_type: file extention to search for
    :yield: files located in the directory that match the extention
    """
    # all_matches = []
    print("Searching {} for {} type files".format(folder, file_type))
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folders(full_item, file_type)
        else:
            yield from search_file(full_item, file_type)


def search_file(filename, file_type):
    """
    Search files for files that end with the given file type extension and return the path with the extension removed
    :param filename: file to search
    :param file_type: file type that matches
    :yield: the absolute path of the file name with the file type extension removed
    """
    # matches = []
    if filename.endswith(file_type):
        yield filename


def convert_video_to_mp4(old_video, file_type_to_convert, input_folder, dir_to_save=None):
    old_video_path = os.path.join(input_folder, old_video)
    if dir_to_save:
        new_video_path = os.path.join(dir_to_save, old_video.replace(file_type_to_convert, "mp4"))
    else:  # save in current directory
        new_video_path = old_video_path.replace(file_type_to_convert, "mp4")
    print("converting {}".format(old_video))
    if not os.path.isfile(old_video_path):
        print("{} is not a file".format(old_video_path))
        return
    subprocess.run([r'C:\Users\beliefs22\AppData\Local\Programs\ffmpeg\bin\ffmpeg.exe', '-i',
                    old_video_path, "-strict", "-2", new_video_path], stderr=subprocess.PIPE)
    print("Finished converting {} saved at {}".format(old_video, new_video_path))


def find_and_convert_media_files(input_folder, file_type, output_folder=None):
    """
    Locates media files or the given type in the given folder and converts them to mp4 format
    :param input_folder: directory that contains the media files
    :param file_type: file type to search for i.e. avi
    :param output_folder: directory to save files to. If not given, will save in files current directory
    :return:
    """
    # TODO: Add options for different file types this can serve as the skelton for each type
    print_header()
    folder = input_folder
    folder = get_folder_from_user(folder)
    if not folder:
        print(folder)
        print("Sorry we can't search that location.")
        return
    file_type = file_type

    if not file_type.strip():
        print("We can't search for nothing!")
        return

    print("Searching {} for {} type files".format(folder, file_type))

    matches = search_folders(folder, file_type)
    if output_folder:
        dir_to_save = output_folder
        dir_to_save = get_folder_from_user(dir_to_save)
        if dir_to_save:
            for m in matches:
                video_name = os.path.basename(m)
                input_folder = os.path.dirname(m)  # Find specific input folder since it searchers recursively
                convert_video_to_mp4(video_name, file_type, input_folder, dir_to_save=dir_to_save)
        else:
            print("Sorry we can't search there")
    else:
        for m in matches:
            print(m)
            video_name = os.path.basename(m)
            input_folder = os.path.dirname(m)
            convert_video_to_mp4(video_name, file_type, input_folder)


if __name__ == '__main__':
    main()
