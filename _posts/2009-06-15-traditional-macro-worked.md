---
layout: post
title: "伝統的なmacroが動いた"
date: 2009-06-15
categories: Nendo
---
ここまで長い道程だったが、macroが動いた。
実際にmacroを実装してみるとmacroがどういうものかやっと理解できた気がする。

## 伝統的なmacroの例

 引数に指定された変数をインクリメントするmacroを定義
```lisp
nendo> (define inc (macro (x) (list 'set! x (list '+ '1 x))))
#<LispMacro:0x00083fcc@(stdin):1>
```

 変数aを準備
```lisp
nendo> (define a 10)
10
```

 macroの展開結果を見る
```lisp
nendo> (macroexpand1 '(inc a))
(set! a (+ 1 a))
```

 実際にインクリメントしてみる
```lisp
nendo> (inc a)
11
```

 引数に指定した処理を2回実行するmacroを定義
```lisp
nendo> (define twice (macro (x) (list 'begin x x)))
#<LispMacro:0x000720d8@(stdin):6>
```

 (inc a)をマクロで2回実行
```lisp
nendo> (twice (inc a))
13
```

 macroの展開結果を見る(1回だけマクロ展開)
```lisp
nendo> (macroexpand1 '(twice (inc a)))
(begin (inc a) (inc a))
```

 macroの展開結果を見る(2回のマクロ展開)
```lisp
nendo> (macroexpand1 (macroexpand1 '(twice (inc a))))
(begin (set! a (+ 1 a)) (set! a (+ 1 a)))
```

さて、orとandをmacroで実装してみよう。と思ったが、可変長引数をサポートしていないので、書けないという問題に気がついた。orz.
やっぱり可変長引数は必須なのか...

## macroの可変長引数サポートについて
その後、macroに可変長引数をサポートしようとして,
```lisp
(define name (macro (arg1 arg2) body))
```
という形式ではゼロ個以上の可変長引数がサポートできないことが分かった... o.rz.
要するに、lambdaが入る部分にmacroというキーワードが入る形で考えていた。
そうすると、なにが問題かというと、ゼロ個以上の可変長引数を書きたい場合は、気持ち的には
```lisp
(define name (macro (. rest) body))
```
だが、S式として成立しない。 (. rest) の部分がS式としてエラーとなる。

TinySchemeはmacro定義をつぎの形式で行なうが、この形式ならうまくいく。
```
(macro (name arg1 arg2) body)
```
または、
```lisp
(macro name (lambda (arg1 arg2) body)
```
となっている。

この形式なら
```
(macro (name . rest) body)
```
とかけるのね。
つまり、defineと同じイメージでmacroキーワードを組み立てないといけないのだな。



---

**コメント by shiro:**  
(macro rest body) じゃまずいですか? > ゼロ個以上の可変長引数


---

**コメント by kiyoka:**  
＞ (macro rest body) じゃまずいですか?
おっと、今R5RSの仕様をみたら、lambdaがその形式を取るんですね。
初めて知りました。
macroも同じ形式で問題ないです。
というか、lambdaのほうもその形式をサポートしないといけないですね。

ありがとうございます。

**コメント by shiro:**  
(macro rest body) じゃまずいですか? > ゼロ個以上の可変長引数
