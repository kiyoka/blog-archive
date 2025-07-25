---
layout: post
title: "Rubyのよくわからない挙動(1)"
date: 2009-03-21
categories: Ruby
---
## ===メソッド(比較演算子)の挙動がよくわからない。
クラス A を定義し、インスタンスを a に代入する。
```python
$ irb
>> class A ; end
class A ; end
=> nil
>> a = A.new
a = A.new
=> #<A:0x3637ec>
```

== がtrueになるのはわかる。
```python
>> a.class == A
a.class == A
=> true
```

=== では何故falseになるのか。
```python
>> a.class === A
a.class === A
=> false
```

=== がtrueになってくれないと === 演算子が適用される case 〜 when が使えない。
例えば、
```
  case val.class
  when Cell
    Cell型の場合の処理
  when Fixnum
    Fixnum型の場合の処理
  end
```
という記述はダメ。どれにもマッチしない。

こう書けばいけるけど、ちょっと苦しい。
```
  case val.class.to_s
  when "Cell"
    Cell型の場合の処理
  when "Fixnum"
    Fixnum型の場合の処理
  end
```

こんな場合Rubyの定石として、どう書くんだろう。



---

**コメント by Grape:**  
勉強し始めたばかりなので、まだ何とも言えませんが、
Rubyの===は、「サブクラスで適宜再定義される」とあるので、オブジェクトによって挙動が違う可能性があります。
つまり、実装によっては必ずしも型が同じで値が同じ時にTrueという動きではないかもしれません。

的外れな答えでしたら、すみませんorz


---

**コメント by mogya:**  
＞こんな場合Rubyの定石として、どう書くんだろう。

こうらしいです。
 case val
  when Cell
    Cell型の場合の処理
  when Fixnum
    Fixnum型の場合の処理
  end

[ruby-list:10473]case with Class からはじまる一連のスレッドに書いてありました。
http://blade.nagaokaut.ac.jp/cgi-bin/vframe.rb/ruby/ruby-list/10473?10428-11968





---

**コメント by kiyoka:**  
Grapeさん、mogyaさん、コメントどうもです。
mogyaさんに教えてもらった方法でいけそうです。
内部の仕組みはよくわかりませんが、これで短く書けますね。(そのへんがRubyに対して好みがわかれるところでしょうが...)
以下、実験結果です。

irb(main):001:0> class A ; end
=> nil
irb(main):002:0> a = A.new
=> #<A:0x4023c478>
irb(main):003:0> case a
irb(main):004:1> when A
irb(main):005:1> 1
irb(main):006:1> when B
irb(main):007:1> 2
irb(main):008:1> else 
irb(main):009:1* 3
irb(main):010:1> end
=> 1

今作っているLispインタプリタをこのスタイルに直しておきますです。

**コメント by Grape:**  
勉強し始めたばかりなので、まだ何とも言えませんが、
Rubyの===は、「サブクラスで適宜再定義される」とあるので、オブジェクトによって挙動が違う可能性があります。
つまり、実装によっては必ずしも型が同じで値が同じ時にTrueという動きではないかもしれません。

的外れな答えでしたら、すみませんorz

**コメント by mogya:**  
＞こんな場合Rubyの定石として、どう書くんだろう。

こうらしいです。
 case val
  when Cell
    Cell型の場合の処理
  when Fixnum
    Fixnum型の場合の処理
  end

[ruby-list:10473]case with Class からはじまる一連のスレッドに書いてありました。
http://blade.nagaokaut.ac.jp/cgi-bin/vframe.rb/ruby/ruby-list/10473?10428-11968



