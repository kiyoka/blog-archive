# kiyokaのブログアーカイブ RAG検索

このプロジェクトは、llama-indexを使用してブログアーカイブに対してRAG（Retrieval-Augmented Generation）検索を行えるようにします。

## セットアップ

### 1. 依存関係のインストール

#### 仮想環境を使用する場合（推奨）

```bash
# 仮想環境の作成
python -m venv venv

# 仮想環境の有効化（Linux/Mac）
source venv/bin/activate

# 仮想環境の有効化（Windows）
venv\Scripts\activate

# 依存関係のインストール
pip install -r requirements.txt
```

#### システム全体にインストールする場合

```bash
pip install -r requirements.txt
```

### 2. 環境変数の設定

`.env.example`をコピーして`.env`ファイルを作成し、API keyを設定してください。

```bash
cp .env.example .env
```

#### OpenAIを使用する場合

`.env`ファイルを編集してAPIキーを設定:

```
OPENAI_API_KEY=your_actual_openai_api_key_here
```

#### ローカルLLMを使用する場合

ローカルでLLMサーバーを起動し、以下のように設定:

```
# ローカルLLM設定（OpenAIの代替）
LOCAL_LLM_URL=http://192.168.56.1:1234
LOCAL_LLM_MODEL=llm-jp-3.1-13b-instruct4

# 埋め込みにはOpenAI APIが必要（検索機能用）
OPENAI_API_KEY=your_actual_openai_api_key_here
```

**注意**: 埋め込み（embeddings）にはOpenAI APIが必要です。回答生成にのみローカルLLMが使用されます。

### 3. ブログ記事データの抽出

```bash
# 仮想環境を使用している場合は事前に有効化
source venv/bin/activate  # Linux/Mac
# または
venv\Scripts\activate     # Windows

python extract_posts.py
```

これにより、`_posts`ディレクトリ内のMarkdownファイルからテキストを抽出し、`posts_data.json`に保存します。

### 4. ベクトルインデックスの構築

```bash
python build_index.py
```

これにより、抽出したブログ記事からベクトルインデックスを構築し、`./storage`ディレクトリに保存します。

## 使用方法

**注意**: 仮想環境を使用している場合は、以下のコマンドを実行する前に仮想環境を有効化してください：

```bash
source venv/bin/activate  # Linux/Mac
# または
venv\Scripts\activate     # Windows
```

### インタラクティブモード

```bash
python query_blog.py
```

対話型のインターフェースが起動し、質問を入力してブログアーカイブを検索できます。

### 単発クエリモード

```bash
python query_blog.py "Lispについて教えて"
```

コマンドライン引数として質問を渡すと、その質問に対する回答を表示して終了します。

## 検索例

- "Lispについて教えて"
- "Rubyの情報を探している"
- "プログラミング言語の比較"
- "テスト駆動開発について"
- "データベースの話"

## 仕組み

1. **テキスト抽出**: Jekyll Markdownファイルからフロントマターとコンテンツを抽出
2. **前処理**: Markdownをプレーンテキストに変換、液体テンプレートタグを削除
3. **ベクトル化**: OpenAIの埋め込みモデルでテキストをベクトル化
4. **インデックス構築**: llama-indexでベクトルストアインデックスを構築
5. **検索**: ユーザーのクエリに対して意味的類似性検索を実行
6. **生成**: 検索結果を基にLLMが回答を生成

## ファイル構成

- `extract_posts.py`: ブログ記事からテキストを抽出
- `build_index.py`: ベクトルインデックスを構築
- `query_blog.py`: RAG検索のメインインターフェース
- `requirements.txt`: Python依存関係
- `.env.example`: 環境変数の例
- `posts_data.json`: 抽出されたブログ記事データ（生成される）
- `./storage/`: ベクトルインデックスのストレージ（生成される）

## 注意事項

- OpenAI APIの使用には料金が発生します
- 初回のインデックス構築には時間がかかる場合があります
- `.env`ファイルにはAPIキーが含まれるため、バージョン管理に含めないでください