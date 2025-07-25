---
layout: post
title: "MongoDB: The Definitive Guide"
date: 2011-11-03
categories: 本
---
この本いいよ。
第二版が出るらしいのだけど、待てないので第一版を買った。
当初WebブラウザでSafari Books Online上の電子書籍を読んでいたのだけど、疲れるので紙の書籍にした。電子書籍リーダー持ってないし。
{% include amazon.html asin="1449381561" title="MongoDB: The Definitive Guide" author="Kristina Chodorow, Michael Dirolf" %}
MongoDBを本格的に使おうと思ってこの本にした。本格的に使うなら、最初からこの本を読み通しておくべきだろうと。
MongoDBのコミッター(10genのエンジニア)も著者に入っているので、なぜこういう設計になっているのかというところも説明してくれている。
実際にサーバー側の内部を知っているものでないと、このような解説はできないだろう。
MongoDBサーバーの設計ポリシーや実装上のトレードオフを最初から理解しておくことは重要だと思う。結果、MongoDBの適用範囲を間違えなくて済む。
トレードオフがわからないままだと、「ここは設計上律速するはずなので、部分的にmemcaced使っとこか」というようなアプリケーションのトレードオフの判断ができない。

MySQLを本格的に使う時に、この本{% include amazon.html asin="4873112095" %}を2回通しで読んだ記憶があるが、1回目はとにかく読む。2回目は使い倒しながら読んだ。

今回のMongoDBもそこまでできるかわからないが、MongoDBをヘビーに使う気でいるので、じっくり読むぞ。
MongoDBの試用実験も始めているので、その経過もブログに書く予定。
