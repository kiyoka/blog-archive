---
layout: post
title: "次はアプリを試作してみよう(3)"
date: 2009-08-18
categories: Nendo
---
私がRubyで書いているLisp方言、 *[Nendo*]の開発状況続き。

let* と case と condの (text => expr) 形式をサポートした。
あとは、assoc系のユーティリティを作ったら、本格的にstowspecのプログラミングに戻ろうと思う。

さて、stowspecの抜粋を紹介しよう。
例えば、xxxx.tar.gz から .tar.gzを外した部分(basename)を求めるプログラムは次の様に書けるようになった。
```lisp
;; `regex' is a string ( not a regex object )
;; returns ( $0-string  $1-string  $2-string  $3-string ... )
(define (regex-match regex str)
  (let1 matchdata ((. str match) regex)
    (if matchdata
        (matchdata.to_a.to_list)
        nil)))

(define (tgz-to-basename tgz)
  (define archive-file-pattern "(*a-zA-Z*.*)")
  (cond
   ((regex-match (+ "^" archive-file-pattern "(.tar.gz|.tgz|.tar.bz2)$") tgz)
    =>
    (lambda (m)
      (second m)))
   (else
    nil)))

;; test
(list
 (tgz-to-basename "abc-1.2.3.tar.gz")
 (tgz-to-basename "abc-1.2.3.tar.bz2")
 (tgz-to-basename "abc-1.2.3.tgz")
 (tgz-to-basename "file.txt"))
```

結果は、以下の通り。
```
(abc-1.2.3 abc-1.2.3 abc-1.2.3 nil)
```

regex-matchが返すmatchdataの取りまわしがcond で自然に書ける様になった。
