from pywinauto.application import Application
from pywinauto.keyboard import SendKeys
from pywinauto.mouse import scroll
from CommandRecorder import CommandRecorder
from dictate import interpret_dication
from logger import log
from win32api import GetCursorPos
from os import remove, _exit


class CommandHandler:

    def __init__(self):
        # TODO: Put these into a seperate "Paths" module (maybe a JSON file?)
        self.chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        self.edge_path = 'C:\Windows\SystemApps\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\MicrosoftEdge.exe' # doesn't work
        self.notepad_path = 'notepad.exe'
        self.explorer_path = 'C:/Windows/explorer.exe'
        self.opera_path = ''

    def handle(self, command, *args, **kwargs):
        """ Execute a given command.
        :param command: string containing the command
        :param args: optional command args
        :param kwargs: optional command kwargs
        """

        if command == "run":
            self.__execute(args)
        elif command == "dictate":
            dictation_recorder = CommandRecorder()
            filename = "dictation.wav"
            log("Listening to dictation...")
            dictation_recorder.record_for_seconds(filename=filename, record_seconds=10)
            log("Dictation ended.")
            transcription = interpret_dication(filename)
            log("Transcription: ", transcription)
            remove(filename)
        elif command == "enter":
            SendKeys('{ENTER}')
        elif command == "home":
            SendKeys('{HOME}')
        elif command == "desktop":
            SendKeys('{LWIN}d')  # does it work?
        elif command == "next_window":
            SendKeys('%{ESC}')
        elif command == "up":
            scroll(coords=GetCursorPos(), wheel_dist=7)
        elif command == "down":
            scroll(coords=GetCursorPos(), wheel_dist=-7)
        elif command == "select_all":
            SendKeys('^a')
        elif command == "copy":
            SendKeys('^c')
        elif command == "paste":
            SendKeys('^v')
        elif command == "save":
            SendKeys('^s')
        elif command == "undo":
            SendKeys('^z')
        elif command == "find":
            SendKeys('^f')
            keyword_recorder = CommandRecorder()
            filename = "keyword.wav"
            log("What to find?")
            keyword_recorder.record_for_seconds(filename=filename, record_seconds=2)
            keyword = interpret_dication(filename)
            log("Szukam ", keyword)
            SendKeys(keyword[1:len(keyword) - 1] + '{ENTER}', with_spaces=True)
            remove(filename)
        elif command == "google":     # WIP
            app = Application(backend='uia')
            app.start(self.chrome_path + ' --force-renderer-accessibility https://www.google.com')
            keyword_recorder = CommandRecorder()
            filename = "keyword.wav"
            log("What to google?")
            keyword_recorder.record_for_seconds(filename=filename, record_seconds=3)
            keyword = interpret_dication(filename)
            log("Googling ", keyword)
            SendKeys(keyword[1:len(keyword)-1] + '{ENTER}', with_spaces=True)
            remove(filename)
        elif command == "youtube":
            app = Application(backend='uia')
            app.start(self.chrome_path + ' --force-renderer-accessibility https://www.youtube.com')
        elif command == "close":
            SendKeys('%{F4}')
        elif command == "end_commander":
            _exit(0)
        elif command == "yoda":
            app = Application(backend='uia')
            app.start(self.chrome_path + ' --force-renderer-accessibility https://youtu.be/bYRYHLUNEs4?t=18')
        elif command == "private_browsing":
            app = Application(backend='uia')
            app.start(self.chrome_path + ' --force-renderer-accessibility https://www.youtube.com/watch?v=x6QZn9xiuOE')
            SendKeys('^+n')
            SendKeys('chicks' + '{ENTER}', with_spaces=True)
            log("Have fun!")
        else:
            raise NotImplementedError('Unknown command!')

    def __execute(self, args):
        if args is not None:
            # Handle the execute command
            app = Application()
            if args[0] == 'chrome' or args[0] == 'chrome.exe':
                app.start(self.chrome_path)
            elif args[0] == 'opera' or args[0] == 'opera.exe':
                app.start(self.opera_path)
            elif args[0] == 'edge' or args[0] == 'edge.exe':
                app.start(self.edge_path)
            elif args[0] == 'notepad':
                app.start(self.notepad_path)
            elif args[0] == 'explorer':
                app.start(self.explorer_path)
            else:
                raise NotImplementedError('Given program handling not implemented!')
        else:
            raise Exception('Specify the program to launch!')

