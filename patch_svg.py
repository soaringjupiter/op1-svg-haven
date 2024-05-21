import argparse
import os

import diff_match_patch as dmp_module

# Set working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def apply_patch(original_svg_path, patch_file_path, output_svg_path):
    # read the original svg and patch files
    with open(original_svg_path, encoding="utf-8") as file:
        original_svg = file.read()
    with open(patch_file_path, encoding="utf-8") as file:
        patch_text = file.read()

    # create a diff_match_patch object
    dmp = dmp_module.diff_match_patch()

    # convert patch text to patches
    patches = dmp.patch_fromText(patch_text)

    # apply the patches to the original svg
    modified_svg, _ = dmp.patch_apply(patches, original_svg)

    # write the modified svg to the output file
    with open(output_svg_path, "w", encoding="utf-8") as file:
        file.write(modified_svg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Apply a patch file to an original file",
    )
    parser.add_argument("original_file", help="The original file")
    parser.add_argument("patch_file", help="The patch file to apply")
    args = parser.parse_args()

    apply_patch(
        args.original_file,
        args.patch_file,
        args.patch_file.replace(".patch", ""),
    )
