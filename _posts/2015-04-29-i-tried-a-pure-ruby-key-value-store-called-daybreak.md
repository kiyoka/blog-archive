---
layout: post
title: "Daybreakというpure rubyのkey-value-storeを試してみた"
date: 2015-04-29
categories: Sekka
---

## 目的
Sekkaの辞書データベースとして、プラットフォームに依存しない形式は無いものかと探している。
Sekkaの辞書データは結構大きいので、Sekkaインストール時にInternetから取得する方式にしているのだけど、プラットフォーム依存だとどうしても導入時に変換が入ってしまう。
その変換時間がバカにならない。
できれば、ダウンロードして即動かしたい。
現在Sekka辞書 1.6.1でサポートしているフォーマットはgdbm/TokyoCabinet/Redisで、どれもtsvからの読み込みが発生してしまう。

## 結論:Daybreakはメモリ消費量が多すぎてボツ
これが、試しに実装してみたブランチ。リリースはしない。
 https://github.com/kiyoka/sekka/tree/daybreak_db

in memoryデータベースなのでしょうがないとはいえ、Sekka辞書ver1.6.1では3GByteのメモリを消費してしまう。
同じin memoryデータベースのRedisだと1.2GByte程度で収まる。
Daybreak 0.3.0のドキュメントを読む限り、内部はRubyのHashをそのまま保持しているようだ。
それに対してRedisはデータ圧縮などの工夫や、その他の工夫をしているようで、メモリフットプリントが少ない。

## 感想
一般論として、pure rubyのまともなkvsは実現が困難だと思う。
データ量が小さいのであれば、pure rubyのHashクラスをそのまま使うのはありだろうが、ある程度データ量が増えると、どこかでDISKに退避したりメモリフットプリントを減らす工夫が必要だと思う。
結局RedisやTokyo CabinetなどC言語などできめ細かく実装するしかないと思う。
