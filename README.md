# Sbe-IT-Practicum
## 概要
情報実習の授業で作成したPythonコードおよび回路図を管理・共有するためのリポジトリです。

授業で扱う`RPi.GPIO`による実装に加え、Raspberry Pi公式推奨の`gpiozero`を使用した実装も掲載しています。
## ディレクトリ構成
```text
/
├── lesson{N}/
│   ├── gpiozero-ver/
│   │   └── *.py
│   ├── *.py
│   └── 回路図.jpg
│
└── ...
```
各ディレクトリの役割は以下のとおりです。
| ディレクトリ・ファイル | 内容 |
|---|---|
| `lesson{N}/` | 授業で扱った `RPi.GPIO` 版のコード |
| `lesson{N}/gpiozero-ver/` | `gpiozero` で書き直したコード |
| `lesson{N}/回路図.jpg` | 実習で使用した回路図 |
## 実装について
### RPi.GPIO版
授業で使用する標準的な実装です。
- `lesson{N}/`直下に配置します。
- 記述量が多くなりやすく、コードも煩雑になりがちです。
- Raspberry Pi 5では`RPi.GPIO`が使用できません。時代遅れです。
### gpiozero版
`RPi.GPIO`版と同等の処理を、`gpiozero`を使用して実装したものです。
- `lesson{N}/gpiozero-ver/`に配置します。
- Raspberry Pi公式が推奨するGPIO操作ライブラリです。
- LEDやボタンなどのデバイスを"モノ"として扱えます。
- Pythonらしく簡潔に記述できます。
- Raspberry Pi 5にも対応しています。
## 補足
基本的には授業で扱った`RPi.GPIO`版を残しつつ、より簡潔で扱いやすい`gpiozero`版も併せて掲載しています。

それぞれの実装を比較しながら、参考にしてください。

ロジックは主に`RPi.GPIO`版にコメントしています
