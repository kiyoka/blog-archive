---
layout: post
title: "flymakeでPHPのリアルタイム文法チェック"
date: 2007-12-28
categories: プログラミング
---
ブログではいつも関数型言語の記事ばっかり書いているが、実は仕事ではPHPを使うこともある。
言語は自分では選べないというのはITの世界ではもはや常識である。
言語選択の自由を唱えるRubyのまつもとさんでもその辺は御存知でしょう(笑)
というわけで、少しでもPHPの開発効率の悪さを軽減すべく、flymake modoの設定をおこなってみた。

いろんな所でEmacsのflymakeモードの設定が書かれているが、うまく動かなかった。
例えば、このサイトのコードも動かない。
 [Syntax checking for PHP in Emacs at Blik.it - Web, Technology and Code](http://www.blik.it/2007/02/21/syntax-checking-for-php-in-emacs/)
動かない理由は『バックスラッシュが全て消えている』のが原因だと思われる。
恐らく、HTML化する時に失敗しているんだろうと思われる。
試しにHTMLソースを見るとちゃんと必要な所にバックスラッシュがちゃんと入っていたよ。

というわけで、これを試してみられたし。
私はCentOS4.4, PHP4, GNU Emacs 22.1.1, php-mode-1.2.0の環境で試した。
(このページのテキストをコピペする場合は、ページタイトル右のPLAIN TEXTというアイコンをクリックして欲しい)

```lisp
(when 
    (string-match "22" emacs-version)
  (progn
    ;; Flymake PHP Extension
    (require 'flymake)
    
    (defconst flymake-allowed-php-file-name-masks '(
						    ("\\.php3\\'" flymake-php-init)
						    ("\\.inc\\'" flymake-php-init)
						    ("\\.php\\'" flymake-php-init))
      "Filename extensions that switch on flymake-php mode syntax checks")
    
    (defconst flymake-php-err-line-pattern-re '("\\(.*\\) in \\(.*\\) on line \\(*0-9*+\\)" 2 3 nil 1)
      "Regexp matching PHP error messages")

    (defun flymake-php-init ()
      (let* ((temp-file       (flymake-init-create-temp-buffer-copy
			       'flymake-create-temp-inplace))
	     (local-file  (file-relative-name
			   temp-file
			   (file-name-directory buffer-file-name))))
	(list "php" (list "-f" local-file "-l"))))
    
    (defun flymake-php-load ()
      (setq flymake-allowed-file-name-masks (append flymake-allowed-file-name-masks flymake-allowed-php-file-name-masks))
      (setq flymake-err-line-patterns (cons flymake-php-err-line-pattern-re flymake-err-line-patterns))
      (flymake-mode t)
      (local-set-key "\C-cd" 'flymake-display-err-menu-for-current-line))

    (add-hook 'php-mode-user-hook 'flymake-php-load)))
```
