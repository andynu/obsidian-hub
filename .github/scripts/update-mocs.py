import os
import sys
import argparse

from make_mocs import filter_directories, moc_file_path_for_directory, index_content_for_directory


def process_all_directories(directory, args):
    print("CAUTION - overwriting MOCs - DO NOT COMMIT")
    for root, dirs, files in os.walk(directory):
        filter_directories(dirs)
        dirs.sort()
        process_directory(root, dirs, files)


def process_directory(root, dirs, files):
    moc_file_path = moc_file_path_for_directory(root)
    with open(moc_file_path, 'w') as output:
        output.write(index_content_for_directory(root, dirs, files))


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        description="Create and update MOCs, mimicking Zoottelkeeper output"
    )
    parser.add_argument("-v", "--verbose", action="store_true", default=False)

    args = parser.parse_args(argv)

    process_all_directories('../..', args)


if __name__ == "__main__":
    main()
