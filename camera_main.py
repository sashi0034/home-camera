import threading
from slack_bolt.adapter.socket_mode import SocketModeHandler
import bot
import settings




# アプリを起動します
if __name__ == "__main__":
    @bot.app.event("reaction_added")
    def call_reaction_added(event, say):
        bot.call_reaction_added(event, say)

    @bot.app.event("message")
    def call_message(event, say):
        bot.call_message(event, say)
    
    bot.start_message()
    
    bot.thread_camera.setDaemon(True)
    
    bot.write_log("start now", "OK")
    
    bot.thread_camera.start()
    bot.thread_slack_event.connect()
    
    while True:
        if bot.run_config.is_alive == False:
            bot.write_log("main thread", "exit")
            exit()



