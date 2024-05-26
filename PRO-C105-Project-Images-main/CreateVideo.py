import os
import cv2

path = "Images/"
images = []

for file in os.listdir(path):
    file_name, file_extension = os.path.splitext(file)
    if file_extension.lower() in ['.gif', '.png', '.jpg', '.jpeg', '.jiff']:
        full_file_name = os.path.join(path, file)
        print(full_file_name)
        images.append(full_file_name)

if images:
    count = len(images)
    frame = cv2.imread(images[0])
    height, width, channels = frame.shape
    size = (width, height)
    print(size)

    out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

    for i in range(count):
        frame = cv2.imread(images[i])
        out.write(frame)

    print("Done")
    out.release()
else:
    print("No images found in the specified directory.")
