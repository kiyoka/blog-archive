---
layout: post
title: "次はアプリを試作してみよう"
date: 2009-08-01
categories: Nendo
---
私がRubyで書いているLisp方言、 *[Nendo*]の開発状況続き。

さて、*[Nendo*]をどういう方向に持って行こうか考えているのだが、考える前にNendoで簡単なアプリを作ってみようと思い立った。
そうすれば、自分が言語に期待するものがわかるんじゃないか。
最初に作ろうと思っているのは、パッケージマネージャソフト [Stow](http://www.gnu.org/software/stow/)のラッパー。
昔、[Cmmi](http://www.netfort.gr.jp/~kiyoka/cmmi/index_ja.html)というパッケージマネージャのラッパーを作ったけど、ちょっと自分のパッケージ管理のユースケースに合わなくなってきた。
今は無理矢理CmmiとStowの組合せでやっているけど、ちょっとめんどくさい。
もっとStow専用にして、スムースに使えるものがいい。

こんな風に使いたい。ツールの名前はstowspecがいいかな。
 ソースアーカイブを引数に渡すと自動的に ~/stowspecに登録してくれる
```bash
$ stowspec http://www.example.com/hogehoge-1.2.3.tar.gz
$ cd ~/stowspec
$ ls 
hogehoge-1.2.3
```

 specファイルがS式になっていて、さっきのコマンドで自動生成されている
```bash
$ cd ~/stowspec/hogehoge-1.2.3
$ cat specfile

(stow
  (configure "configure --prefix=/usr/local/stow/hogehoge-1.2.3")
  .
  (略)
  .
```

 specファイルがカレントディレクトリにあれば /usr/local/stow/ へのインストールまでは全く考えなくても良い。
```bash
$ cd ~/stowspec/hogehoge-1.2.3
$ stowspec
 以下、 configure, make, make install の全プロセスが走る。
  .
  .
```

こうすれば、ソースコードからビルドした手順が残せたり、同一ソフトの複数バージョンを混乱無く管理できそう。
他にも実現したいことは、
- ~/stowspec 以下をgitで管理したい。そのためには、~/stowspec 以下にはspecファイル以外は置きたくない。
- --prefix指定がちゃんと動かないtarボールを発見してエラー通知したい。
- インストールターゲットごとに、ビルド条件を変えたい。(そこはS式なのでifとかcondとか使って自由自在)
かな。
今の*[Nendo*]の機能では不足がありすぎるだろうから、随時構文を追加したり、デザインを見なおしたりしながら進めようと思う。
