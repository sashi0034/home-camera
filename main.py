import threading
from slack_bolt.adapter.socket_mode import SocketModeHandler
import bot
import settings
from slack_bolt import App


    

# アプリを起動します
if __name__ == "__main__":
    bot.app = App(token=settings.BOT_TOKEN)
    bot.run_config = bot.Config()
    
    @bot.app.event("reaction_added")
    def call_reaction_added(event, say):
        bot.call_reaction_added(event, say)

    @bot.app.event("message")
    def call_message(event, say):
        bot.call_message(event, say)
    
    camera = bot.Camera()
    thr = threading.Thread(target=camera.take_picture)
    thr.start()

    SocketModeHandler(bot.app, settings.SLACK_APP_TOKEN).start()

