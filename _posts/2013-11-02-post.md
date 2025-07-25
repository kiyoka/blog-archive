---
layout: post
title: "静的型チェックの設計メモ(1)"
date: 2013-11-02
categories: Nendo
---
 ![img]({{ "/assets/images/iStock_000019986662XSmall.jpg" | relative_url }})
自分用備忘録。

## 型付けと、型チェックは2フェーズにする必要あり

理由は、再帰的に定義された関数は自身を定義するまで自身の型が不明なので、1パス目ではチェックできない。

 サンプルコード
```lisp
;; fact
(define (fact n)
  (if (zero? n)
      1
      (* n (fact (- n 1)))))
```

このコードは、コンパイルフェーズで以下のようにマクロ展開される。
```lisp
(define fact
  (lambda (n)
    (if (zero? n)
        1
        (%tailcall (* n (fact (- n 1)))))))
```

上のコードで使われている関数群 zero? %tailcall * - と フォーム (if a b c) が全て副作用なしとして型付けされていたとする。
ここで、変数factの型を1パス目で型チェックしようすると、factの型が未定義なので失敗する。
従って、1パス目でfactの型を決定してから、2パス目で型チェックをする必要がある。

## 応用編
次のようなletrecで定義された束縛変数においても同様。
```lisp
(define (append a b)
  (letrec ((append-reverse
            (lambda (a b)
              (if (pair? a)
                  (append-reverse (cdr a) (cons (car a) b))
                  b))))
    (append-reverse (reverse a) b)))
```

それにしてもこのappendの定義ってよくできているなぁ。
誰が書いたのだろう… Chibi-Schemeから持ってきたハズ…
