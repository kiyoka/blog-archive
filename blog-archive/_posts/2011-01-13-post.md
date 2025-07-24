---
layout: post
title: "まじめにSchemeのportをサポートする時間が無いので保留"
date: 2011-01-13
categories: Nendo
---
NendoのjsonライブラリをGaucheのrfc.jsonライブラリと互換にしたかったのだが、時間が無いので保留にすることにした。
Nendoの他のライブラリと同じように、portの変わりにRubyのFileオブジェクトでお茶を濁すことにした。
優先すべきはSekkaからGoogle IME APIにアクセスして未知語を獲得する機能なので、今は寄り道はやめておこう。
毎日30分だけNendoに割り当てる方針で、本当に少しづつだけど前進している。

ちなみに、portを実装するには peek-char を正しく対応しないといけないが、労力の少ない方法が思いつかない。
