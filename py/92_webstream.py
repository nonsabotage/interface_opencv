import cv2
import bottle
import time

web = bottle.Bottle()

def __main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    if not cap.isOpened():
        print ("Not Opened Video Camera")
        exit()

    while True:
        ret, img = cap.read()

        if not ret:
            print("Video Capture Err")
            break

        result, jpgImg = cv2.imencode(".jpg", img = img, params = [int(cv2.IMWRITE_JPEG_QUALITY), 80])
        yield b'--frame\r\n' + b'Content-Type:image/jpeg\r\n\r\n' + bytearray(jpgImg) + b'\r\n\r\n'
        time.sleep(1 / 60)

    cap.release()
    cap.destroyAllWindows()

    return 0

@web.route("/")
def main():
    return bottle.static_file("index.html", root = "./")

@web.route("/video_recv")
def video_recv():
    bottle.response.content_type = "multipart/x-mixed-replace;boundary=frame"
    return __main()

if __name__ == "__main__":
    print(cv2.__version__)
    web.run(host = "localhost", port = 8080, reloader = True, debug = True)



    


