---
layout: post
title: "Rubyのブロック構文をサポートした"
date: 2010-07-30
categories: Nendo
---
私がRubyで書いているLisp方言、 *[Nendo*]について。

## 新しく追加したブロック生成構文
*[Nendo*]でRubyのブロックを生成する構文を追加した。
Rubyのブロック構文とは、以下のような {} で囲んだコード片(クロージャ)をメソッドに渡す構文である。
```ruby
#  ファイルの１行目を読み込んで出力する
open( "file.txt" ) { |f|
  puts f.readline
}
```
Rubyのライブラリにはブロックを受けとるメソッドが多く、*[Nendo*]からRubyのライブラリをまともに使おうと思ったら*[Nendo*]でブロックを生成する方法が必須となる。
いろいろ考えた結果、&block というプリミティブなキーワードを追加することにした。他に考えた案よりも、実装が簡単だった。
(*[Nendo*]のlambdaはRubyのブロックとは仮引数の渡しかたが違うため、*[Nendo*]/no lambdaをそのままブロックとして渡すことができない)
&blockの構文は lambda と類似しており (&block (arg ...) body ...) のように "lambda"のかわりに"&block" と書くだけ。
上記のコードを*[Nendo*]で書くとこうなる。
```ruby
;; ファイルの１行目を読み込んで出力する
(.open "file.txt" (&block (f)
  (.puts (f.readline))))
```

Rubyでも別の書き方にすると、*[Nendo*]のコードと似た感じになるのはRubyに詳しい人ならご存知だろう。
```ruby
#  ファイルの１行目を読み込んで出力する
open( "file.txt", &Proc.new { |f| 
  puts f.readline
} )
```

※ 他にも (& (lambda ...)) と書くとRubyのブロックに変換してくれるという案もあったけど、実装の簡単さと視認性が大きく変わらないという理由で上記のようにした。

## sortライブラリを楽して実現
前から*[Nendo*]のために自前でsortアルゴリズムを書くのはいやだなと思っていた。
せかっくRubyが組込みでsortを用意してくれているので、それを使わない手はない。かなりチューニングしてくれているハズだし。
今回、ブロック生成構文を使って sort と sort-by ができた。
```lisp
(define (sort lst . cmpfn)
  (let1 cmpfn (get-optional cmpfn #f)
    (to-list
     (if cmpfn
         (lst.to_arr.sort (&block (a b) (cmpfn a b)))
         (lst.to_arr.sort)))))


(define (sort-by lst keyfn)
  (to-list
   (lst.to_arr.sort_by (&block (item) (keyfn item)))))
```

## まとめ
- (&block (arg ...) body ...) というRubyのブロックを生成できる構文を用意した。
- それを使って*[Nendo*]のsortライブラリはRubyのsortをそのまま使えた。

いろんなライブラリで、もうちょっと&blockを試してみて、問題なさそうならこの仕様で行く予定。
