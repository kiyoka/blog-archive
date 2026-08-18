---
layout: post
title: "srfiのポーティング(1)"
date: 2010-07-05
categories: Nendo
---
私がRubyで書いているLisp方言、 *[Nendo*]について。

srfi-1のポーティングに挑戦中。
Olin Shiversさんのリファレンス実装はsyntax-rulesが使われていないが、call-with-current-continuation(継続)が使われている。
 リファレンス実装の情報はこちら: [SRFI 1: List Library](http://srfi.schemers.org/srfi-1/srfi-1.html)
 そして、ソースコードは[こちら](http://srfi.schemers.org/srfi-1/srfi-1-reference.scm)
これを、継続を使わない形式に書きなおしていく予定。
継続が使われている理由を推測すると、おそらくmap関数などに長いリストを渡してもスタックオーバーフローしないようにしているのだろう。
mapが一つのリストを受けとった場合については、末尾再帰で書くのは簡単だけど、複数のリストを受けとった場合も考慮すると、継続なしで効率の良いコードは書けない気がする。(セルの大量コピーが発生しても良いなら書けるかも)
Nendoについては、セルの大量コピー版でいくか...

srfi-1以外については*[Nendo*]はsyntax-rulesが未実装なので、syntax-rulesを先にサポートする必要が有りそう。
外の処理系のsyntax-rulesの実装を見てまわっているが、Scheme自身で書かれていたり(chibi-scheme)、Rubyで書かれて言たり(heist)、いろいろだ。(Gaucheは何で書かれているのか読み切れなかった。どこに有るのか見つけられなかった。Gaucheはチューニングの工夫が入りすぎていて、簡単にソースが追えないなあ...)
それにしても、Scheme処理系の実装方法の幅は広いなあ。いろいろソースを読むのも楽しい。
