import cv2
import random
import time
import tkinter as tk
from tkinter import messagebox

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

def show_success_popup():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Verification", "EYe Blink Captcha Test successfully passed!")
    root.destroy()

def count_blinks(cap, required_blinks=3, timeout=20):
    blink_count = 0
    eye_closed_frames = 0
    eye_open_frames = 0
    blink_detected = False
    start_time = time.time()
    init_ignore_frames = 10  # Ignore first 10 frames to allow camera to stabilize
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Camera error")
            break

        frame_count += 1
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

        if frame_count <= init_ignore_frames:
            cv2.putText(frame, f"Initializing...", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            cv2.imshow('Eye Blink CAPTCHA', frame)
            if cv2.waitKey(30) & 0xFF == 27:
                break
            continue

        if len(eyes) == 0:
            eye_closed_frames += 1
            eye_open_frames = 0
        else:
            eye_open_frames += 1
            if eye_closed_frames > 2 and not blink_detected:
                blink_count += 1
                print(f"Blink detected: {blink_count}")
                blink_detected = True
            elif eye_open_frames > 2:
                blink_detected = False
            eye_closed_frames = 0

        cv2.putText(frame, f"Blink count: {blink_count}/{required_blinks}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Eye Blink CAPTCHA', frame)

        if blink_count >= required_blinks:
            print("Eye Blink Captcha Test successfully passed!")
            show_success_popup()
            break

        if (time.time() - start_time) > timeout:
            print("Timeout! Verification failed.")
            break

        if cv2.waitKey(30) & 0xFF == 27:
            print("User exited.")
            break

    cap.release()
    cv2.destroyAllWindows()
    return blink_count >= required_blinks

# --- MAIN ---

required_blinks = random.randint(2, 5)
print(f"Please blink your eyes {required_blinks} times within 20 seconds.")

cap = cv2.VideoCapture(0)

result = count_blinks(cap, required_blinks)

if result:
    print("CAPTCHA Verified: Human detected.")
else:
    print("CAPTCHA Failed: No human detected or timeout.")
