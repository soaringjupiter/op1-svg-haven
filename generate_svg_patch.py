import argparse
import os

import diff_match_patch as dmp_module

# Set working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def generate_patch(original_svg_path, modified_svg_path, patch_file_path):
    # read the original and modified svg files
    with open(original_svg_path, encoding="utf-8") as file:
        original_svg = file.read()
    with open(modified_svg_path, encoding="utf-8") as file:
        modified_svg = file.read()

    # create a diff_match_patch object
    dmp = dmp_module.diff_match_patch()

    # generate the patches
    patches = dmp.patch_make(original_svg, modified_svg)

    # convert patches to text
    patch_text = dmp.patch_toText(patches)

    # write the patch text to the patch file
    with open(patch_file_path, "w", encoding="utf-8") as file:
        file.write(patch_text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a patch file from two files")
    parser.add_argument("original_file", help="The original file")
    parser.add_argument("modified_file", help="The modified file")
    args = parser.parse_args()

    yes = True

    generate_patch(
        args.original_file,
        args.modified_file,
        args.modified_file + ".patch",
    )
