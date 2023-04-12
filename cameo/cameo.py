import cv2
import filters_13 as filters
from managers_10 import WindowManager, CaptureManager

class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo',
                                            self.onKeypress)

        self._captureManager = CaptureManager(cv2.VideoCapture("resource/spot-demo.MOV"), 
                                              self._windowManager, False)
        
        self._curveFilter = filters.SharpenFilter()

    def run(self):
        """Run the main loop."""
        self._windowManager.createWindow()

        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            
            # TODO: Filter the frame (Chapter 3).
            #filters.strokeEdges(frame, frame)
            self._curveFilter.apply(frame, frame)
            
            self._captureManager.setfilteredFrame(frame)
            self._captureManager.exitFrame()
            self._windowManager.processEvents()
    
    def onKeypress (self, keycode):
        """Handle a keypress.
        space  ->  Take a screenshot.
        tab    ->  Start/stop recording a screencast.
        escape ->  Quit.
        """
        
        if keycode == 32: # space
            print("Saving screenshot")
            self._captureManager.writeImage('resource/screenshot.png')
        
        
        elif keycode == 9: # tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('resource/screencast.avi')
            
            else:
                self._captureManager.stopWritingVideo()
        
        elif keycode == 27: # escape
            self._windowManager.destroyWindow()

if __name__=="__main__":
    Cameo().run()
