import cv2

data_dir = "docs/IF2101T/CQProjectBasics_1"

def __main():
    img = cv2.imread(data_dir + "/IMG_1630_2.jpg")
    overLay = cv2.imread(data_dir + "/IMG_1630_2_T.jpg")
    org = img.copy()

    height, width, _ = overLay.shape
    x = 50
    y = 30
    img[y:(y + height), x:(x + width)] = overLay
    
    cv2.imshow("Final result", img)
    cv2.imshow("Original", org)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print(cv2.__version__)
    __main()

