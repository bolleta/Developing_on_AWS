import json
import urllib.request

def lambda_handler(event, context):
    # 実行時の引数のパース
    msg = event["queryStringParameters"]["message"]
    payload = {
        "text": msg
    }
    print(json.dumps(payload).encode('utf8'))

    # Rocket.Chatに送信
    uri = "https://tess0214.hazumik.com/hooks/DQmuspntSiMGbjgDW/ecNmK2ubHLBMaSoSETbhHTEodCfqa8Xx6jRg2MA5ranBmvNB"  # TODO 作成したRocket.ChatのURLに置き換えてください
    req = urllib.request.Request(
        uri,
        data=json.dumps(payload).encode(),
        headers={'Content-Type': 'application/json; charset=utf-8'},
        method="POST"
    )
    res = urllib.request.urlopen(req)

    # 実行結果返却
    return {
        'statusCode': res.status,
        'body': res.read().decode("utf-8")
    }
