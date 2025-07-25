# Dropbox画像移行計画

## 現在のDropboxリンク一覧

### 使用されている画像ファイル
1. `iStock_000016378483XSmall.jpg` - 11箇所で使用
2. `iStock_000019986662XSmall.jpg` - 2箇所で使用  
3. `iStock_000019296334XSmall.jpg` - 3箇所で使用
4. `bookshelf_of_bookscan.png` - 1箇所で使用
5. `lazy_for_nendo_exam_graph.png` - 1箇所で使用
6. `eager.nnd.png` - 1箇所で使用
7. `generator.nnd.png` - 1箇所で使用
8. `lazy.nnd.png` - 1箇所で使用

## 移行手順

### 1. Dropbox側の準備
1. 現在の古い公開リンク形式（`http://dl.dropbox.com/u/3870066/`）は廃止されています
2. Dropboxから画像ファイルをローカルにダウンロード
3. 新しい共有リンクを作成するか、別のホスティング方法を検討

### 2. 新しいホスティング方法の選択肢

#### オプション1: GitHubリポジトリ内に画像を保存
- `assets/images/`ディレクトリを作成
- 画像をリポジトリに追加
- 相対パスでリンク: `/assets/images/filename.jpg`

#### オプション2: GitHub Pages CDN
- GitHub Pagesの自動CDN機能を利用
- リポジトリ内の画像は自動的にCDN経由で配信

#### オプション3: 外部画像ホスティングサービス
- Imgur、Cloudinary等の画像専用ホスティングサービスを利用
- 無料プランで十分な容量

### 3. 推奨される移行方法

**GitHub リポジトリ内への移行を推奨**
- 理由：
  - 外部依存を減らせる
  - リンク切れのリスクが低い
  - バージョン管理が可能
  - GitHub Pagesとの統合が簡単

### 4. 実装手順
1. `assets/images/`ディレクトリを作成
2. Dropboxから画像をダウンロード
3. 画像をリポジトリに追加
4. ブログ記事内のリンクを更新
   - 旧: `http://dl.dropbox.com/u/3870066/blog/filename.jpg`
   - 新: `/assets/images/filename.jpg`

### 5. 注意事項
- 画像サイズの最適化を検討（WebP形式への変換など）
- リポジトリサイズが大きくなりすぎないよう注意
- 画像の著作権を確認