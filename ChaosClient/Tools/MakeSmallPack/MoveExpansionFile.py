# coding=utf-8
import os
import stat
import os.path
import sys
import shutil
import subprocess

fromdir_find = '../SmallPack/'

tagdir_find = '../../Client/Output/data/'

tempfile_folder = "temp_for_expansion/"

to_assets_folder = tempfile_folder + "assets/data/"

tagFloders = ["ccb", "map", "obj", "sound"]


def is_file_in_smallpack(path):
    path = path.replace("-a8.pkm", ".png")
    path = path.replace(".pkm", ".png")
    tagdir = path.replace(tagdir_find, fromdir_find)
    return os.path.exists(tagdir)


def MoveFiles(dir):
    newDir = dir
    copydir = dir.replace(tagdir_find, to_assets_folder)
    if os.path.isfile(dir):
        if not is_file_in_smallpack(dir):
            shutil.copy(dir, copydir)
            os.chmod(dir, stat.S_IWRITE)
            os.remove(dir)
    elif os.path.isdir(dir):
        if not os.path.exists(copydir):
            os.mkdir(copydir)
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            MoveFiles(newDir)


if os.path.exists(tempfile_folder):
    shutil.rmtree(tempfile_folder)

os.mkdir(tempfile_folder)
os.mkdir(tempfile_folder + "assets/")
os.mkdir(tempfile_folder + "assets/data/")

for floder in tagFloders:
    totagf = tagdir_find + floder
    MoveFiles(totagf)

#start zip
sz_path = r"C:\Program Files\7-Zip\7z.exe"
os.chdir(tempfile_folder)
zip_name = "main.1.packagename.obb"
zip_target = 'assets/*'
subprocess.call([sz_path, 'a', '-tzip', '-r', zip_name, zip_target])


