import cv2
import numpy as np

if __name__ == "__main__":
    print(f"cv2 version is {cv2.__version__}")

    size = np.array([480, 640, 3])
    # 白のキャンバス
    img  = np.full(size, (255, 255, 255), dtype = np.uint8)
    color = np.array([0., 0., 255])

    cv2.arrowedLine(
        img = img, 
        pt1 = (30, 50), 
        pt2 = (320, 50), 
        color = color, 
        thickness = 5,
    )
    cv2.arrowedLine(
        img = img, 
        pt1 = (610, 100), 
        pt2 = (320, 100), 
        color = color, 
        thickness = 5,
    )
    cv2.arrowedLine(
        img = img, 
        pt1 = (0, 480), 
        pt2 = (320, 240), 
        color = color, 
        thickness = 5,
        line_type = cv2.LINE_AA,
    )


    cv2.imshow("Final result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
