#Each part of the code must be run separately through all images, the parts of the code are divided by #ph_redX.py

#ph_red1.py

import os
import cv2

def make_background_in_folders(root_folder):
    # Recursive function to traverse all folders and files inside the root folder
    def process_folder(folder_path):
        # Iterate through all items in the current folder
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            # If it's a folder, call the function recursively
            if os.path.isdir(item_path):
                process_folder(item_path)
            # If it's a file, check if it's an image
            elif item.endswith('.png') or item.endswith('.jpg') or item.endswith('.jpeg'):
                file_without_extension = os.path.splitext(item)[0]
                # Load the image with an alpha channel
                image = cv2.imread(item_path, cv2.IMREAD_UNCHANGED)
                # Check if the image is loaded successfully
                if image is not None:
                    # If the image has an alpha channel, remove it
                    if image.shape[-1] == 4:
                        trans_mask = image[:, :, 3] == 0
                        image[trans_mask] = [255, 255, 255, 255]
                        new_img = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
                        cv2.imwrite(os.path.join(folder_path, file_without_extension + '.png'), new_img)
                        print(f'{item}\'s alpha channel deleted')
                    else:
                        print(f"File '{item}' has no alpha channel, skipping.")
                else:
                    print(f"Unable to load file: '{item}'")

    # Start traversal from the root folder
    process_folder(root_folder)

# Specify the path to the root folder
root_folder = "Latin"
make_background_in_folders(root_folder)



#ph_red2.py

import os
import cv2

def shift_in_folders(root_folder):
    # Recursive function to traverse all folders and files inside the root folder
    def process_folder(folder_path):
        # Iterate through all items in the current folder
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            # If it's a folder, call the function recursively
            if os.path.isdir(item_path):
                process_folder(item_path)
            # If it's a file, check if it's an image
            elif item.endswith('.png') or item.endswith('.jpg') or item.endswith('.jpeg'):
                file_without_extension = os.path.splitext(item)[0]
                # Load the image
                img = cv2.imread(item_path)
                # Check if the image is loaded successfully
                if img is not None:
                    arr_translation = [[15, -15], [-15, 15], [-15, -15], [15, 15]]
                    arr_caption = ['15-15', '-1515', '-15-15', '1515']
                    for i in range(4):
                        # Apply translation to the image
                        M = np.float32([[1, 0, arr_translation[i][0]], [0, 1, arr_translation[i][1]]])
                        shifted_img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
                        cv2.imwrite(os.path.join(folder_path, file_without_extension + arr_caption[i] + '.png'), shifted_img)
                        print(f'{item} shifted')
                else:
                    print(f"Unable to load file: '{item}'")

    # Start traversal from the root folder
    process_folder(root_folder)

# Specify the path to the root folder
root_folder = "Latin"
shift_in_folders(root_folder)


#ph_red3.py

import os
from PIL import Image

def rotate_in_folders(root_folder):
    # Recursive function to traverse all folders and files inside the root folder
    def process_folder(folder_path):
        # Iterate through all items in the current folder
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            # If it's a folder, call the function recursively
            if os.path.isdir(item_path):
                process_folder(item_path)
            # If it's a file, check if it's an image
            elif item.endswith('.png') or item.endswith('.jpg') or item.endswith('.jpeg'):
                file_without_extension = os.path.splitext(item)[0]
                try:
                    # Open the image using PIL
                    img = Image.open(item_path)
                    # Check if the image is loaded successfully
                    if img is not None:
                        # Define rotation angles
                        angles = [-13, 13]
                        for angle in angles:
                            # Rotate the image
                            rotated_img = img.rotate(angle, resample=Image.BICUBIC, fillcolor=(255, 255, 255))
                            # Convert the image to RGB mode
                            rotated_img = rotated_img.convert('RGB')
                            # Save the rotated image
                            rotated_img.save(os.path.join(folder_path, file_without_extension + str(angle) + '.png'))
                            print(f'{item} rotated')
                    else:
                        print(f"Unable to load file: '{item}'")
                except Exception as e:
                    print(f"Error processing file '{item}': {e}")

    # Start traversal from the root folder
    process_folder(root_folder)

# Specify the path to the root folder
root_folder = "Latin"
rotate_in_folders(root_folder)



#ph_red4.py

import os

def balancing(root_folder):
    # Recursive function to traverse all folders and files inside the root folder
    def process_folder(folder_path):
        # Get the list of subfolders in the current folder
        subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
        # Iterate through all subfolders
        for subfolder in subfolders:
            subfolder_path = os.path.join(folder_path, subfolder)
            # Call the function recursively for each subfolder
            process_folder(subfolder_path)
            # Get the list of files in the current subfolder
            files = [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]
            # Define the minimum number of files in subfolders
            min_value = 6500
            # If there are more files in the current subfolder than the minimum, delete the excess
            if len(files) > min_value:
                # Sort files by creation time
                files.sort(key=lambda x: os.path.getctime(os.path.join(subfolder_path, x)))
                # Delete excess files
                for file_to_remove in files[min_value:]:
                    os.remove(os.path.join(subfolder_path, file_to_remove))

    # Start traversal from the root folder
    process_folder(root_folder)

# Specify the path to the root folder
root_folder = "Latin"
balancing(root_folder)


#ph_red5.py

import os
import shutil
import random


def move_and_delete(root_folder, destination_folder, portion=0.3):
    # Create the target folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate through all folders A-Z
    for letter_folder in os.listdir(root_folder):
        if letter_folder.isalpha():  # Check if it is a folder with a letter
            letter_folder_path = os.path.join(root_folder, letter_folder)
            # Get the list of files in the folder
            files = [f for f in os.listdir(letter_folder_path) if os.path.isfile(os.path.join(letter_folder_path, f))]
            # Determine the number of files to move
            num_to_move = int(len(files) * portion)
            # Randomly select files to move
            files_to_move = random.sample(files, num_to_move)
            # Move the selected files to the target folder
            for file_to_move in files_to_move:
                source_file = os.path.join(letter_folder_path, file_to_move)
                destination_file = os.path.join(destination_folder, letter_folder, file_to_move)
                # Create a folder for the letter in the target folder if it doesn't exist
                if not os.path.exists(os.path.join(destination_folder, letter_folder)):
                    os.makedirs(os.path.join(destination_folder, letter_folder))
                shutil.move(source_file, destination_file)
                print(f"{file_to_move} moved")


# Specify the path to the root folder containing folders A-Z
root_folder = "Latin"
# Specify the path to the target folder where folders A-Z will be moved
destination_folder = "Latin-test"
# Specify the portion of files to move (in this case 30%)
portion = 0.2

move_and_delete(root_folder, destination_folder, portion)


#ph_red6.py

import os
import shutil
import random


def move_and_delete(root_folder, destination_folder, portion=0.3):
    # Create the target folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate through all folders A-Z
    for letter_folder in os.listdir(root_folder):
        if letter_folder.isalpha():  # Check if it is a folder with a letter
            letter_folder_path = os.path.join(root_folder, letter_folder)
            # Get the list of files in the folder
            files = [f for f in os.listdir(letter_folder_path) if os.path.isfile(os.path.join(letter_folder_path, f))]
            # Determine the number of files to move
            num_to_move = int(len(files) * portion)
            # Randomly select files to move
            files_to_move = random.sample(files, num_to_move)
            # Move the selected files to the target folder
            for file_to_move in files_to_move:
                source_file = os.path.join(letter_folder_path, file_to_move)
                destination_file = os.path.join(destination_folder, letter_folder, file_to_move)
                # Create a folder for the letter in the target folder if it doesn't exist
                if not os.path.exists(os.path.join(destination_folder, letter_folder)):
                    os.makedirs(os.path.join(destination_folder, letter_folder))
                shutil.move(source_file, destination_file)
                print(f"{file_to_move} moved")


# Specify the path to the root folder containing folders A-Z
root_folder = "Latin"
# Specify the path to the target folder where folders A-Z will be moved
destination_folder = "Latin-valid"
# Specify the portion of files to move (in this case 30%)
portion = 0.1

move_and_delete(root_folder, destination_folder, portion)
