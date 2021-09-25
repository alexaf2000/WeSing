import pygame
import cv2

def set_video():
    
    # Video framerate definition
    video_fps = 30
    # Loads video
    cap = cv2.VideoCapture('/Users/studiogenesis/Downloads/video_passandpay_tpv_inapp.mp4')

    success, img = cap.read()
    shape = img.shape[1::-1]
    wn = pygame.display.set_mode(shape)
    clock = pygame.time.Clock()

    while success:
        clock.tick(video_fps)
        success, img = cap.read()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                success = False
        wn.blit(pygame.transform.scale(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (1920,1080)), (0, 0))
        pygame.display.flip()
