---
layout: post
title: "Nendoで定義した関数をRubyから呼べるようになった"
date: 2010-08-25
categories: Nendo
---
私がRubyで書いているLisp方言、 *[Nendo*]について。

タイトルの通り、*[Nendo*]で定義した関数をRubyから呼べるようになった。
これで、Nendoで書いたコードをRubyのライブラリとして呼べるようになる。

以下はサンプルプログラム * export-lisp-functions.rb *
```lisp
#!/usr/local/bin/ruby

require 'nendo'

def main
  core = Nendo::Core.new()
  core.loadInitFile
  lst = * "a", "b", "c",
          [ "d", "e" *.to_list
        ].to_list
  core.evalStr( '(define (sexpToString sexp) (write-to-string sexp))' )
  core.evalStr( '(export-to-ruby sexpToString)' )
  core.evalStr( '(use text.tree)' )
  core.evalStr( '(define (treeToString sexp) (tree->string sexp))' )
  core.evalStr( '(export-to-ruby treeToString)' )
  puts core.sexpToString( lst )
  puts core.treeToString( lst )
end

main
```

Nendoの世界で (export-to-ruby シンボル) と宣言すると、Nendo::Coreクラスのインスタンス(サンプルでは core) に同名のメソッドが動的に増えるのだ。
動的にメソッドが生えるというのはなんか気持ち悪いけれど、Rubyの世界では普通なのです。ほんとほんと。
※ 現状は、引数の数が固定の関数しか export できないルールにしている。まあ困らんだろう。

 *実行結果*
```bash
$ ./export-lisp-functions.rb 
("a" "b" "c" ("d" "e"))
abcde
```

これで、Nendoで書いたアプリを、RackやSinatra(Webアプリケーションフレームワーク)に乗せることができるようになったはず。
早速、Sekkaという新しい日本語変換エンジンをのせていくところから始める予定。
