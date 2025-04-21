# toio-parade

toio (トイオ) を Python で制御し「おもちゃの兵隊の行進 (Parade of the Wooden Soldiers)」に合わせて踊ります。  
最大6台で同時接続、動作させることを確認済みです。  
  
動作は以下の音源に合わせて作成しました。  

- 【混合5〜7重奏（楽器が選べるアンサンブル）】おもちゃの兵隊の行進 (https://www.youtube.com/watch?v=7IoZLJhnByY)

## 📦 セットアップ手順

### 1. 仮想環境の作成 (既にある場合はスキップ)
```bash
python -m venv toio-env
```

### 2. 仮想環境のアクティベート
```bash
source toio-env/bin/activate
```

### 3. 必要なパッケージのインストール
```bash
pip install -r requirements.txt
```

## 🚀 実行方法

toio を起動し、Bluetooth 接続が可能な状態にしてから以下を実行:

```bash
python gogo-toio.py
```

## 🛠 使用ライブラリ

- Python 3.12.9
- bleak (BLE 通信ライブラリ) など
- toio-py 1.1.0

## 📁 プロジェクト構成

```
.
├── gogo-toio.py           # メインスクリプト
├── requirements.txt       # 依存パッケージ一覧
├── .gitignore             # Git 管理無視ファイル一覧
├── .python-version        # pyenv用のPythonバージョン指定
└── toio-env/              # 仮想環境ディレクトリ (Git 管理対象外)
```

## 🧸 対応ハードウェア

- toio Core Cube
- Bluetooth 4.0 以上の PC またはデバイス

## 📝 ライセンス

MIT License
