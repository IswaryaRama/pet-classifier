import os
import shutil

base_dir = "dataset"

for split in ["train", "test"]:
    split_dir = os.path.join(base_dir, split)
    cats_dir = os.path.join(split_dir, "cats")
    dogs_dir = os.path.join(split_dir, "dogs")
    os.makedirs(cats_dir, exist_ok=True)
    os.makedirs(dogs_dir, exist_ok=True)

    moved_cats = 0
    moved_dogs = 0

    for fname in os.listdir(split_dir):
        fpath = os.path.join(split_dir, fname)
        if not os.path.isfile(fpath):
            continue  # skip the cats/dogs folders themselves
        if fname.lower().startswith("cat"):
            shutil.move(fpath, os.path.join(cats_dir, fname))
            moved_cats += 1
        elif fname.lower().startswith("dog"):
            shutil.move(fpath, os.path.join(dogs_dir, fname))
            moved_dogs += 1

    print(f"{split}: moved {moved_cats} cat images, {moved_dogs} dog images")

print("Done organizing dataset.")
