import speech_recognition as sr
import pyaudio
import os
import webbrowser
import sys

r = sr.Recognizer()

commands_dict = {
    'commands': {
        'task_mgr': ['открой диспетчер задач', 'открыть диспетчер задач'],
        'control_panel': ['открой панель управления', 'открыть панель управления'],
        'open_folder': ['открой папку', 'открыть папку'],
        'exit_pr': ['выход из программы', 'выйти из программы'],
        'power_off': ['выключи компьютер', 'выключить компьютер']},
   }


def listen_command():
    try:
        with sr.Microphone() as mic:
            r.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = r.listen(source=mic)
            query = r.recognize_google(audio_data=audio, language="ru-RU").lower()
        return query
    except sr.UnknownValueError:
        return 'error'


query = listen_command()
print(query)

def task_mgr():
    os.startfile('Taskmgr.exe')


def control_panel():
    os.startfile('control.exe')


def open_folder():
    os.system(r"explorer.exe C:\Users\user")


def exit_pr():
    sys.exit('выключаюсь')


def div():
    s = query.split(' ')
    n = int(s[1])
    m = int(s[3])
    print(n / m)


def power_off():
    os.system('shutdown -s -t 0')


def search():
    s = query.split(' ')
    q = ''
    for i in range(3,len(s)):
        q += s[i]
        q += ' '
    print(q)
    webbrowser.open('https://www.google.com/search?q=' + q)


def main():
    for k, i in commands_dict['commands'].items():
        if query in i:
            print(globals()[k]())
    if 'раздели' in query or 'разделить' in query:
        return div()
    elif 'поиск по запросу' in query or 'найди в интернете' in query or 'найти в интернете' in query or 'поиск в интернете' in query:
        return search()


if __name__ == '__main__':
    main()

