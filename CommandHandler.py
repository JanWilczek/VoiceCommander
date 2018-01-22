import admin
if not admin.isUserAdmin():
    admin.runAsAdmin()

from pywinauto.application import Application
from pywinauto.keyboard import SendKeys
from pywinauto.mouse import scroll
from CommandRecorder import CommandRecorder
from win32api import GetCursorPos

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

        if command=="run":
            self.__execute(args)
        elif command=="start_dictation":    # not implemented
            raise NotImplementedError('Dictation not implemented')
            dictation_recorder = CommandRecorder()
            dictation_recorder.record_for_seconds(filename="dictation.wav", record_seconds=-1)
            # additional code
        elif command=="home":
            SendKeys('{HOME}')
        elif command=="desktop":
            SendKeys('{LWIN}d')  # does it work?
        elif command=="up":
            scroll(coords=GetCursorPos(), wheel_dist=10)
        elif command=="down":
            scroll(coords=GetCursorPos(), wheel_dist=-10)
        elif command=="select_all":
            SendKeys('^a')
        elif command=="copy":
            SendKeys('^c')
        elif command=="paste":
            SendKeys('^v')
        elif command == "save":
            SendKeys('^s')
            if args is not None:
                SendKeys(str(args[0]) + '{ENTER}')
        elif command=="undo":
            SendKeys('^z')
        elif command=="google":     # WIP
             app = Application(backend='uia')
             app.start(self.chrome_path + ' --force-renderer-accessibility https://www.google.com')
             #SendKeys("google.com{ENTER}")
             if args is not None:
                app_new_tab = Application(backend='uia').connect(path='chrome.exe', title_re='New Tab')
                #app_new_tab.window().type_keys(str(args[0]) + '{ENTER}')
                SendKeys(str(args[0]) + '{ENTER}')
        elif command=="close":
            SendKeys('%{F4}')
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