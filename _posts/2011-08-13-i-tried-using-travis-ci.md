---
layout: post
title: "Travis CIを使ってみた"
date: 2011-08-13
categories: Ruby
---
Travis CIはRubyのオープンソースプロジェクトの継続的インテグレーション(CI)を行うプラットフォーム。
[Travis CI - Distributed build platform for the Ruby community](http://travis-ci.org/)
 An open-source, distributed build system for the Ruby community.

使ってみて、非常に便利だったので紹介したい。
といっても、現段階では複数versionのRubyでビルドとテストを行う機能に限定されている。
Github上のオープンソースプロジェクトを持っている人に特化している。
Ruby + GitHubでない人はゴメン。
 ![img](http://pix.am/At7b.png)
私は、Rubyで書かれた*[Nendo*]というLisp処理系を開発していて、これまで複数のRuby処理系で全部テストするの面倒だった。
リリースの度に複数の処理系を切り替えてテストをするのが面倒くさくなってきて、「今回はJRubyのテスト端折ろうかな」と考えたことは一度では無い。
Travis CIを使えば、そのような面倒なプロセスを自動化してくれる。スゲー。
GitHub上の指定したブランチのpushタイミングで、自動的に複数のRubyバージョンのビルド&テストが開始する。

まずは試しに、*[Nendo*]のテストスイートをCRuby 1.9.2とCRuby 1.9.3の両方でテストする設定をした。
早速、1.9.3側だけエラーが出た。
 ![img](http://pix.am/P1FE.png)

なんと Dateクラスで1970年からの通算秒のフォーマットが変わっているようだ。
そんなテスト項目を設定している自分が悪いのだけど、まあこういう仕様変更も発見できるわけだ。
 ![img](http://pix.am/yqX6.png)

その後、調子に乗ってJRubyもテストするように設定した。
しかし、自分の手元の環境とは違い Travis CIの環境では正しく動かないテスト項目がある。
多分JRubyの基本的なバグだと思うが、手元で再現しないのでいったん保留にしておくことにした。残念…
 ![img](http://pix.am/cbFv.png)

まあ、まだTravis CIはalphaサービスなので今後の改善に期待したい。きっと直るんじゃないかな。
 ![img](http://pix.am/z2tG.png)
それにしても、このようなサービスが無料で利用できるのは凄いことだ思う。
やっぱ、Rubyのように勢いのあるコミュニティ周辺で遊ぶのはメリット大きいなぁと感じる今日この頃です。
それと、Rubyコミュニティには自動テストをてんこ盛り書くという文化は良いです。
