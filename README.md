# ros2_chat
![test](https://github.com/rupa-04/ros2_chat/actions/workflows/test.yml/badge.svg)

ros2_chatはROS2のトピック通信を用いて、チャット風のメッセージ通信を行うROS2パッケージです。

## ノードの機能
**chat_talker**
- 役割：メッセージの送信
- 動作：
    - ユーザが端末から入力した文字列を取得
    - メッセージとしてトピックにPublish

**chat_listener**
- 役割：メッセージの受信
- 動作：
    - 指定されたトピックをSubscribe
    - 受信したメッセージを標準出力に表示

## トピックの機能
**/chat**
- メッセージ型：std_msgs/msg/String
- 通信内容：チャットメッセージ(文字列)
- Publisher：chat_talker
- Subscriber：chat_listener

## 使用方法
- ノードを個別に起動する場合

別々のターミナルで以下を実行します。
```
(ターミナル1)
$ ros2 run ros2_chat chat_talker
```
```
(ターミナル2)
$ ros2 run ros2_chat chat_listener
```

chat_talkerを起動すると以下の内容が表示され、名前とメッセージの入力を求められます。
```
あなたの名前を入力してください： rupa-
[INFO][1767136966.470932434][chat_talker]: メッセージを入力し、Enterキーを押すと送信されます。
こんにちは
元気ですか？
```

chat_listenerを起動すると以下の内容が表示されます。
```
[INFO][1767137033.415672377][chat_listener]: rupa-: こんにちは 
[INFO][1767137051.812978855][chat_listener]: rupa-: 元気ですか？
```

- launchファイルを使用する場合

PublisherとSubscriberを同時に起動することができます。
```
$ ros2 launch ros2_chat chat.launch.py
```

## 必要なソフトウェア
- Python
- ROS2

## テスト環境
- Ubuntu 24.04 LTS

## ライセンス
- このソフトウェアは、3条項BSDライセンスの下、再頒布および使用が許可されます。
- ©2025 rupa-04
