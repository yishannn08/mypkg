import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from person_msgs.srv import Query

rclpy.init()                     #rclpyの初期化（最初に1回）
node = Node("talker")

def cb(request, response):               #タイマーで定期的に呼ばれるコールバック関数
    if request.name == "Yi Shan" :
        response.age = 21           #関数を抜けてもnがリセットされないようにしている
    else:
        response.age = 255
    return response

def main():
    srv = node.create_service(Query,"query", cb)
    rclpy.spin(node)            #実行（無限ループ。タイマーや送受信を処理し続ける）

