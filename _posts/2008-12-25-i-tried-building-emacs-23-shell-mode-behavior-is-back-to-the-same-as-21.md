---
layout: post
title: "Emacs 23をビルドしてみた。shell-modeの挙動が21と同じに戻った。"
date: 2008-12-25
categories: Emacs
---
 ![img](http://www.netfort.gr.jp/~kiyoka/predoc/img/emacs_48.png)
久々にEmacsネタを。
普段からよく使っている、shell-modeの挙動がEmacs 21時代に戻っている。
個人的にはこれだけでもEmacs 23を使う意味がある。

Emacs 22では shell-mode中でコマンドを実行した場合、コマンドが出力した文字列は通常のテキストとは違う扱いになっていた。
例えば、次の様な一連の連携プレーはEmacs 22で出来なくなった。
まず、次のコマンドを実行する。
```
 % find . -type d
 ./dir_A
 ./dir_B
 ./dir_C
```

次にfind コマンドが出力した ./dir_B の部分の先頭に 'cd 'を追加して
```bash
 cd ./dir_B *return*
```

と入力した場合、Emacs 21では、cd ./dir_B が実行される。これは素直な動作だと思う。
それがEmacs 22では空振りする。(プログラムが出力したテキストは保護されているおり、プロンプトの直後だけをコマンドと認識するようだ)

これが、Emacs 23では Emacs21と同じ挙動に戻されている。
これはかなり嬉しい。
Emacsユーザのみんなはどう思っているんだろう。誰かのクレームがあって戻ったんだろうか。

