---
layout: post
title: "RSpecでraise_errorマッチャの使いかたを勘違いしていた"
date: 2009-05-04
categories: Ruby
---
RSpecのexpectationの書き方で、気を付けないと行けないところ

## raise_errorマッチャはProcに対してのみ有効
『あるexampleで例外TypeErrorが出ること。』という仕様を記述する際、『shouldを付ける対象はProcでないといけない』ということは簡単に間違えそう。

ある関数でTypeErrorが出ることを宣言したい場合、次の例は間違い。
```
 @anObj.aMethod.should raise_error( TypeError )
```
このままでは、RSpecのspecコマンド本体が例外で止まるので、次の様にしていた。
```
 begin
   @anObj.aMethod.should raise_error( TypeError )
 rescue
 end
```
こうすることによって、エラーがでなくなり、テストにパスしていたいのでOKだと思ってしまっていた。
でも実は、ちゃんと検査できていなかっただけ。

正解はコチラ
```lisp
 lambda{ @anObj.aMethod }.should raise_error( TypeError )
```
Procのインスタンスにするためにlambdaで囲っている。
この場合、 @anObj.aMethodが TypeError以外の例外をraiseしたり、何も例外をraiseしなかった場合、ちゃんとfailしてくれる。

## (TestDriven Development:TDD)の基本
上の例はちゃんと失敗するところを見届けてなかったからこんな勘違いをしたのだ。

TDD の進め方と原則を引用しておきます。ちゃんと守らないと。
 [Rubyist Magazine - スはスペックのス 【第 1 回】 RSpec の概要と、RSpec on Rails (モデル編)](http://jp.rubyist.net/magazine/?0021-Rspec)
 TDD の進め方と原則
 TDD の進め方はいたって簡単です。TDD は以下の 3 つのステップから構成されます。
  1. プロダクトコードを書く前にテストコードを書き、それが失敗することを
     確認する (レッド)
  2. テストに成功するようにプロダクトコードを書く (グリーン)
  3. プログラムの振る舞いを変えないように、プロダクトコードの重複などを
     整理する (リファクタリング)
  4. (最初に戻る)
 
 「レッド」や「グリーン」といった表現は、いわゆる xUnit*1 の実行結果表
 示バーの伝統的な色づかいに由来しています。RSpec でもレッド/ グリーンと
 いった色使いの伝統が踏襲されています。

ところで、*[Nendo*]の開発はspecファイルをガシガシ書き足しているところだが、まだまだ*[Nendo*]を書き捨てスクリプティングに使えるようになるまでは先が長そう。
7月のShibuya.lispのLTをする段階で一応ダウンロードして遊べるようにしときたいなぁ。
そのために、シンタックスエラーとかランタイムエラー表示まわりを強化しようと頑張っているところです。
プログラミング言語処理系はこういう地道な作業が山積みで骨が折れる。
