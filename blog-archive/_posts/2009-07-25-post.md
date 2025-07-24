---
layout: post
title: "Ruby 1.8と Ruby 1.9の違い"
date: 2009-07-25
categories: Ruby
---
*[Nendo*]の文字リテラルの扱いをどうしようかとRubyを調べてみると、Ruby 1.8とRuby 1.9に違いがあることを知った。
意外と大きな仕様変更なのではないかと思う。
 [<Think IT> 先取り！Ruby 1.9.1 (2/3)](http://www.thinkit.co.jp/cert/article/0709/26/2.htm)
   この変更に伴い、いくつか文字列まわりに重要な変更が発生します。
 例えば、文字の扱いがいろいろと変わります。従来、文字列に対して「
 String#*n*」とすると、バイト列のn番目の数値が返ってきました。つま
 り、"Hello"*0*は72を返す、といった具合です。しかし、今後文字列はエ
 ンコード情報を保持しますので、"Hello"*0*は"H"という1文字を返すよう
 になります。

Ruby 1.8では数値を返す。
```javascript
$irb
>> ?a
?a
=> 97
>> ?a.class
?a.class
=> Fixnum
```

Ruby 1.9では文字列1文字を返す。
```javascript
$ irb
irb(main):001:0> ?a
?a
=> "a"
irb(main):002:0> ?a.class
?a.class
=> String
```

*[Nendo*]の世界では、文字リテラルというのは無くして、1文字の文字列で代用出来るんじゃないかと思っている。
*[Nendo*]の処理系自体は、Ruby 1.8とRuby 1.9で動くようにしたいので、Nendoのユーザはこの差は意識しなくても良いはずだ。
