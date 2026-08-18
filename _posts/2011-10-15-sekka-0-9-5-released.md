---
layout: post
title: "Sekka 0.9.5 リリース"
date: 2011-10-15
categories: Sekka
---
SKKライクな日本語入力メソッド *[Sekka*] 0.9.5をリリースしました。(リリースノート *[Sekka.ReleaseNote*])

 ![img](http://mrg.bz/NbpKsE)

大きな変更点は、sekka.elのカスタマイズ変数のデフォルト設定変更です。

これまで、Ctrl-Jとスペースキーの両方で変換確定する操作をデフォルトで有効にしてきましたが、今回スペースキーでの変換確定を無効に戻しました。
スペースキーで変換確定する操作はMS-IMEなどの一般的なIMEと操作感が同じになるため、良い面もありますが、Sekkaの最大の特徴である「モードレス」が失なわれるという大きな問題がありました。
(スペースキーの挙動を止めるためにCtrl-Gを押して、日本語変換モードを抜ける必要がある)

プログラミング中に日本語コメントや文章を入力する頻度が高くなるとモードレスでないとモード切替忘れによる入力ミスが出ます。
数ヶ月使ってみて、やはりSekkaのアイデンティティはモードレスでないといけないと思い至りました。
![img]({{ "/assets/images/sekka.before_henkan.png" | relative_url }})
   ↓*Ctrl-J*を押す。
![img]({{ "/assets/images/sekka.after_henkan.png" | relative_url }})

変換モードがあっても許せる人なら、カスタマイズ変数でスペースキーでの変換を有効にしてもらう、もしくはSKKなどを使ってもらえればいいと思います。:(

## version 0.9.5
- sekka.el: url-host関数が呼び出せず、mode-lineのSekka[]の表示が消えるバグを修正した。
  (require 'url-parse)が必要だった。
- sekka.el: sekka-kakutei-with-spacekey のデフォルト値を nil に戻した。
- sekka.el: sekka-muhenkan-key のデフォルト値をnilに設定した。
 また、指定したキーをkeymapに設定する必要があるので、カスタマイズ変数でなくした。
 例えば、.emacsで(setq sekka-muhenkan-key "q") する必要がある。
- sekka-serverの辞書追加/既に登録済みのメッセージをシンプルなものに変更した。

## 次の目標
*[Nendo*]に新しい例外処理機能を付けている最中です、その機能を使って例外まわりのテストを拡充する予定です。
