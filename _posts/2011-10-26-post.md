---
layout: post
title: "Nendo 0.5.4 リリース"
date: 2011-10-26
categories: Nendo
---
*[Nendo*] 0.5.4をリリースしました。(リリースノート: *[Nendo.ReleaseNote*])
![img]({{ "/assets/images/rubygems_icon_128.png" | relative_url }})
## リリースの目玉
例外をハンドリングできるようになりました。道具立てはguardとunwind-protectです。
GaucheとAPIをなるべく似せて、Gaucheに慣れた人が新しく覚えることを少なくしました。 (*[Nendo.ReferenceManual*] のguardのあたり参照)
テストフレームワークの nendo.testもgauche.test同様のAPIにしています。
Gaucheは独自の例外オブジェクトを持っていますが、Nendoでは例外オブジェクトとしてRubyのそのものを使うことになっているので、Rubyのオブジェクトをそのまま指定できるようにしました。
RuntimeErrorやArgumentErrorやTimeout、Errno::ECONNREFUSEDなんかがそのまま書けます。

GaucheとRubyの両方知っている人は、(exc.is_a? TypeError)のくだりなんかは非常に気持ち悪いかもですね。GaucheとRubyのどっちになりたいんだよと。
例)
```
(guard
 (exc (else (sprintf "Type is *%s*" (exc.class))))
 (error "This is RuntimeError"))
```
 → "Type is *RuntimeError*"

```
(guard
 (exc (else (sprintf "Type is *%s*" (exc.class))))
 (raise ArgumentError))
```
 → "Type is *ArgumentError*"

```ruby
(guard
    (exc ((exc.is_a? RuntimeError)
          "Type is *RuntimeError*")
         ((exc.is_a? TypeError)
          "Type is *TypeError*"))
  (+ (Array.new) 1)
  (error "This is RuntimeError"))
```
 → "Type is *TypeError*"

ついでにguardを使って、unwind-protectも実装しました。
Nendoでも衛生的なマクロ(syntax-rules)をサポートしたおかげで、このようなマクロもあっという間に書けるようになりました。
だいぶライブラリが積み上ってきた感があります。

以下リリースノートです。
## version 0.5.4
- guardフォームをサポートした。
- unwind-protectフォームをサポートした。
- raiseフォームの引数を可変長引数にした。
 Gauche 0.9.2の仕様に似せた。
- テストフレームワーク nendo.test に期待した例外が上がるかどうかテストする機能を追加した。
 Gauche 0.9.1に付属のgauche.testをポーティングし、(test-error <例外>)関数などを実現した。
- util.listのテストケースにRuntimeErrorが発生するテストケースを追加した。
 Nendo 0.5.3まではコメントアウトしていたもの。

## 次の目標
もうそろそろNendoで実践的なWebサービスを作っていってもだいじょうぶかなと思い始めました。
Webフレームワーク、ドキュメントStore(MongoDB)などと組み合わせて使う場合、どんなやりかたが良いのかを考えながらライブラリを拡張していきたと思います。
それから、副作用のあるコードブロックのチェック機能(pure S式)もぼちぼち考えていきます。こちらは優先度低いです。

あっ、その前にリファクタリングする予定がありました。
nendo.rbの行数がとんどもないことになっているので、ファイル分割します。
それからいろいろ手をつけていきます。
