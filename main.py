from ultralytics import YOLO
import cv2
import pygame
import os
import time

def perform_detection(model, image_path):
    return model.predict(source=image_path, save=True, show=True)

def check_and_play_alarm(results):
    for result in results:
        print("Bounding boxes:", result.boxes)  
        print("Class names:", result.names)  
        print("Class IDs:", result.boxes.cls)  
        print("Confidence scores:", result.boxes.conf)  
        
        
        for cls_id in result.boxes.cls:
            label = result.names[int(cls_id)]
            print("Detected label:", label)  
            if label == 'fire' or label == 'smoke':
                print("Alarm! Fire or smoke detected!")
                try:
                    if not pygame.mixer.get_init():
                        pygame.mixer.init()
                        print("Pygame mixer initialized.")
                    
                    
                    alarm = pygame.mixer.Sound('alarm.wav')
                    alarm.play()
                    print("Alarm sound playing.")
                    time.sleep(2)  
                except Exception as e:
                    print(f"Error playing sound: {e}")
                return  

def main():
    alarm_sound = 'alarm.wav'
    if not os.path.exists(alarm_sound):
        print(f"Error: {alarm_sound} not found!")
        return
        
    model_path = 'fire_and_smoke_model.pt'
    image_path = 'test.jpeg'

    
    pygame.init()
    pygame.mixer.init()
    print("Pygame initialized.")

    model = YOLO(model_path)
    results = perform_detection(model, image_path)
    check_and_play_alarm(results)

if __name__ == "__main__":
    main()

