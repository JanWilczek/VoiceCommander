from CommandHandler import CommandHandler

command_handler = CommandHandler()
command_handler.handle('execute', 'chrome.exe')
command_handler.handle('execute', 'edge')
command_handler.handle('execute', 'notepad')
command_handler.handle('execute', 'explorer')

