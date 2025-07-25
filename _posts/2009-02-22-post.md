---
layout: post
title: "Key-Value Store勉強会に行きたかった..."
date: 2009-02-22
categories: プログラミング
---
![img](http://www.publicdomainpictures.net/pictures/1000/thumb/1-1208707554nqU5.jpg)
 [Key-Value Store勉強会に行ってきました - blog.katsuma.tv](http://blog.katsuma.tv/2009/02/key_value_store_study.html)
 greeさんで開催されたKey Value Store勉強会に行ってきました。時間にして
 4時間超え、内容も国内のKey-Value Storeなソフトウェアの最前線の話ばかり
 で相当なボリューム。以下、メモってたのを残しておきたいと思います。
それにしても、このメモすごい情報量。

自分の興味としては、Key-Valueストレージエンジンの実装よりも、Key-Valueのデータベースの応用事例の方にある。
リレーショナルDBなら事例は山ほどあり、論理設計、物理設計ともに設計手法も確立している。
Key-Valueの場合はどんな分野で使えるんだろう。
例えば、*[Sumibi.org*]をTokyoCabinetベースで作るとなると、どんな設計になるのかなとか。
もしかしたら、いまMySQLにメモリ3GByteも割当てているけどTokyoCabinetなら圧縮がかかってメモリ節約出来るんだろうかとか。
はたまた、一般的なCRMをKey-Valueで作るとどんな点に気を付けないといけないのかとか。そもそも、そういう分野には向いていないのではないかとか。
たぶん将来はAmazonのインフラ上で作品を作りたいと思っているので、この辺勉強しないといけないなと思っていた所。
作品を作る時は、*[Kahua*]のObject DBをAmazon S3とかDynamo対応する方向なのかなと漠然と思っているけど、もっと勉強すると各エンジンのトレードオフとかも肌で分かるようになるのかな。

 [KVS 勉強会に出て、自分でも書いてみたいなと思ったり。 - 生駒日記](http://d.hatena.ne.jp/mamoruk/20090220/p1)
 かな漢字変換的にはやはり key-value store (hash 的なもの)ではなく Trie
 があるといい(common prefix search が使えると検索効率がよい)のだが、やっ
 ぱり自分で1回は書いておいたほうがいいのだろうなー、と思った。いつになる
 か分からないけど……。
[id:mamoruk](http://d.hatena.ne.jp/mamoruk/about)さんも書いておられるように『自分で1回は書いておいたほうがいいのだろうなー』という気持もあるけど、自分はWebアプリケーションを作るほうに時間を使いたいのでちょっとそこまで時間はかけられないかなと思ったりもする。
ちょっと自分はRDBとSQL脳に傾いているのでもっと引出しを増やす意味でもいろいろ見ておこう。

追記:Key-Value Store勉強会については首藤さん所が、リンクが沢山で便利。
 [Shudo's Notes (2009/2)](http://www.shudo.net/diary/2009feb.html#20090220)

