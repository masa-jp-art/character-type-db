!pip install gspread oauth2client openai==0.28 google-auth google-auth-oauthlib google-auth-httplib2 pandas --upgrade

import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import openai
import pandas as pd
from google.colab import auth
from google.auth import default
import os
import json

# Google認証
auth.authenticate_user()
creds, _ = default()
gc = gspread.authorize(creds)

# スプレッドシートとシートを開く
sheet_url = '<ここにスプレッドシートのURLを入れる>'
spreadsheet = gc.open_by_url(sheet_url)

# 各シートを取得
sheet_protagonist = spreadsheet.worksheet('protagonist')
sheet_SubCharacter = spreadsheet.worksheet('SubCharacter')
sheet_antagonist = spreadsheet.worksheet('antagonist')

# 生成AIを動かす関数を定義
openai.api_key = "<ここにOpenAIのAPI Keyを入れる"

def ai(x):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        max_tokens=2048,
        messages=[
            {"role": "system", "content": "人間の仕事を助ける優秀なAIアシスタントとして、指示に従い、必要な情報を出力します。出力が長大になっても構わないので、網羅的かつ詳細に出力します。"},
            {"role": "user", "content": x},
        ]
    )
    return response["choices"][0]["message"]["content"]

# シートからランダムに値を取得
protagonist = random.choice(sheet_protagonist.col_values(2)[1:])
SubCharacter = random.choice(sheet_SubCharacter.col_values(2)[1:])
antagonist = random.choice(sheet_antagonist.col_values(2)[1:])

print(protagonist)
print(SubCharacter)
print(antagonist)

# 物語の舞台を定義

input = """
<ここに物語の舞台のアイデアを入れる>
"""

# 各キャラクターを生成
prompt_protagonist = ai(f"""
下記の文章を抽象的に解釈して、この物語の主人公の名前と人物像を出力します。
\n物語の舞台: {input},
\n主人公のキャラクタータイプ: {protagonist},
""")

prompt_SubCharacter = ai(f"""
下記の文章を抽象的に解釈して、この物語のサブキャラクターの名前と人物像を出力します。
\n物語の舞台: {input},
\nサブキャラクターのキャラクタータイプ: {SubCharacter},
\n参考：主人公の人物像: {prompt_protagonist},
""")

prompt_antagonist = ai(f"""
下記の文章を抽象的に解釈して、この物語において主人公と対立する者の名前と人物像を出力します。
\n物語の舞台: {input},
\n主人公と対立する者のキャラクタータイプ: {antagonist},
\n参考：主人公の人物像: {prompt_protagonist},
""")


# 物語のあらすじを生成
Synopsis = ai(f"""
下記の3人のキャラクターが活躍する物語のあらすじを書いてください。物語全体が調和するために不要な要素は削除しても構いません。必要に応じて構造化して読みやすい形式で出力してください。
\n物語の舞台: {input},
\n参考：主人公の人物像: {prompt_protagonist},
\n参考：サブキャラクターの人物像: {prompt_SubCharacter},
\n参考：主人公と対立する者の人物像: {prompt_antagonist},
""")

print(Synopsis)
