---
layout: post
title: "anything.el is everything!"
date: 2008-04-23
categories: Emacs
---
今更ながら、[anything.el](http://www.emacswiki.org/cgi-bin/wiki/anything.el) を使いはじめた。
すごいすごいとはいろんなブログで読んでいたけど、これは本当にすごいわ。
いままでバッファを切りかえる際、バッファ一覧を C-xC-b で出して C-xC-o してバッファ一覧からインクリメンタル検索していたのが、
C-; してインクリメンタルするだけになった。
これは、Emacsの標準機能になるのも時間の問題だと思う。
rubikitchさんところの[2007-07-25 - ’(rubikitch wanna be (a . lisper))](http://d.hatena.ne.jp/rubikitch/20070725)が参考になる。
ちなみに、私の設定はこんな感じ。これでどんな状態からでも C-;でanythingが起動するぞ。
```lisp
(iswitchb-mode 1)

(require 'anything-config)
(setq anything-sources (list anything-c-source-buffers
                             anything-c-source-bookmarks
;;                             anything-c-source-recentf
                             anything-c-source-file-name-history
                             anything-c-source-locate))
(define-key anything-map (kbd "C-p") 'anything-previous-line)
(define-key anything-map (kbd "C-n") 'anything-next-line)
(define-key anything-map (kbd "C-v") 'anything-next-source)
(define-key anything-map (kbd "M-v") 'anything-previous-source)
(global-set-key (kbd "C-;") 'anything)
(anything-iswitchb-setup)
```
この設定を動かすには、[EmacsWiki: anything.el](http://www.emacswiki.org/cgi-bin/wiki/anything.el)と[EmacsWiki: anything-config.el](http://www.emacswiki.org/cgi-bin/wiki/anything-config.el)の両方のインストールが必要。
Emacs使っている人はぜひ[anything.el](http://www.emacswiki.org/cgi-bin/wiki/anything.el) を使おう。
