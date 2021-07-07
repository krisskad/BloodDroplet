import numpy as np
import cv2
import glob
import os


def preprocess(img_file, output_dir):
    # Mat result
    # vector<vector<Point> >contours
    # vector<Vec4i>hierarchy
    savedContour = -1
    maxArea = 0.0

    # load image
    # image = cv2.imread('circle1.png')
    # binarayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # img_file = "DSC_0780.jpg"
    main_original = cv2.imread(img_file)
    # print(main_original.shape)

    kernel = np.ones((5, 5), np.uint8)
    gradient = cv2.morphologyEx(main_original, cv2.MORPH_GRADIENT, kernel)
    img = cv2.cvtColor(gradient, cv2.COLOR_BGR2GRAY)
    ret, th1 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

    # cv2.imwrite("A.png",th1)

    # Find the largest contour
    binarayImage = cv2.medianBlur(th1, 15)

    contours, hierarchy = cv2.findContours(binarayImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for i in range(0, len(contours)):
        area = cv2.contourArea(contours[i])
        if area > maxArea:
            maxArea = area
            savedContour = i

    # Create mask
    result = cv2.drawContours(binarayImage, contours, -1, (0, 255, 0), 5)

    # apply the mask:
    binarayImage &= result
    ret, binarayImage = cv2.threshold(binarayImage, 100, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    # cv2.imwrite("B.png",binarayImage)

    # Fill all small holes
    des = cv2.bitwise_not(binarayImage)

    # use morphology to close figure
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (35, 35))
    des = cv2.morphologyEx(des, cv2.MORPH_CLOSE, kernel, )

    contour, hier = cv2.findContours(des, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contour:
        cv2.drawContours(des, [cnt], 0, 255, -1)

    # binarayImage = cv2.bitwise_not(des)
    # print(gray.shape)
    # print(des.shape)
    # show image
    # cv2.imwrite("mask.png", des)

    # masked image
    masked = cv2.bitwise_and(main_original, main_original, mask=des)
    # cv2.imwrite("masked.png", masked)

    # draw rectangle over mask
    rect_img = des.copy()
    boxes = []
    for c in contour:
        (x, y, w, h) = cv2.boundingRect(c)
        boxes.append([x, y, w, h])

    boxes = np.asarray(boxes)
    x, y = np.min(boxes, axis=0)[:2]
    w, h = np.max(boxes, axis=0)[2:]

    roi = masked[y:y + h, x:x + w]
    # cv2.rectangle(rect_img, (left,top), (right,bottom), (255, 0, 0), 2)

    cv2.imwrite(output_dir, roi)


all_images = glob.glob("INPUT/*.jpg")

for image in all_images:
    # image name
    image_name = os.path.split(image)[1]
    output_dir = os.path.join("OUTPUT", image_name)
    preprocess(image, output_dir)
