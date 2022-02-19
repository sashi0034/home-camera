# home-camera

# 📋 概要

ラズパイで撮影してSlack上で管理する防犯カメラです

# 🎥 実行

`settings.py`に`BOT_TOKEN`, `POST_CHANNEL`, 'SLACK_APP_TOKEN'を書き込んで保存します

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




