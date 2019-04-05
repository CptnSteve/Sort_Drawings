# == DRAWING SORT ==
# Steve Olsen
# Program to sort files into folders based on the first 3 digits of their name.

# Using the operating system for file and filename access
import os

# Establish to-from folders
source_dir = 'C:\D_Legacy\Domino Engineering Data Base\_PDFs_\_Dump_'
target_base = 'C:\D_Legacy\Domino Engineering Data Base\_PDFs_'

# List to identify legal directories for use (these directories exist)
true_dir = ['A17', 'A18', 'A19',
            'AE1',
            'D17', 'D18', 'D19',
            'G17', 'G18', 'G19',]

# Iterate through the files in the source directory
for filename in os.listdir(source_dir):
    file_prefix = filename[0] + filename[1] + filename[2]
    target = target_base + '\\' + file_prefix + '\\' + filename
    misc_target = 'C:\D_Legacy\Domino Engineering Data Base\_PDFs_\Misc\\' + filename

    # Check that the output file does not already exist. If it does, print it's path.
    if os.path.exists(target):
        print(target)
    elif os.path.exists(misc_target):
        print(misc_target)
    # Check each filename's prefix to see if that value is present in the above list.
    elif file_prefix in true_dir:
        os.rename(source_dir + '\\' + filename,target)
    # If neither of these are true, dump the file into a misc. folder.
    else:
        os.rename(source_dir + '\\' + filename,misc_target)

input("Press enter to exit.")
