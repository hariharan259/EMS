# emg_overview_realtime.py

import time
import threading

# EMG function descriptions
emg_functions = [
    ("1. Muscle Activity Monitoring", "Detects and records electrical signals when muscles contract and relax."),
    ("2. Medical Diagnosis", "Helps diagnose neuromuscular disorders like ALS, myopathy, or nerve damage."),
    ("3. Biofeedback", "Provides real-time feedback for muscle training and rehabilitation therapy."),
    ("4. Prosthetic Control", "EMG signals are used to control artificial limbs (bionic arms, hands)."),
    ("5. Human-Computer Interaction (HCI)", "Used in gesture recognition and controlling devices using muscle signals."),
    ("6. Sports Science", "Monitors muscle performance, fatigue, and training effectiveness."),
    ("7. Research", "Used in biomechanics, robotics, and movement analysis.")
]

# 1️⃣ EMG Signal Reader via Serial (for OpenBCI or USB EMG)
def read_emg_serial(port='/dev/ttyUSB0', baudrate=115200):
    import serial
    try:
        ser = serial.Serial(port, baudrate)
        print("🔌 Serial EMG connected. Reading data...")
        while True:
            if ser.in_waiting > 0:
                raw_data = ser.readline().decode('utf-8').strip()
                print(f"📈 EMG Signal: {raw_data}")
    except Exception as e:
        print("❌ Serial EMG error:", e)

# 2️⃣ EMG Signal Reader via ADS1115 (for MyoWare analog sensors)
def read_emg_analog(channel=0):
    import board
    import busio
    from adafruit_ads1x15.analog_in import AnalogIn
    from adafruit_ads1x15.ads1115 import ADS1115

    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS1115(i2c)
    chan = AnalogIn(ads, getattr(ADS1115, f'P{channel}'))

    print("🔌 Analog EMG connected via ADS1115. Reading data...")
    while True:
        print(f"📈 EMG Signal: {chan.voltage:.3f} V")
        time.sleep(0.1)

# GUI display (optional)
def show_gui():
    import tkinter as tk

    root = tk.Tk()
    root.title("EMG Functions Overview")
    root.geometry("650x450")
    root.configure(bg="#e0f7fa")

    title = tk.Label(root, text="🔹 EMG Functional Overview 🔹", font=("Arial", 16, "bold"), bg="#e0f7fa")
    title.pack(pady=10)

    for title_text, desc_text in emg_functions:
        tk.Label(root, text=title_text, font=("Arial", 12, "bold"), bg="#e0f7fa", fg="#00796b").pack(anchor="w", padx=20)
        tk.Label(root, text="→ " + desc_text, font=("Arial", 10), bg="#e0f7fa").pack(anchor="w", padx=40, pady=2)

    root.mainloop()

# Terminal fallback
def show_terminal():
    print("\n🔹 EMG (Electromyography) Functional Overview 🔹\n")
    for title, desc in emg_functions:
        print(f"{title}\n   → {desc}\n")
        time.sleep(0.8)

# Entry point
if __name__ == "__main__":
    try:
        # Start GUI or terminal
        threading.Thread(target=show_gui).start()
    except:
        show_terminal()

    # 👇 Choose EMG source
    # threading.Thread(target=read_emg_serial, kwargs={'port': '/dev/ttyUSB0'}).start()     # For OpenBCI or USB
    # threading.Thread(target=read_emg_analog, kwargs={'channel': 0}).start()               # For MyoWare analog

