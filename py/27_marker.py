import cv2
import numpy as np
import re

if __name__ == "__main__":
    print(f"cv2 version is {cv2.__version__}")

    size = np.array([480, 640, 3])
    # 白のキャンバス
    img  = np.full(size, (255, 255, 255), dtype = np.uint8)
    color = np.array([0., 0., 255])

    marker_types = [x for x in dir(cv2) if re.match("MARKER_", x)]
    idx = range(len(marker_types))

    for x, y, t in zip(idx, idx, marker_types):
        cv2.drawMarker(
            img = img, 
            position = (100 + x * 30, 100 + y * 30), 
            color = color, 
            markerType = eval(f"cv2.{t}")
        )


    cv2.imshow("Final result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
