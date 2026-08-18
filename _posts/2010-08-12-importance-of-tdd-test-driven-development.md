---
layout: post
title: "TDD(テスト駆動開発)の重要性"
date: 2010-08-12
categories: Nendo
---

実験中の新しい日本語入力メソッド Sekka(仮名)を*[Nendo*]で作ろうとしているが、そのために*[Nendo*]に足りない機能を足している。
SekkaはちゃんとTDD(テスト駆動開発)で開発していく予定なので、unit testフレームワークが必要になった。
そこで、gauche.testの基本機能をポーティングしたところ。
 リンク: [Gauche ユーザリファレンス: 9.22 gauche.test - 単体テスト](http://practical-scheme.net/gauche/man/?l=jp&p=test-start)

実は、恥ずかしながらSumibi.orgはunit testの様に再現可能なテストスイートは持っていないので、ソースコード規模が大きくなるほどメンテナンスに対する心理的負担が大きくなっていった。リファクタリングもなかなか困難になっていた。
*[Nendo*]で完全にTDDを実践し、いまではTDD以外の開発は考えられなくなった。プログラミング言語処理系の開発にはテストスイートが必須だと思う。おそらく複雑なアルゴリズムを使ったソフトウェアには同様にそれなりの量のテストスイートが無いとどこかで必ず開発が破綻するだろう。
SekkaもTDDで開発していつでもリファクタリングできる状態を維持しよう。

 参考: [テスト駆動開発 - Wikipedia](http://ja.wikipedia.org/wiki/テスト駆動開発)
 {% include amazon.html asin="0321146530" title="Test Driven Development" author="Kent Beck" %}
