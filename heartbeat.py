import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


cap = cv2.VideoCapture(0)


face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


frame_numbers = []
avg_r_values = []
avg_g_values = []
avg_b_values = []


plt.ion()
fig, ax = plt.subplots()
(line_r,) = ax.plot([], [], "r-", label="Avg R")
(line_g,) = ax.plot([], [], "g-", label="Avg G")
(line_b,) = ax.plot([], [], "b-", label="Avg B")
ax.set_xlim(0, 300)
ax.set_ylim(0, 255)
ax.set_xlabel("Frame Number")
ax.set_ylabel("Average RGB Value")
ax.legend()

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cap.set(cv2.CAP_PROP_FPS, 30)
    frame_count += 1

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        face_roi = rgb_frame[y : y + h, x : x + w]

        avg_r = np.mean(face_roi[:, :, 0])
        avg_g = np.mean(face_roi[:, :, 1])
        avg_b = np.mean(face_roi[:, :, 2])

        frame_numbers.append(frame_count)
        avg_r_values.append(avg_r)
        avg_g_values.append(avg_g)
        avg_b_values.append(avg_b)

        if len(frame_numbers) > 300:
            frame_numbers.pop(0)
            avg_r_values.pop(0)
            avg_g_values.pop(0)
            avg_b_values.pop(0)

        line_r.set_data(frame_numbers, avg_r_values)
        line_g.set_data(frame_numbers, avg_g_values)
        line_b.set_data(frame_numbers, avg_b_values)

        ax.set_xlim(max(0, frame_count - 300), frame_count)
        plt.draw()
        plt.pause(0.01)

        if len(avg_g_values) > 30:
            peaks, _ = find_peaks(avg_g_values, distance=15)
            peak_intervals = np.diff(peaks)
            if len(peak_intervals) > 0:
                avg_peak_interval = np.mean(peak_intervals)
                heart_rate = 60 / (avg_peak_interval / 30)

                cv2.putText(
                    frame,
                    f"Heart Rate: {heart_rate:.2f} BPM",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                )

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
plt.ioff()
plt.show()
