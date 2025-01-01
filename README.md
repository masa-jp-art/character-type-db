# 概要
- このプロジェクトでは、OpenAI o1 proが出力したキャラクタータイプの分類データからデータベースを作り、ランダムに取り出したキャラクタタイプからキャラクターのアイデアを生成します。
- このプロジェクトは、ChatGPT Proで使用できる、OpenAIのo1 pro modeの検証を兼ねています

# 手順
- ChatGPT Proのo1 pro modeに、物語のキャラクタータイプを生成させます
  - [character-type-protagonist-1.md](https://github.com/masa-jp-art/character-type-db/blob/main/character-type-protagonist-1.md)
  - [character-type-protagonist-2.md](https://github.com/masa-jp-art/character-type-db/blob/main/character-type-protagonist-2.md)
  - [Character-type-SubCharacter.md](https://github.com/masa-jp-art/character-type-db/blob/main/Character-type-SubCharacter.md)
  - [Character-type-antagonist.md](https://github.com/masa-jp-art/character-type-db/blob/main/Character-type-antagonist.md)
- 各キャラクターをスプレッドシートに転記してデータベースを作ります
  - [20250101-Character-type-snapshot](https://docs.google.com/spreadsheets/d/19C8QyBmT4gazWGgDIjvax4VwzGr_POiDX0nXsoZP9QQ/edit?usp=sharing)
- Google colabでプログラムを動かし、キャラクターとあらすじを生成します
  - [code-for-google-colab.py](https://github.com/masa-jp-art/character-type-db/blob/main/code-for-google-colab.py)
 
# 関連
- [OpenAI o1 pro mode検証:物語のキャラクタータイプデータベースが作れるか](https://note.com/msfmnkns/n/nfe0e4f07d4b5)
