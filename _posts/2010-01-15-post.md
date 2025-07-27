---
layout: post
title: "gemをGemCutter.orgに再登録した"
date: 2010-01-15
categories: Nendo
---
私がRubyで書いているLisp方言、 *[Nendo*]について。

Github.comのgem配布の仕組が廃止になったので、GemCutter.orgにgemを再登録した。
![img]({{ "/assets/images/rubygems_icon_128.png" | relative_url }})
モジュール名もprefix付きのkiyoka-nendoという名前からnendoになり、これでnendoというgem名がNendo言語のものになった。
これで、nendoの処理系をインストールするのは超簡単になった。
手順は*[Nendo*]に記載した通り、Ruby 1.9.1の環境で、gem install nendo とするだけ。
少しづつ、自分でアプリを書いたり、リファレンスマニュアル(未整備)を書きながら、使える処理系にしていこう。

とりあえず、nendoを使てどんなコードが書けるかは、このソースをざっと眺めて見て貰えればと思う。
[sample/stowspec at 473eabbbf23023b619213ded4ad1a76979a7e3f2 from kiyoka's nendo - GitHub](http://github.com/kiyoka/nendo/blob/473eabbbf23023b619213ded4ad1a76979a7e3f2/sample/stowspec)
