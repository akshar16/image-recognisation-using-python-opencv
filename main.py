import cv2
import google.generativeai as genai
import base64
import time

API_KEY = "YOUR_API_KEY"
if not API_KEY:
    raise ValueError("API key missing")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash-exp')


def enc_img(img):

    _, buf = cv2.imencode('.jpg', img)
    return base64.b64encode(buf).decode('utf-8')

def split_text(text, words_per_line):
    words = text.split()
    lines = []

    for i in range(0, len(words), words_per_line):

        line = " ".join(words[i:i+words_per_line])
        lines.append(line)
    return lines

def proc_vid(src='camera', vid_path=None, skip=5, max_f=20, txt_dur=30):

    if src == 'camera':
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("cant open cam")
            return

    elif src == 'file':
        if not vid_path:
            print("Need path for vid file")
            return

        cap = cv2.VideoCapture(vid_path)
        if not cap.isOpened():
            print(f"cant open {vid_path}")
            return

    else:
        print("Bad source")
        return

    f_cnt = 0
    f_num = 0
    show_txt = False
    txt_start = 0
    rsp_txt = ""

    while True:

        ret, frame = cap.read()
        if not ret:

            print("end of vid")
            break

        f_num += 1

        if f_num % skip != 0:
            if show_txt and time.time() - txt_start <= txt_dur:
                lines = split_text(rsp_txt, 15)
                y_off = 30

                for line in lines:
                    cv2.putText(frame, line, (10, y_off), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0, 0), 2, lineType=cv2.LINE_AA)
                    y_off += 30

            cv2.imshow("Stream", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            continue

        if f_cnt >= max_f:
            print(f"done with {max_f}")
            break

        b64_img = enc_img(frame)
        prompt = "Describe the object closet to the camera in 50 words"

        try:
            rsp = model.generate_content([prompt, {"mime_type": "image/jpeg", "data": b64_img}])
            print("Gemini says:")
            print(rsp.text)
            rsp_txt = rsp.text
            show_txt = True
            txt_start = time.time()

        except Exception as e:
            print(f"err: {e}")
            rsp_txt = f"Error: {e}"
            show_txt = True
            txt_start = time.time()

        if show_txt and time.time() - txt_start <= txt_dur:

            lines = split_text(rsp_txt, 20)
            y_off = 30

            for line in lines:
                cv2.putText(frame, line, (10, y_off), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2, lineType=cv2.LINE_AA)
                y_off += 30


        cv2.imshow("Stream", frame)
        f_cnt += 1
        key = cv2.waitKey(1)

        if key == ord('q'):

            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    proc_vid(src='camera', skip=5, txt_dur=30)