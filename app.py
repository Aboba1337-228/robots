import tkinter as tk
import pyaudio
import speech_recognition as sr 

window = tk.Tk()
window.geometry("250x150")
window.resizable(False, False)

p = pyaudio.PyAudio()   
for i in range(p.get_device_count()):
   print(i, p.get_device_info_by_index(i)['name'])

r = sr.Recognizer()

def speech():
    with sr.Microphone(device_index=0) as sourse:
        txt_label.configure(text="Говорите")
        window.update()

        try:
            audio = r.listen(sourse, phrase_time_limit = 5, timeout=7)
            query = r.recognize_google(audio, language='ru-RU')
        except(sr.WaitTimeoutError, sr.UnknownValueError):
            txt_label.configure(text='Не понимать мана')
            window.update()
            speech()
        else:
            txt_label.configure(text='Готово')
            return query.capitalize()

def insert_rec():
    recording = speech()
    print(recording)


button_rec = tk.Button(window, text='Rec', command=insert_rec)
button_rec.place(x = 0, y = 10)

txt_label = tk.Label(window, text='Готов')
txt_label.place(x = 10, y = 80)

window.mainloop()
