---
layout: post
title: "Schemerにとって理想のRubyとは(2)"
date: 2008-03-04
categories: Ruby
---
*[kiyoka.2008_02_25*]の続き。
Rubyにnamed letみたいなのが欲しい
再起でレキシカルアナライザが自然に書けるよ。
```lisp
def lexer( f )
  tokenList = * *
  let loop { |ch = f.readchar, prev, token = ""| 
    case ch
    when f.eof?
    else
      # トークンの蓄積
      case ch
      when ' ' '\t'
        tokenList << token
        token = ""
      else
        token += ch
      end
      loop( f.readchar, ch, token )
    end
  end
  tokenList
end
```
本物のRubyにはないコーディングは、たぶん次の三つだけだと思う。
# ブロック構文の引数の初期値指定
# let構文
# Procオブジェクトを.call()を付けなくても呼出せる
要するに、Schemerは何でもλに見えてしまうので、Rubyにもそれを期待してしまう。
もしこれが出来てもRubyの構文自体はあまりくずれないと思うけどなぁ。
