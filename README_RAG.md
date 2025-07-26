# kiyokaのブログアーカイブ RAG検索

このプロジェクトは、llama-indexを使用してブログアーカイブに対してRAG（Retrieval-Augmented Generation）検索を行えるようにします。

## セットアップ

### 1. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 2. 環境変数の設定

`.env.example`をコピーして`.env`ファイルを作成し、OpenAI API keyを設定してください。

```bash
cp .env.example .env
```

`.env`ファイルを編集してAPIキーを設定:

```
OPENAI_API_KEY=your_actual_openai_api_key_here
```

### 3. ブログ記事データの抽出

```bash
python extract_posts.py
```

これにより、`_posts`ディレクトリ内のMarkdownファイルからテキストを抽出し、`posts_data.json`に保存します。

### 4. ベクトルインデックスの構築

```bash
python build_index.py
```

これにより、抽出したブログ記事からベクトルインデックスを構築し、`./storage`ディレクトリに保存します。

## 使用方法

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