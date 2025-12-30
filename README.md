# ros2_chat
![test](https://github.com/rupa-04/ros2_chat/actions/workflows/test.yml/badge.svg)

ros2_chatはROS2のトピック通信を用いて、チャット風のメッセージ通信を行うROS2パッケージです。chat_talkerとchat_listenerの二つのノードを用いて、メッセージの送受信を行います。

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
