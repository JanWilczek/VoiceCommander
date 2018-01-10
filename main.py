import admin
import listen_for_commands
from CommandHandler import CommandHandler

if __name__=="__main__":
    if not admin.isUserAdmin():
        admin.runAsAdmin()
    listen_for_commands()
    # Here comes handling the recording in 'command.wav'
    # (response/command, args) = ...
    handler = CommandHandler()
    # handler.handle(command,args)
