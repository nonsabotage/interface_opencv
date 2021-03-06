import cv2
import numpy as np

if __name__ == "__main__":
    print(cv2.__version__)

    size = np.array([480, 640, 3])
    # 白のキャンバス
    img  = np.full(size, (255, 255, 255), dtype = np.uint8)
    color = np.array([0., 0., 255])

    # 直線の描画
    cv2.rectangle(
        img = img, 
        pt1 = (0, 240), 
        pt2 = (640, 24), 
        color = color, 
        thickness = -1, # 塗りつぶし
    )
    cv2.rectangle(
        img = img, 
        pt1 = (0, 0), 
        pt2 = (640, 480), 
        color = color, 
        thickness = 1,
    )

    cv2.imshow("Final result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
