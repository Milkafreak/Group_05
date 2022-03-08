"""System module."""
from urllib.request import urlretrieve
import os # we want python to be able to read what we have in our hard drive
import pandas as pd # type: ignore
import shutil


def download_file():
    """
    Downloads a file from an URL into your hard drive and read it.
    If directory exist print File already exists !
    Parameters
    ------------
    output_file:
        A folder if not exsited that contain Energy.csv file.
    Returns
    ---------
    Example
    ---------
    download_file("https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip",
    output_file='Test.zip')
    """
    file_link = "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv"
    output_file = 'Energy.csv'
    path = './Download'
    full_path = './Download/Energy.csv'
    # If file doesn't exist, download it. Else, print a warning message.
    if not os.path.exists(full_path):
        os.makedirs(path)
        print("The new directory is created!")
        urlretrieve(file_link, filename="Energy.csv")
        shutil.move("./"+output_file, full_path)
    else:
        print("File already exists !")

