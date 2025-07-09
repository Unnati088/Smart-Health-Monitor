# Smart Health Monitor (C + Python Project)

🚀 A mini project combining C and Python to simulate a **health monitoring system**, just like in smartwatches or fitness trackers.

## 🔧 How It Works

- `health_sensor.c` (C): Simulates hardware-level sensors, generates heart rate and temperature data, and writes to `sensor_data.txt`.
- `health_monitor.py` (Python): Reads data, logs it to CSV, checks for abnormalities, and plots readings with `matplotlib`.

## 📦 Technologies Used

- C for low-level data generation
- Python for:
  - File I/O
  - CSV logging
  - Data visualization using `matplotlib`

## ▶️ How to Run

```bash
gcc health_sensor.c -o sensor && ./sensor
python health_monitor.py
