from concurrent.futures import thread
from logging import Logger, NullHandler
import time
import datetime
import threading
from slack_bolt import App

from slack_sdk.web import client
import subprocess
from subprocess import PIPE
import command
import settings
from runtime_config import Config
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import math


# ボットトークンとソケットモードハンドラーを使ってアプリを初期化します
app = App(token=settings.BOT_TOKEN)


# 初期指定チャンネルに投稿
def post_mes(send: str):
	app.client.chat_postMessage(
		token=settings.BOT_TOKEN,
		channel= settings.POST_CHANNEL,
		text= send,
	)


def call_reaction_added(event, say):
# イベントがトリガー
    say(f"<@{event['user']}> reaction_added :{event['reaction']}: to {event['item']['ts']} of <@{event['item_user']}>:");
    write_log("reaction added", event)


def call_message(event, say):
    command.ExeCmd.input_command(event["text"])  
    return


class Camera:
    def __init__(self) -> None:
        self.buffer_time = 0
    
    def take_picture(self):
        
        global run_config
        while True:
            time.sleep(10)
            self.buffer_time += 10
            
            write_log("can take", run_config.can_picture)
            
            if (self.buffer_time >= run_config.shot_interval):
                self.buffer_time = 0
                
                if (run_config.can_picture == False):
                    continue
                
                proc = subprocess.run("fswebcam temp.jpg", shell=True, stdout=PIPE, stderr=PIPE, text=True)
                write_log("try upload file", proc)
                
                try:
                    res = app.client.files_upload(
                        channels=settings.POST_CHANNEL,
                        #initial_comment="Here's my file :smile:",
                        file=f"./temp.jpg",
                    )
                    #write_log("upload result", res)
                except Exception as e:
                    write_log("upload error", e)
                    
                


def start_message():
    f = open("log.in", "r")
    data = f.read()
    post_mes(data[max([0, len(data)-4000]):])
    f.close






# ログを書く
def write_log(tag, content):
    print(f"[{tag}: {datetime.datetime.now()}]:\n{content}\n")
    #logger.info(content)
 

@app.message("hello")
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    say(f"Hey there <@{message['user']}>!")




run_config = Config()
camera = Camera()
thread_camera: threading.Thread = threading.Thread(target=camera.take_picture)
thread_slack_event: SocketModeHandler = SocketModeHandler(app, settings.SLACK_APP_TOKEN)



