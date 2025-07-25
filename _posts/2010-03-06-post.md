---
layout: post
title: "named letをmacroで実装した"
date: 2010-03-06
categories: Nendo
---
私がRubyで書いているLisp方言、 *[Nendo*]について。

これまで、*[Nendo*]ではlet等の予約語はマクロを束縛すると正しく展開できない実装だったが、ついに予約語と同名の変数にマクロを束縛しても動作するようにした。
そうすることで、例えば named let をmacroで定義できるようになった。
```lisp
;; named letのサポート
(define let
  (macro lst
    (if (symbol? (car lst))
        ;; named let
        `(letrec ((,(first lst)
                   (lambda ,(map
                             (lambda (x)
                               (first x))
                             (second lst))
                     ,(third lst))))
           (,(first lst)
            ,@(map
               (lambda (x)
                 (second x))
               (second lst))))
           
        ;; don't touch
        `(let ,@lst))))
```

なぜこれをできるようにしたかというと、処理系全体のソースコードがコンパクトになる方向を目指しているためだ。
一般的にS式のmacroはソースコード規模を圧縮する方向に作用するため、Rubyで実装するコアはシンプルな構文のみに抑え、Lispのmacroを多用して構文を拡張した方が有利になるからだ。
Rubyではコード圧縮に限界がある。

Rubyで『named letの機能を持たない基本的なlet』と『letrec』に対応するコード生成機能が有れば、named letを*[Nendo*]のmacroで記述できる。
例えば、下記のnamed letのサンプルコードは上のマクロで解決できる。

 展開前
```lisp
(let1 total 0
  (let loop ((cnt 10))
    (if (< 0 cnt)
        (begin
          (set! total (+ total cnt))
          (loop (- cnt 1)))))
  total)
```

 展開後
```lisp
(let ((total 0))
  (letrec
      ((loop (lambda (cnt)
               (if (< 0 cnt)
                   (begin (set! total (+ total cnt))
                          (loop (- cnt 1)))))))
    (loop 10))
  total)
```

 実行結果
```
55
```

恥を晒すと、本当はSchemeのdefine-syntax相当をサポートしてそれで定義するのがまっとうな方法かも知れないが、まだそこまで自分の力量が足りていないというのが正直なところ。
しかし、これまで実際にLisp処理系を実装するのは本当に勉強になると実感した。
やればやるほど、Lispの奥深さが少しづつ感じ取れる様になった。(オマケとしてRubyにも詳しくなったし…)
Lisp系言語を本当に習得したいという人は一度は自分のLisp処理系を実装してみることをおすすめするぞ。
