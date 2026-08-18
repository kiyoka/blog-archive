---
layout: post
title: "Sekka 0.8.6 リリース"
date: 2011-04-14
categories: Sekka
---
SKKライクな日本語入力メソッド *[Sekka*] 0.8.6をリリースしました。(リリースノート *[Sekka.ReleaseNote*])
 ![img](http://mrg.bz/NbpKsE)

## version 0.8.6
- gemの依存規則で、Nendoの依存バージョンとして0.4.1のみとした。
 今後、NendoのライブラリAPIの仕様変更で動かなくなる可能性があるため。
- sekka-server起動時、sekka-serverが使用中のNendoバージョンを表示するようにした。

機能的には、0.8.5から何も変わらないので特にバージョンアップする意味はありません。
今後リリースするNendoに下位互換性が無くてもSekkaに影響が無いようにするためです。(実際、一部APIで下位互換性が失われている)

実験したところNendo 0.4.1とNendo 0.5.0の両方がインストールされていても、Sekka 0.8.6はNendo 0.4.1を使うことを確認しました。gemってよくできてるなぁーと思います。
```
~ $ gem list nendo

*** LOCAL GEMS ***

nendo (0.5.0, 0.4.1)

~ $ sekka-server
----- Sekka Server Started -----
  Sekka version  : 0.8.6
  Nendo version  : 0.4.1
  dict-db        : /home/kiyoka/.sekka-server/SEKKA-JISYO.SMALL.tch
  memcached      : localhost:11211
  listenPort     : 12929
  proxyHost      : 
  proxyPort      : 
--------------------------------
*2011-04-14 06:14:15* INFO  WEBrick 1.3.1
*2011-04-14 06:14:15* INFO  ruby 1.9.2 (2011-02-18) *i686-linux*
*2011-04-14 06:14:15* INFO  WEBrick::HTTPServer#start: pid=11284 port=12929
```
