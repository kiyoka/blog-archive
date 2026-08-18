---
layout: post
title: "let-syntaxの実装方法の検討"
date: 2011-04-30
categories: Nendo
---
オレ処理系の*[Nendo*]についての開発メモ。
 ![img](http://mrg.bz/SYKjVO)

( ※ この記事中のやりかたは全くの間違いだとわかったので、信じないようにお願いします。後日、正しい内容をまとめます )

let-syntaxの実装方法を検討中。

## 概要
次のような手順でマクロ展開しようと考えている。
 ソースコード → 内部表現1  → 内部表現2  → 展開形

## ソースコード → 内部表現1
*ソースコード*
```lisp
(define (a-topleve-func arg1 arg2 ...)
  (let-syntax ((name1 (syntax-rules ...))
               (name2 (syntax-rules ...)))
    ... body1 ...
    (letrec-syntax ((name1 (syntax-rules ... ))
                    (name2 (syntax-rules ... )))
      ... body2 ...)))
```
Rubyでマクロ展開する時に少しでも楽をするために、Nendoの初期化スクリプト(init.nnd)でlet-syntaxとletrec-syntaxを両方とも%lexical-define-syntaxを使った内部表現に変換する。
let-syntaxとletrec-syntaxの二つは伝統的マクロで以下の形に変換する。
let-syntaxのほうだけ、束縛するキーワードの数だけネストさせた形にする。
letrec-syntaxのほうは、キーワードが %lexcal-define-syntaxになるだけで、フォームの変形は行わない。

## 内部表現1 → 内部表現2
*内部表現1*
```lisp
(define (a-toplevel-func arg1 arg2 ...)
  (%lexical-define-syntax ((name1 (syntax-rules ...)))
      (%lexical-define-syntax ((name2 (syntax-rules ...)))
          ... body1 ...
          (%lexcal-define-syntax ((name1 (syntax-rules ...))
                                  (name2 (syntax-rules ...)))
             ... body2 ...))))
```
Rubyで実装したマクロ変換器で、%lexcal-define-syntaxの (syntax-rules ...)部分を実行形式にコンパイルする。
実行形式へのコンパイルはNendoのBuilt-in関数であるevalを呼べばいいので、Rubyとinit.nndのどちらでも書ける。
(Nendoではsyntax-rules手続きを呼びだせば、LispSyntaxクラスのインスタンスが返ってくる)

変換後は以下のような内部表現になる。(#<LispSyntax>は説明用の便宜上の表現)

## 内部表現2 → 展開形
*内部表現2*
```lisp
(define (a-toplevel-func arg1 arg2 ...)
  (%lexical-syntax ((name1 . #<LispSyntax>))
    (%lexical-syntax ((name2 . #<LispSyntax>))
       ... body1 ...
       (%lexcal-syntax ((name1 . #<LispSyntax>)
                        (name2 . #<LispSyntax>))
          ... body2 ...))))
```
ここまで来れば簡単だ。
Rubyでのマクロ変換器を拡張して、%lexical-syntaxにぶら下がっているキーワードを拾いながら再帰的に body1 や body2 の S式を変換していけばいい。
もちろん、レキシカルスコープを持っているので同名のキーワードが出現すれば内側のキーワードでシャドウしながら適用する。

ブログを書いている時点では*内部表現1*→*内部表現2*→*展開形*の部分だけ動いている。(キーワードがちゃんとレキシカルスコープになっているかまではテストできていないが)
さて、実際に全体が動くかやってみよう。
