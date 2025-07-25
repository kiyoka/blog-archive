---
layout: post
title: "quack.elのλの字形が気にいらないので変更した"
date: 2007-12-16
categories: Emacs
---
quack.elの defconstを次の様に変更するとよい。

```lisp
(defconst quack-lambda-char (string-to-char "λ"))
```

オリジナルは半角で表示されるが、これで全角のラムダが表示されるようになる。
注意点としては、iso-2022-jpで保存しないといけない。
忘れるといけないので2行目に次の様なコメントを入れておいた。
Emacsがこのファイルを開くときに確実にエンコードをiso-2022-jpと認識してくれるので一石二鳥。

```
;;; quack.el --- enhanced support for editing and running Scheme code
;;; λの表示文字の為、このファイルはiso-2022-jpで保存してください。 (kiyoka)
```
