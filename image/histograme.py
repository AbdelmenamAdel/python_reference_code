import cv2
import numpy as np
path='D:/matlap_exe/toolbox/images/imdata/'

def RGB_2_Bin(img, threshold):
    row, column, _ = img.shape

    bin_img = np.zeros((row, column), dtype=np.uint8)

    for i in range(row):
        for j in range(column):
            # Convert the pixel value to grayscale using a simple average
            pixel_value = np.mean(img[i, j])  # Simple way to get intensity of RGB pixel

            # Apply the threshold to the pixel
            if pixel_value > threshold:
                bin_img[i, j] = 255  # Set to 255 (white)
            else:
                bin_img[i, j] = 0    # Set to 0 (black)

    # Display the binary image
    cv2.imshow('Binary Image', bin_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread(path+'toysflash.png')  
threshold_value = 128  
RGB_2_Bin(img, threshold_value)
