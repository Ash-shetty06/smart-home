# 🏠 Smart Home Control System

This project is an **assignment implementation** of a Smart Home System.  
It provides a **menu-driven program** where users can manage different smart devices (Fan, Light, AC, Washing Machine, etc.), control their settings, and create/view/manage schedules.

---

## 📂 Project Structure

├── main.py # Menu-driven program
├── device.py # Base class for all devices
├── device_manage.py # DeviceManager class (add/remove/view devices)
├── schedule.py # Schedule and ScheduleManager classes
├── fan.py # Fan subclass (with speed)
├── light.py # Light subclass (with brightness)
├── ac.py # AC subclass (with temperature)
├── washing_mac.py # WashingMachine subclass (with mode)

## ⚙️ Features

- **Device Management**
  - Add new devices
  - View all devices
  - Get device status

- **Device Control**
  - Turn ON/OFF devices
  - Adjust settings (brightness, speed, temperature, mode)

- **Scheduling**
  - Create schedules for devices
  - Update / Delete schedules
  - Auto-control devices based on schedule and current time

🖥️ Example Menu
Smart Home Menu
1. Add Device
2. List All Devices
3. Get Device Status
4. Control Device (ON/OFF)
5. Create Device Schedule
6. Manage Device Schedule
7. View All Schedules
8. Exit

📌 Example Usage

Add a Light named "BedroomLight"

Set its brightness to 80%

Create a schedule from 18:00 to 22:00

At runtime, the system auto-turns ON the light during that period
