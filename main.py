from concurrent.futures import thread
from logging import Logger, NullHandler
import time
import datetime
import threading
from typing_extensions import Self
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk.web import client
import cv2
import command
import settings
from runtime_config import Config


# ボットトークンとソケットモードハンドラーを使ってアプリを初期化します
app = App(token=settings.BOT_TOKEN)
run_config = Config()
logger = Logger("main")


@app.event("reaction_added")
def call_reaction_added(event, say):
    # イベントがトリガー
    say(f"<@{event['user']}> reaction_added :{event['reaction']}: to {event['item']['ts']} of <@{event['item_user']}>:");
    print(event)



@app.event("message")
def call_message(event, say):
    command.ExeCmd.input_command(event["text"])
    
    return
    

    logger.info(res)



class Camera:
    def __init__(self) -> None:
        self.buffer_time = 0
    
    def take_picture(self):
        yield
        while True:

            self.buffer_time += 1
            
            if (self.buffer_time >= run_config.shot_interval):
                self.buffer_time = 0
                
                cap = cv2.VideoCapture(0) # /dev/video*
                ret, frame = cap.read()
                cv2.imwrite('temp.jpg', frame)

                print("try upload file")
                res = app.client.files_upload(
                    channels=settings.POST_CHANEL,
                    #initial_comment="Here's my file :smile:",
                    file=f"./temp.jpg",
                )
                
            time.sleep(60)


    





# 初期指定チャンネルに投稿
def post_mes(send: str):
	app.client.chat_postMessage(
		token=settings.BOT_TOKEN,
		channel= settings.POST_CHANNEL,
		text= send,
	)


# ログを書く
def write_log(tag, content):
    print(f"[{tag}: {datetime.datetime.now()}]:\n{content}\n")
    #logger.info(content)
 

@app.message("hello")
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    say(f"Hey there <@{message['user']}>!")



# アプリを起動します
if __name__ == "__main__":
    
    #camera = Camera()
    #thr = threading.Thread(target=camera.take_picture())
    #thr.start()
    
    SocketModeHandler(app, settings.SLACK_APP_TOKEN).start()




