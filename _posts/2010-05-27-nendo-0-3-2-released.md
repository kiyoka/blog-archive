---
layout: post
title: "Nendo 0.3.2 リリース"
date: 2010-05-27
categories: Nendo
---
*[Nendo*] 0.3.2をリリースしました。(リリースノート: *[Nendo.ReleaseNote*])
![img]({{ "/assets/images/rubygems_icon_128.png" | relative_url }})
チュートリアルと、リファレンスマニュアルはまだ書きかけです。
*[Nendo.Tutorial*] 
*[Nendo.ReferenceManual*] 

今回から、Nendoで記述されたユーザースクリプトをRubyにコンパイルする機能が入りました。
Lispの一番重い処理であるコンパイルステップ(マクロ展開など)が処理済みのRubyのソースコードが出力されます。
 *コマンド例*
```
nendo -c script.nnd > script.rb
```

あとは、script.rb に実行権限を付ければ普通のRubyスクリプトとして実行できます。
```
chmod +x script.rb
./script.rb
```

これで、頻繁に利用するコマンドラインツールを*[Nendo*]で書いてもストレスなく使えるものが作れます。
ちなみに、Nendoで開発している*[Stowspec*]というコマンドラインツールでは以下のような結果になりました。
起動時間だけが分かるように、stowspecスクリプトのmain関数の入口で (exit 0) するようにしています。

 うちにある一番速いマシン(Sumibi.orgの漢字変換サーバ)での計測結果。
 スペック: AMD Athlon(tm) 64 X2 Dual Core Processor 4200+
```bash
$ time ./stowspec
2.147 secs                                                                                                                      
$ time ./stowspec
2.156 secs                                                                                                                      
$ nendo -c ./stowspec > stowspec.rb  
$ time ./stowspec.rb
0.315 secs                                                                                                                      
$ time ./stowspec.rb
0.315 secs                                                                                                                      
```

ちなみに、ソースコードの行数はかなり膨らんでいますが、この時間で終わるのはRubyすごいです。
```bash
$ wc stowspec
     576    1924   20576 stowspec
$ wc stowspec.rb
    6183   20458  531101 stowspec.rb
```

他にも、vectorが使えるようになったりと、少しずつ言語のコア機能が固まりつつありますが、もうそろそろ、新しいモノ好きの人に試してもらうためのドキュメント整備が必要かなと思っています。
