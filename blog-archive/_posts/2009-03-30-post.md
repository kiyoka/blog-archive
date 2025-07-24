---
layout: post
title: "そろそろオレ言語でもやっておくか(8)"
date: 2009-03-30
categories: 言語
---
Rubyで書いたLisp処理系の RedLisp 開発の続き。
lambdaとifの二つのスペシャルフォームを実装した結果、fact(階乗計算)関数が動くようになった。
```lisp
$ ./redlisp
redlisp> (def fact
     (lambda (n)
       (if (= n 1)
           1
           (* n (fact (- n 1))))))
          rubyExp=<<<fact = lambda { |n|
if ( _eq.call(n , 1) ) then 1 else _multi.call(n , fact.call(_minus.call(n , 1))) end
}
>>>
#<Proc:0x4022dea0@./redlisp:263> 
redlisp> (fact 10)
          rubyExp=<<<fact.call(10)>>>
3628800
redlisp> (fact 20)
          rubyExp=<<<fact.call(20)>>>
2432902008176640000
redlisp> 
```

RedLispは、まだ実験段階なので、構文エラーなどの例外処理は真面目にやっていない。
しかし、内部でS式をRubyに動的にトランスレートしてはevalするという方式を取ること自体は間違いでは無さそうという感触は得た。
 ![img](http://farm4.static.flickr.com/3601/3394736419_80a85b7aaa_m.jpg)
さて、次はどんな実験をしようかな。
let let* の実装をやってみて、Rubyのレキシカルスコープがそのまま利用できるかの確認と、map等の高階関数をどうやって実装するか等の検討かな。
その後はRubyのクラスライブラリをどうやって呼び出すかあたりが課題となるだろう。
File#openとかはブロックを渡す場合と渡さない場合があるが、そういうのをどうやって呼び出し方変えるかなど考えないといけない事が控えている。
というか、RedLispはそういう思考実験を繰返しながら、言語デザインをするのが目的だったので、早くそのレベルまでいきたいな。
