---
layout: post
title: "Clojureのビデオを見る(2)"
date: 2009-07-13
categories: Lisp
---
*[Nendo*]の開発でかなり参考にしたい言語である[Clojure](http://clojure.org/)のビデオをみた。
このあいだ紹介したやつ(*[kiyoka.2009_07_02*])とは別のビデオ。

 [InfoQ: Clojure](http://www.infoq.com/presentations/hickey-clojure)
 In this presentation from the JVM Languages Summit 2008, Rich Hickey
 discusses Clojure, which is an implementation of Lisp. Topics covered
 include Clojure features and syntax, example code, interoperation
 with Java, Clojure and functional programming, persistent data
 structures, concurrency semantics, references, transactions, software
 transactional memory, agents, implementation and pain points.

Rich Hickey自身によるClojureのプレゼンテーションビデオの中でもスライドショーが同期しながら見れるのはこれだけだと思う。また、Clojure自体の紹介が軽めに抑えてある。
私のように、Clojureの並列処理部分よりもJava連携やLispの拡張自体に興味があるような人にも見てもらいやすいと思う。
これを見るとやっぱり、配列とかをLispの構文に組みこんでしまっている点が気になる。
 こんなやつ
```
(drop 2* 1 2 3 4 5*) -> (3 4 5)
```
 Mapなら、こう書くらしい(Rubyで言うところのHash)
```python
(def m {:a 1 :b :2 :c 3})
```

これを入れてしまうかどうかが一つの分かれ道かも。
