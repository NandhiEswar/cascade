import os
import random
import string


def generate_random_name():
    # Generate a random string of lowercase letters and digits
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=8))


def rename_file(directory):
    for filename in os.listdir(directory):
        if filename.endswith((".png", ".jpeg", ".webp", ".avif", ".jpg")):
            file_path = os.path.join(directory, filename)
            print(filename)
            base_name, extension = os.path.splitext(filename)
            new_base_name = generate_random_name()
            new_filename = new_base_name + ".jpg"
            new_file_path = os.path.join(directory, new_filename)
            os.rename(file_path, new_file_path)
            print(f"Renamed {filename} to {new_filename}")


# Directory containing the files
directory = "/Users/nandieswar/Desktop/image"

# Call the function to rename the files
rename_file(directory)


def write_file_names_to_txt(directory, output_file):
    with open(output_file, "w") as f:
        for filename in os.listdir(directory):
            f.write("negtive/" + filename + "\n")

        print(f"File names written to {output_file}")


# directory
directory = "/Users/nandieswar/Desktop/image/negtive"

outputfile = "/Users/nandieswar/Desktop/image/negtive.txt"

# rename_file(directory)

write_file_names_to_txt(directory, outputfile)
