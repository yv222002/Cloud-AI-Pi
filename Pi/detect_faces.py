import picamera, sys
from time import sleep
from lib import detect, highlight, control
with picamera.PiCamera() as camera:
    camera.resolution = (1920,1920)
    camera.hflip = True
    camera.vflip = True
    camera.contrast = 0
    camera.brightness = 50
    while input('ENTER to detect, else to quit...') == '':
        camera.capture('faces.jpg')
        faces = detect.faces('faces.jpg')
        print(len(faces), 'face(s) found!')
        highlight.highlight(faces, 'faces.jpg')
        print('faces-out.jpg created!')
        for face in faces:
            if detect.happy(face) == False:
                print('Pi guesses someone is NOT happy...')
                for _ in range(3):
                    control.move('j',0.2)
                    control.move('k',0.2)
                break
        else:
            for _ in range(len(faces)):
                control.move(sys.argv[1],float(sys.argv[2]))
                sleep(0.5)
    control.GPIO.cleanup()