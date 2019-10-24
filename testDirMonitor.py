import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import os
#dd

import sys
import pytesseract
import cv2


import tkinter as tk
from tkinter import messagebox

import stringdist

class ImagesEventHandler(LoggingEventHandler):
    def __init__(self):
        pass

    def on_created(self, event):
        imgPath = event.src_path
        _ , ext = os.path.splitext(imgPath)
        #print(filename)
        
        
        #step 1. check if image file
        ext = ext.lower()
        if(ext ==".jpg" or ext ==".jpeg" or ext==".png" or ext==".bmp"):
            
            #step 2 อ่านข้อความจากภาพ
            imgSrc = cv2.imread(imgPath, 0)
            text = pytesseract.image_to_string(imgSrc, lang='tha') #.replace("/", "_").replace("เ", "เอ").replace("แ", "แอ").replace("้", "อ้").replace("่", "อ่").replace("ฅ", "ฐ").replace("ฃ", "slash").replace("ฺ", "dot").replace("๊", "อ๊").replace("๋", "อ๋").replace("ุ", "อุ").replace("ู", "อู").replace("ิ", "อิ").replace("ี", "อี").replace("ึ", "อึ").replace("ื", "อื").replace(".", "อำ").replace("โ", "โอ").replace("ไ", "ไอ").replace("ใ", "ไอ").replace("ฯ", "ไปยางน้อย").replace("ๆ", "ยามก").replace("์", "การัน").replace("ั", "อะ").replace("า", "อา")
            #ให้นำไปสร้างเป็นชื่อ folder ได้
           

            #step 3 เอาข้อความไปวิ่งเทียบกับ folder ที่ใกล้เคียง




            #stringdist.levenshtein('test', 'testing')
            root= tk.Tk() # create window
            canvas1 = tk.Canvas(root, width = 300, height = 300)
            canvas1.pack()

            def btn1_onClick():
                #MsgBox = tk.messagebox.askquestion ('Exit Application' + text,'Are you sure you want to exit the application',icon = 'warning')
                #if MsgBox == 'yes':
                root.destroy()
                #   print(text)
                #else:
                pass

            def btn2_onClick():
                #MsgBox = tk.messagebox.askquestion ('Exit Application' + text,'Are you sure you want to exit the application',icon = 'warning')
                #if MsgBox == 'yes':
                root.destroy()
                #   print(text)
                #else:
                pass
                #     tk.messagebox.showinfo('Return','You will now return to the application screen')
                    
            
            canvas1.create_window(150, 150, window=tk.Button(root, text='Yes',command=btn1_onClick))
            canvas1.create_window(75, 75, window=tk.Button(root, text='Exit',command=btn2_onClick))
            canvas1.create_window(10,10,window =  tk.Label(root, text=text))
            
            root.mainloop()

            #cv2.imshow('imgSrc', imgSrc)
            #while(True):
            #    if cv2.waitKey(1000//12) & 0xff == ord("q"):
            #        cv2.destroyAllWindows()
            #        exit()


        else:
            print("file is not an image.!")




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = ImagesEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()