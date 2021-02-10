import cv2
import numpy as np
import random

def __main():
    img = createBaseImage()
    org = img.copy()

    (x, y), radius = cv2.minEnclosingCircle(points = pts)
    org = cv2.circle(org, (int(x), int(y)), int(radius), (0, 255, 0), 2)
    cv2.imshow("Final result", org)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ノイズの描画
def __setNoise(img, color):
    global pts
    height, width, channels = img.shape[:3]
    for num in range(50):
        x = int(random.uniform((width/2)-(width/4), (width/2) +(width/4)))
        y = int(random.uniform((height/2)-(height/4), (height/2) +(height/4)))
        angle = (x, y, 5, 5)
        cv2.rectangle(img, angle, color, -1)
        pts = np.append(pts, np.array([[x, y]]), axis = 0)

# ベース画像
def createBaseImage():
    size = (480, 640, 3)
    color = (0., 0., 0.,)
    img = np.full(size, color, dtype = np.uint8)

    color = (255, 255, 255)
    __setNoise(img, color)
    return img


if __name__ == "__main__":
    pts = np.empty((0, 2), int)
    print(cv2.__version__)
    __main()

