import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

pose = mp_pose.Pose(
    static_image_mode=False,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

def detectPose(image, draw=True):
    """
    Processes the image to detect human pose landmarks using MediaPipe.
    Args:
        image: The input frame from the webcam.
        draw: Boolean to decide if landmarks should be drawn on the frame.
    """
    output_image = image.copy()
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    if results.pose_landmarks and draw:
        mp_drawing.draw_landmarks(
            output_image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )

    return output_image, results
