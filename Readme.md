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
bash
git clone (https://github.com/Parth-bot-crypto26/Subway-Surfers-Pose-Control.git)
cd subway-surfers-pose-control

### 2. Run the Controller
Execute the main script to start the webcam feed and gesture recognition system:
Bash
python main.py


## 🎮 How to Play
Once the script is running, follow these steps to play the game:

**Step 1: Prepare the Environment**
   1. **Launch the Game:** Open your web browser and navigate to a Subway Surfers game (e.g., on Poki or similar sites).

   2. **Position the Windows:** Make sure the browser window is visible on your screen. The Python script window ("Subway Surfers with Pose Control") should also be visible so you can see your video feed.

   3. **Stand Back:** Position yourself 3-5 feet away from the camera. Ensure your head and shoulders are clearly visible in the frame.


**Step 2: Start & Calibrate**
To start the game, perform the "Namaste" / Prayer Gesture:

Join your hands together in front of your chest.

Hold this pose for about 1 second (until the text on screen confirms).

Automatic Action: The system will:

   * Calibrate your height (distinguishing between standing, jumping, and crouching).

   * Automatically click the center of the screen to focus the game window.

   * Press Space to start running.


**Step 3: Game Controls**
| **Action**       | **Body Gesture**                               | **Keyboard Equivalent** |
|------------------|----------------------------------------|                                 |
| ReactJS           | Frontend framework                    |                                 |
| JSX, HTML, CSS    | Structure & styling                   |                                 |
| Firebase          | Auth & database                        |                                |
| Framer Motion     | Smooth animations                      |                                |
| GSAP              | Mascot animations                      |                                |
| Responsive Design | Mobile & desktop support               |                                |
**Action**             **Body Gesture**                        **Keyboard Equivalent**
Move Left              Lean your body to the left                    Left Arrow
Move Right             Lean you body to the right                    Right Arrow
Stay in Lane           Stand straight in the center                   (No Key)
   Jump                Stand tall or Jump(Shoulders move up)          Up Arrow
 Roll/Duck             Crouch down (Shoulders move down)              Down Arrow

**💡 Pro Tip:** Try to return to a neutral "Standing" position in the center after dodging obstacles to reset your movement

