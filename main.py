import os
from logging import Logger
import requests
import shutil
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


@app.event("reaction_added")
def call_reaction_added(event, say):
    # イベントがトリガー
    say(f"<@{event['user']}> reaction_added :{event['reaction']}: to {event['item']['ts']} of <@{event['item_user']}>:");
    print(event)



@app.event("message")
def call_message(event, say):
    command.ExeCmd.input_command(event["text"])
    
    return
    
    say("写真を送信します")
    
    cap = cv2.VideoCapture(0) # /dev/video*
    ret, frame = cap.read()
    cv2.imwrite('test.jpg', frame)

    print("try upload file")
    res = app.client.files_upload(
        channels=settings.POST_CHANEL,
        initial_comment="Here's my file :smile:",
        file=f"./test.jpg",
    )

    logger.info(res)








# 初期指定チャンネルに投稿
def post_mes(send: str):
	app.client.chat_postMessage(
		token=settings.BOT_TOKEN,
		channel= settings.POST_CHANNEL,
		text= send,
	)




@app.message("hello")
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    say(f"Hey there <@{message['user']}>!")



# アプリを起動します
if __name__ == "__main__":
    SocketModeHandler(app, settings.SLACK_APP_TOKEN).start()




