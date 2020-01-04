from PIL import Image
import numpy as np
import sys
import os
import csv
from google_images_download import google_images_download
#
# arguments = {"keywords": "machine learning", "limit": 2, "print_urls": True}
# paths = response.download(arguments)
# #print complete paths to the downloaded images
# print(paths)


# default format can be changed as needed
def createFileList(myDir, format='.jpg'):
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList


# load the original image
# myFileList = createFileList('/Users/mankaransingh/Downloads/Image-Directory-to-CSV-master/downloads')
#
# for file in myFileList:
#     print(file)
#     img_file = Image.open(file)
#     # img_file.show()
#
#     # get original image parameters...
#     width, height = img_file.size
#     format = img_file.format
#     mode = img_file.mode
#
#     # Make image Greyscale
#     img_grey = img_file.convert('L')
#     # img_grey.save('result.png')
#     # img_grey.show()
#
#     # Save Greyscale values
#     value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
#     value = value.flatten()
#     print(value)
#     with open("output1.csv", 'a') as f:
#         writer = csv.writer(f)
#         writer.writerow(value)




def download_convert(keyword, limit, print_urls = True):
    arguments = {"keywords": keyword, "limit": limit, "print_urls": print_urls}
    response = google_images_download.googleimagesdownload()

    paths = response.download(arguments)
    print (paths)
    download_path = os.path.join(os.getcwd(), 'downloads/{}'.format(keyword))
    print(download_path)
    for path in os.listdir(download_path):

        img_path = os.path.join(download_path, path)
        print(img_path)
        img_file = Image.open(img_path)
            # img_file.show()

            # get original image parameters...
        width, height = img_file.size
        format = img_file.format
        mode = img_file.mode

            # Make image Greyscale
        img_grey = img_file.convert('L')
            # img_grey.save('result.png')
            # img_grey.show()

            # Save Greyscale values
        value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
        value = value.flatten()
        print(value)
        with open(os.path.join(os.getcwd(), 'csv_dir', keyword + '.csv'), 'a') as f:
                writer = csv.writer(f)
                writer.writerow(value)


download_convert(keyword = 'machine learning', limit = 2)
