import admin

if not admin.isUserAdmin():
    admin.runAsAdmin()
from pywinauto.application import Application

class CommandHandler:

    def __init__(self):
        # Put these into a seperate "Paths" module (maybe a JSON file?)
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

        if command=="execute":
            if args is not None:
                # Handle the command
                app = Application()
                if args[0]=='chrome' or args[0]=='chrome.exe':
                    app.start(self.chrome_path)
                elif args[0]=='opera' or args[0]=='opera.exe':
                    app.start(self.opera_path)
                elif args[0]=='edge' or args[0]=='edge.exe':
                    app.start(self.edge_path)
                elif args[0]=='notepad':
                    app.start(self.notepad_path)
                elif args[0]=='explorer':
                    app.start(self.explorer_path)
                else:
                    raise NotImplementedError('Given program handling not implemented!')
            else:
                raise Exception('Specify the program to launch!')