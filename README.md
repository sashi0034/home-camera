# home-camera

# 📋 概要

ラズパイで撮影してSlack上で管理する防犯カメラです

# 🎒 準備

1. Webカメラを取り付けたラズパイ
2. `$ sudo apt-get install fswebcam`
3. `$ pip install slack_bolt` など
4. `settings.py`に`BOT_TOKEN`, `POST_CHANNEL`, `SLACK_APP_TOKEN`などを書き込みます


# 🎥 実行
```
$ nohup sh camera.sh &
```

で実行します

# 🧮 使い方

招待したボットがいるチャンネルで以下の操作ができます

コマンドを実行するときは`$`も含めます

- `$ ping`
- `$ stop`
- `$ start`
- `$ interval {seconds}`
- `$ kill`




