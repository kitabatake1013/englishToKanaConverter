# englishToKanaConverter

英語文字列をカタカナに変換するプログラム

## 概要

アルファベットで書かれた文字列を、カタカナ文字列に変換するプログラムです。
アルファベット以外の部分には何も作用しません。

このプログラムを使うことで、「hello」が「ハロー」に、「tanaka」が「タナカ」に、「abc」が「エイビーシー」になります。
即ち、変換後の文字列には、アルファベットが一切出てこなくなります。

## 動作環境

python 3.7以降

## 使用方法

本リポジトリ内の`englishToKanaConverter`ディレクトリに、モジュール本体が格納されています。
カレントディレクトリ内にこのディレクトリが含まれる状態で、以下のようにして使用します。

```
# モジュールのインポート
from englishToKanaConverter import EnglishToKanaConverter

# EnglishToKanaConverterインスタンスを作成
# 第1引数debugをTrueにすると、englishToKanaConverterディレクトリ内にenglishToKanaConverter.logというファイルが生成され、ログが記録されます。
# 引数を省略するとFalseになり、ログは生成されません。
converter = EnglishToKanaConverter()
# 変換元のテキスト
text = "hello"
# 変換結果
text_converted = converter.process(text)
# 結果を出力
print(text_converted)
```

## 動作確認用プログラム

コマンドラインで本リポジトリのトップに移動し、

```
python sample.py
```

を実行すると、本モジュールの動作確認が行えます。
変換したい文字列を入力してEnterキーを押すと、変換結果が表示され、再度入力待ち状態になります。
プログラムを終了するには、Ctrl+Cを押します。
なお、本プログラムを使用すると、`englishToKanaConverter`ディレクトリ内に`englishToKanaConverter.log`が作成され、ログが保存されます。

## 辞書のメンテナンス

### 辞書ファイルの種類

本プログラムで使用する辞書データは、`englishToKanaConverter`ディレクトリ内の`dictionaries`サブディレクトリ内に格納されています。
各ファイルの用途は下記の通りです。

* `phrases.py`: 英単語をカタカナに変換するための辞書です。複合語の変換にも用います。
* `words.py`: 英単語をカタカナに変換するための辞書です。対象文字列内のアルファベット列がこのファイルにある単語と完全に一致する場合にのみ、変換が行われます。
* `suffix.py`: 「ing」や「ed」など、単語の末尾にある特定の文字列を自動変換するための辞書です。
* `roman.py`: 英単語として変換できない文字列があった際、ローマ字として変換を試みるために用いる辞書です。
* `spell.py`: 英単語やローマ字として変換できないアルファベット列をスペルアウトするために用いる辞書です。各アルファベットの読み方を定義します。

### 辞書の最適化

辞書に項目を追加した際は、辞書データの最適化を必ず行ってください。
コマンドラインで本リポジトリのトップに移動後、

```
python tools/optimizeDic.py
```

と入力してください。

### 辞書への単語登録時の注意点

* 変換元文字列（辞書のキー）として使用できるのは、半角の大文字アルファベットと「'（半角アポストロフィー）」のみです。辞書の最適化を行うと、小文字アルファベットは大文字に、全角アルファベットは半角に変換されます。その結果、使用できない文字が含まれていると、辞書の最適化時に警告メッセージが表示されます。自動での修正を行わないため、手動で内容を確認・修正してください。
* 辞書の最適化を行うと、記述内容がアルファベット順でソートされます。従って、項目を追加する際は、何をどこに追加してもかまいません。

## ライセンスと著作権

本プログラムは、GPL(GNU GENERAL PUBLIC LICENSE) Version 2の条件に従い、自由にご利用いただけます。

Copyright (C) 2022 Kazto Kitabatake, ACT Laboratory All rights reserved.

本プログラムで使用している英語カタカナ変換辞書は、[Bilingual Emacspeak Project](http://www.argv.org/bep/)が提供している`bep-eng.dic`を元にしています。

Copyright 1999-2002 Bilingual Emacspeak Project.　All rights reserved.
