import discord
import requests
import gosh

def getweather():

    url = "http://weather.livedoor.com/forecast/webservice/json/v1"
    payload = {"city": "130010"}
    tenki_data = requests.get(url, params=payload).json()

    print(tenki_data["title"])
    print(tenki_data["forecasts"][0]["date"])
    print(tenki_data["forecasts"][0]["telop"])
    print(tenki_data["forecasts"][0]["temperature"]["max"]["celsius"])
    print(tenki_data["forecasts"][0]["temperature"]["max"]["fahrenheit"])
    print(tenki_data["forecasts"][1]["date"])
    print(tenki_data["forecasts"][1]["telop"])
    print(tenki_data["forecasts"][1]["temperature"]["max"]["celsius"])
    print(tenki_data["forecasts"][1]["temperature"]["max"]["fahrenheit"])
    print(tenki_data["publicTime"])

    return tenki_data


# 接続に使うオブジェクト / starting
client = discord.Client()

# 起動した確認 / confirm starting
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



# こっから処理 / processing
@client.event
async def on_message(message):

    dic = { "晴": "晴れ。洗濯◎",
            "雨": "雨。洗濯☓",
            "晴時々曇": "晴れ時々曇り。洗濯◎",
            "晴のち曇": "晴れのち曇り。洗濯◎",
            "晴時々雨": "晴れ時々雨。洗濯○",
            "晴のち雨": "晴れのち雨。洗濯○",
            "晴時々雪": "晴れ時々雪。洗濯○",
            "晴のち雪": "晴れのち雪。洗濯○",
            "曇": "曇り。洗濯○",
            "曇時々晴": "曇り時々晴れ。洗濯◎",
            "曇のち晴": "曇りのち晴れ。洗濯◎",
            "曇時々雨": "曇り時々雨。洗濯△",
            "曇のち雨": "曇りのち雨。洗濯△",
            "曇時々雪": "曇り時々雪。洗濯△",
            "曇りのち雪": "曇りのち雪。洗濯△",
            "雨": "雨。洗濯☓",
            "雨時々晴": "雨時々晴れ。洗濯△",
            "雨のち晴": "雨のち晴れ。洗濯○",
            "雨時々曇": "雨時々曇り。洗濯△",
            "雨のち曇": "雨のち曇り。洗濯△",
            "雨時々雪": "雨時々雪。洗濯☓",
            "雨のち雪": "雨のち雪。洗濯☓"
            }

    if message.content.startswith("洗濯"):
        if client.user != message.author.name:

            tenki = getweather()

            weather = tenki["forecasts"][1]["telop"]

            sendMessage = dic[weather]
            channel = message.channel
            await channel.send(sendMessage)


# ここにはdiscordのbotのトークンを入れる / fill in "token"
TOKEN = gosh.requestsToken()
client.run(TOKEN)