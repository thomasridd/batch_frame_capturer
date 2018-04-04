import cv2
from os import walk


f = []
# get a list of files to process from in the input directory
input_folder = 'data/in'
for (dirpath, dirnames, filenames) in walk(input_folder):
    f.extend(filenames)

output = 'data/out/'

# for each file
for file_name in f:
    # open the video
    vidcap = cv2.VideoCapture('%s/%s' % (input_folder, file_name))
    success = True

    # start at frame 0
    frame_number = 0

    # while the video still has time left
    while success:
        # get the next frame
        vidcap.set(cv2.CAP_PROP_POS_MSEC, 10000 * frame_number)
        success, image = vidcap.read()

        # if the frame capture is successful write it to the output directory
        if success:
            print('writing file %s_%d_seconds.jpg' % (file_name, 10 * frame_number))
            cv2.imwrite("%s/%s_%d_seconds.jpg" % (output, file_name, 10 * frame_number), image)     # save frame as JPEG file
            frame_number += 1

    # close the video
    vidcap.release()
