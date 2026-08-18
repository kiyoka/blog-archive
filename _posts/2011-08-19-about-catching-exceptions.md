---
layout: post
title: "例外の捕捉について"
date: 2011-08-19
categories: Nendo
---
オレ処理系の*[Nendo*]についての開発メモ。
 ![img](http://mrg.bz/SYKjVO)

Gaucheのguardに似せたsyntaxになるようにトライしているところ。
たぶん、guardとunwind-protectはGaucheと同等のsyntaxになると思う。
実際には、例外クラスにはRubyのクラスが設定されるので、ソースコードレベルで互換性が確保できるわけではない無いけど…
Gauche脳とRuby脳の両方を持つ人にはGaucheのリファレンスをちらっと見ただけでコードが書けるレベルは保てるだろう。(Nendoのリファレンスも書く予定だけど…)

どういう風にRubyのコードにマッピングするかは実装しながら考える。
ちなみに、今回初めてsyntax-rules使ってシンタックスを定義しているのだけど、これは楽だ〜。
やっとブロックが積みあがってきた感じがするよ〜。
