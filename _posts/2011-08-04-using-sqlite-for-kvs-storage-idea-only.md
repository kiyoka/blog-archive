---
layout: post
title: "SQLiteをKVSのストレージに使う(アイデアのみ)"
date: 2011-08-04
categories: アイデア
---
 ![img](http://nosql-database.org/PICS/nosql-logo.gif)
SQLiteのテストスイート項目数の多さは有名だ。項目数の多さが欠陥の少なさを示しているわけではないが相関はあるだろう。
こいつをKVSのストレージとして使えば、ソフトウェアのバグによるデータ破損が発生しにくいKVSが実現できるのではないかというアイデア。

KVSは星の数ほどあるが、コードの信頼性の評価は難しい。
普及率も把握できないし、参考にできるのは、どこそこのサイトで実運用しているという情報だけというのが正直なところ。
そこで、SQLiteをバックエンドに持つKVSを使えばSQLiteの枯れたコードを利用して信頼性を確保できる。
SQLiteはiPhoneやAndroid、ThunderBirdにも入っているため、コードはななり枯れていると推測できる。

そのようなソフトウェアをちゃっちゃとでっち上げるとすれば、きっとNoSQLiteという名前になるだろうなー。
と思ってGoogleで検索してみると… もう既にあった。

 [DBIx::NoSQL - search.cpan.org](http://search.cpan.org/~rokr/DBIx-NoSQL-0.0017/lib/DBIx/NoSQL.pm)
  DBIx::NoSQL - NoSQL-ish overlay for an SQL database
 
 DESCRIPTION
  DBIx::NoSQL is a layer over DBI that presents a NoSQLish way to
  store and retrieve data. It does this by using a table called
  __Store__. Once connected to a database, it will detect if this
  table is missing and create it if necessary
  
  When writing data to the store, the data (a HASH reference) is first
  serialized using JSON and then inserted/updated via DBIx::Class to
  (currently) an SQLite backend
  
  Retrieving data from the store is done by key lookup or by searching
  an SQL-based index. Once found, the data is deserialized via JSON
  and returned
  
  The API is fairly sane, though still beta

同じ作者のgithubを見に行ってみると。
過去の作品だと思われる、同様のものがあった。

 [robertkrimen/FutonDb - GitHub](http://github.com/robertkrimen/FutonDb)
  FutonDb - A NoSQL-ish overlay for an SQL database

作った動機はわからないけれども、作品はあるわけで、同じことを考える人はいるんだなぁと思った。

ついでにPythonにも同様のものがあったり。これはオブジェクトをシリアライズして保存するやつだけど。
 [y_serial – warehouse compressed Python objects with SQLite — y_serial v0.60 documentation](http://yserial.sourceforge.net/)
  y_serial = serialization + persistance. In a few lines of code,
  compress and annotate Python objects into SQLite; then later
  retrieve them chronologically by keywords without any SQL. Highly
  useful NoSQL “standard” module for a database to store schema-less
  data.

さて、SQLiteをバックエンドストレージにした場合、パフォーマンスは出ないだろうからKVSである必要性が無いんだよなーという、やはり本質的なところに戻ってきてしまった。
きっと、超高速なKVSの裏方でレプリケーションスレーブにしてバックアップ専用に使うとかが現実的なのかな。
例えば、次のような構成かな。
 Tokyo Tyrant => レプリケーション => NoSQLite(SQLite内蔵)
 または
 Kyoto Tycoon => レプリケーション => NoSQLite(SQLite内蔵)

なんか、KVSのインタフェースを持つ必要性がうぃんあらなくなってきたぞ。あれれアイデアが破綻した…(笑)
