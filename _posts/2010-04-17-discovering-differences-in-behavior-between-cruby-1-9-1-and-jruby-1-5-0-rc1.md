---
layout: post
title: "CRuby-1.9.1とJRuby 1.5.0-RC1の挙動の違いを発見"
date: 2010-04-17
categories: JRuby
---
JRubyのバグかなとTwitterでつぶやいたら、[@hiro_asari](http://twitter.com/hiro_asari)さんから、どんな内容か教えて下さいと返信もらったので、これはその説明用エントリです。[@hiro_asari](http://twitter.com/hiro_asari)さんありがとうございます。
 [Twitter / Hiro Asari: @kiyoka JRubyで1.9相当の挙動を促すに ...](http://twitter.com/hiro_asari/status/12284922871)
 @kiyoka JRubyで1.9相当の挙動を促すには--1.9というフラグが必要です。そ
 れでも違う場合には、どのような物か提示してもらえれば調査してみます。

このあたり、Ruby処理系間の仕様の調整(RubySpecとかあるけど)のノウハウが無いので、後は[@hiro_asari](http://twitter.com/hiro_asari)さんにお願いできればと思います。
仕様がちょっと違うというだけのバグなので、JRubyの中身を知っている人ならスグに直せそうな問題です。(JRuby側を合わせるとしたらですが...)
それから、本ブログからソースコードをコピペする場合は、ページタイトル右横の*PLAIN TEXT*アイコンで本ページのTEXT版が出てきます。その方法を試してみて下さい。

## 現象
次のメソッドの返す型が違う。
CRubyはシンボルの配列を返し、JRubyは文字列の配列を返す。
- global_variables
- instance_variables
- local_variables

class_variablesだけは両方の処理系でシンボルの配列を返す。

## 実験結果

## * 実験用ソースコード print_variables.rb
```python
# -*- encoding: utf-8 -*-

$global_var1 = 1
$global_var2 = 2

class A
  @@class_var1 = 1
  @@class_var2 = 2
  def initialize
    @instance_var1 = 1
    @instance_var2 = 2
  end

  def view_variables
    local_var1 = 1
    local_var2 = 2

    print "global_variables:\n  "
    p global_variables
    print "class_variables:\n  "
    p A.class_variables
    print "instance_variables:\n  "
    p self.instance_variables
    print "local_variables:\n  "
    p local_variables
  end
end

a = A.new
a.view_variables
```

## * JRubyの挙動
```bash
$ jruby --1.9 --version
jruby 1.5.0.RC1 (ruby 1.9.2dev trunk 24787) (2010-04-14 0b08bc7) (Java HotSpot(TM) Client VM 1.5.0_22) *ppc-java*
$ jruby --1.9 print_variables.rb 
global_variables:
  *"$$", "$`", "$@", "$\\", "$<", "$=", "$!", "$.", "$;", "$&", "$\"", "$'", "$,", "$+", "$>", "$:", "$/", "$~", "$0", "$_", "$*", "$?", "$-n", "$-I", "$-p", "$global_var1", "$-a", "$-l", "$global_var2", "$-d", "$-K", "$stderr", "$stdout", "$LOAD_PATH", "$SAFE", "$FILENAME", "$stdin", "$VERBOSE", "$LOADED_FEATURES", "$deferr", "$defout", "$PROGRAM_NAME", "$KCODE", "$DEBUG"*
class_variables:
  *:@@class_var1, :@@class_var2*
instance_variables:
  *"@instance_var2", "@instance_var1"*
local_variables:
  *"local_var1", "local_var2"*
```

## * CRubyの挙動
```bash
$ ruby --version
ruby 1.9.1p376 (2009-12-07 revision 26041) *powerpc-darwin9.8.0*
$ ruby print_variables.rb 
global_variables:
  *:$;, :$-F, :$@, :$!, :$SAFE, :$~, :$&, :$`, :$', :$+, :$=, :$KCODE, :$-K, :$,, :$/, :$-0, :$\, :$_, :$stdin, :$stdout, :$stderr, :$>, :$<, :$., :$FILENAME, :$-i, :$*, :$?, :$$, :$:, :$-I, :$LOAD_PATH, :$", :$LOADED_FEATURES, :$VERBOSE, :$-v, :$-w, :$-W, :$DEBUG, :$-d, :$0, :$PROGRAM_NAME, :$global_var1, :$global_var2, :$-p, :$-l, :$-a, :$1, :$2, :$3, :$4, :$5, :$6, :$7, :$8, :$9*
class_variables:
  *:@@class_var1, :@@class_var2*
instance_variables:
  *:@instance_var1, :@instance_var2*
local_variables:
  *:local_var1, :local_var2*
```

今回初めてTwitterが有効活用されそうな予感です。



---

**コメント by あさり:**  
念の為に追記しておきますと、http://twitter.com/hiro_asari/status/12359856172 に書きました通り、この点は http://bit.ly/acyiqv で対処しました。ご報告に感謝します。


---

**コメント by kiyoka:**  
あさりさん、すばやい対処ありがとうございます。お役に立ててなによりです。
CRuby1.9互換競争で、JRubyがトップを走ってそうですね。
また何か見つけたら報告します。

**コメント by あさり:**  
念の為に追記しておきますと、http://twitter.com/hiro_asari/status/12359856172 に書きました通り、この点は http://bit.ly/acyiqv で対処しました。ご報告に感謝します。
