---
layout: post
title: "Schemeのportをportingするには？"
date: 2010-12-26
categories: Nendo
---
Schemeのportって何を抽象化しているんだろう。
RubyのFileオブジェクトをちょっとラップしただけでもできるもんなのだろうか。
もうそろそろ、portが無いとGaucheのライブラリのAPIを近似できない事態が増えてきた。rfc.jsonとか。

ちょっと、ここらでじっくりportについて考えてみたほうが良いのではないかというフェーズに入った。

きっかけは、*[Sekka*]で未知語登録UIのために、google ime apiを使いたいと思った事で、
# google ime apiが返却するうJSONファイルがおかしいのに気付き、
# google ime apiを修正するプロキシサービスをheroku.com上に立ちあげ、
# 同時にGaucheの0.9.1でjsonライブラリが公式APIになったので、
# *[Nendo*]にjsonライブラリをGaucheと同一APIでサポートしようとして、
# portという概念まで合わせ込みたくなった。
という状況。

*[Nendo*]の開発は常にアプリケーションドリブン。オレ処理系の開発としては当面これでいいよね。
言語としてのとんがった部分は平行に別の脳の部位を使って考えとります。

それにしても、*[Sekka*]の未知語登録UIのサポートまでの手順が長過ぎる。まあ仕方ない。
