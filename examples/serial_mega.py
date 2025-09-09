import serial, threading, sys

PORT = '/dev/ttyUSB0'
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=0.2)
ser.reset_input_buffer()

def reader():
    while True:
        try:
            line = ser.readline()  # reads until \n or timeout
            if line:
                print("[ARDUINO]", line.decode(errors='ignore').rstrip())
        except Exception as e:
            print("Reader error:", e)
            break

t = threading.Thread(target=reader, daemon=True)
t.start()

print("Type commands like: pm1:3 (Ctrl+C to quit)")
try:
    while True:
        msg = input()
        # ensure newline so Arduino's readStringUntil('\n') returns
        ser.write((msg + "\n").encode())
except KeyboardInterrupt:
    pass
finally:
    ser.close()
    print("\nClosed.")
