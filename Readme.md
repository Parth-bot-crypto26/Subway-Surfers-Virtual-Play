# 🎮 Subway Surfers Control Using Pose Detection

This project demonstrates a **real-time Human–Computer Interaction (HCI)** system where the game **Subway Surfers** is controlled using **body gestures** captured through a webcam.

Using **MediaPipe Pose**, **OpenCV**, and **PyAutoGUI**, the system detects human pose landmarks, interprets body movements, and converts them into **keyboard inputs** to control the game character.

---

## 📌 Features
* **Touchless Gameplay:** Play without touching the keyboard.
* **Gesture Recognition:**
    * **Start Game:** Join hands (Namaste pose) to start and calibrate.
    * **Lane Changing:** Lean Left or Right.
    * **Jumping & Crouching:** Stand tall to jump, duck down to crouch.
* **Real-time Processing:** Smooth performance using MediaPipe's lightweight pose detection.
* **Visual Feedback:** On-screen pose landmarks and FPS counter.

---

## 🛠️ Technologies Used
* **Python 3.x**
* **OpenCV:** For video capture and image processing.
* **MediaPipe:** For robust human pose estimation.
* **PyAutoGUI:** For simulating keyboard presses.

---

## 📁 Project Structure
Subway Surfers/
│
├── pose_utils.py # Pose detection logic
├── gesture_utils.py # Gesture detection functions
├── main.py # Final application (game controller)
├── requirements.txt
└── README.md


---

## 🚀 Getting Started

### 1. Clone the Repository
Open your terminal or command prompt and run:
```bash
git clone (https://github.com/Parth-bot-crypto26/Subway-Surfers-Pose-Control.git)
cd subway-surfers-pose-control
