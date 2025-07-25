---
layout: post
title: "RESTベースの関数型言語ライブラリ"
date: 2008-04-08
categories: プログラミング
---
{% include amazon.html asin="4873111609" title="Tomcatハンドブック" %}
を*[Kahua*]と見比べながら読んだり、[ricollab Web Tech Blog >> REST 入門(1 Web アプリケーションのアーキテクチャ)](http://blogs.ricollab.jp/webtech/introduction_to_rest_no_1/)を読んだりした。
そうすると、なぜか頭の中で変な風に配線が繋がった。関数型言語でいうところの関数なら、1関数=1URLで表現できるんじゃないか。
RESTの基本はステートレスサーバ、つまりクライアントの状態をサーバーが管理せず、サーバが計算するために必要な全ての情報を毎回クライアントからもらう。
これって、関数型言語のimmutableな関数の考えかたじゃないか。
REST APIを数珠つなぎにすれば関数型プログラミングもできる。
# RESTでSchemeの関数を実装した例
例えば、S式のリストをソートする関数は次のURLで実行できるとすれば、
```
http://func.example.com/lib/sort
```
次のようなコードが書けると面白いのでは？
```javascript
(use-rest-function "http://func.example.com/lib")
(sort '(1 5 2 4 7 6 8 9 3))
```
結果
```
(1 2 3 4 5 6 7 8 9)
```
RESTにしてうれしい物としては、英語の辞書とか、大きなデータベースを必要とするため
ローカルに置いておくよりも、皆で共有したほうが良いものとかかな。
他にも、画像処理などの重たい処理を簡単に分散処理・並列処理を実現する手段としても使えそう。
