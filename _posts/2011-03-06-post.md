---
layout: post
title: "個人プロジェクトこそTDDでやるべき"
date: 2011-03-06
categories: オープンソース
---
個人プロジェクトは、プライベートな空き時間にちょっとづつ開発を進めていくというスタイルが大半だろう。
そういう場合こそ、TDDを積極的に使おう。
 ![img](http://mrg.bz/UKvA7I)

TDDの一番大きなメリットは、プロジェクトに戻る時の心理的障壁が低いこと。
これは、自分のプライベートな時間を使って自主的に進めていくプロジェクトでは、特に重要だ。
全てを頭の中にいれてなくてもプロジェクトに戻って、コードに手を入れることができるので、気軽にコードを変更できる。
大量のテストケースが、コードを守ってくれているおかげだ。

時間が細切れになり、まとまった時間があまり取れない場合は、特にTDDのメリットを感じることができる。
ドカッとまとまった時間が取れる場合は、TDDのメリットが見えにくいかもしれないが、それでも数日後にプロジェクトに戻る時の負荷が非常に少ない。
自分の場合は一番下位レイヤーの数行のライブラリ関数までテストケースを残しているので、細かい挙動を後で確認するのにも役立つ。

実際に、自分の過去のプライベートプロジェクトで、コード変更に対する心理的負荷が上がりすぎたため止まってしまったプロジェクトもいくつかある。
私の個人プロジェクトを振りかえってみよう。

## TDDでやらなかったプロジェクト
- *[Stowspec*] ( GNU Stowのヘルパーアプリ )
- [Sumibi ( 新感覚日本語入力メソッド )](http://www.sumibi.org/)
    ![img](http://www.sumibi.org/sumibi_org_WASHIlogo.png)
- *[OldType*] ( OldTypeのためのWikiシステム。GaucheベースのWikiClone )
    ![img]({{ "/assets/images/oldtype_logo.png" | relative_url }})
- [R@eply.org ( iモードメール専用Webリーダー )](http://r.eply.org/)
    ![img](http://r.eply.org/eply_org_icon.gif)
- [Predoc ( 軽量ドキュメントフォーマット )](http://www.netfort.gr.jp/~kiyoka/predoc/index_ja.html)
    ![img](http://www.netfort.gr.jp/~kiyoka/predoc/img/img_close.png)
- [TzWatch ( Lingr用の時刻表示アプリ )](http://www.sumibi.org/lingr/tzwatch.cgi)
    ![img](http://farm4.static.flickr.com/3043/2924809497_52f5ce4524_o.png)
- [Oneliner ( Emacs shell mode )](http://oneliner-elisp.sourceforge.net/index_ja.html)
- [Cmmi (configure ; make ; make install)](http://www.netfort.gr.jp/~kiyoka/cmmi/index_ja.html)
- [Sxmlcnv (SXML <-> XML)](http://www.netfort.gr.jp/~kiyoka/sxmlcnv/index_ja.html)

## TDDでやっているプロジェクト(過去2年間くらいの大半)
- *[Nendo*]    ( Rubyで実装されたLisp処理系 )
- *[Sekka*]    ( SKKライクな日本語入力メソッド )
- *[google-ime-api-normalizer*] ( Google IME APIのJSON正常化サービス )
- [fuzzy-string-match](http://github.com/kiyoka/fuzzy-string-match) ( 曖昧文字列マッチングライブラリ for Ruby )

やっぱりTDDは重要。これからの個人プロジェクトは全てTDDでやります。
もちろん本業でもTDDでやるつもり。(って今までできてないんか！ってつっこみもありながら)

## 参考文献
 これは絶対読んでおいたほうが良い。
 TDDを実践する上で手順を実際にスローモーションで見せてくれるという感じの本。
 {% include amazon.html asin="4894717115" title="テスト駆動開発入門" author="Kent Beck" %}

 TDDでやっていない過去のコードをいかにTDDに直すかという内容の本。
 これを読んだからといって、苦労はするんだけどね。
 いかんともしがたいほどテストしにくいコードをいかに壊さないようにTDDに持っていくかという本なので、本業では非常に参考になると思う。
 {% include amazon.html asin="4798116831" title="レガシーコード改善ガイド" author="マイケル・C・フェザーズ, ウルシステム" %}
ズ株式会社



---

**コメント by sion:**  
前から気になってたので、この機会にと、早速 Amazon で購入。読んでみました。普段の開発工程と、かなりの部分で、酷似していて、明確に「テスト」を意識するかどうか、程度の違いだけだったため、うんうん、そうそう、と、抵抗なく読み進められました。ペアプロにも興味深々なのだけど、なかなか、踏み切れない・・・。
アカデミックで、ホットな情報、いつも感謝しています。


---

**コメント by kiyoka:**  
文脈からいくと、読まれた本は「テスト駆動開発入門」のほうですね。
sionさんは普段からテスト駆動に近い開発スタイルなんですね。
私の場合、本業ではテスト駆動かどうかは人依存だったり（まあ、スキル依存もありますが...) なかなかうまくいっておらず、「レガシーコード」が発生しがちです。
この状況をなんとかして、打開したいと思っています。
個人プロジェクトやオープンソースプロジェクトは期限が無い分、徹底的にこだわることができるので、TDDを実践できて結果的にうまくまわせるのですが、本業だとどうしても負の連鎖に陥りがちです。
うーん。いまそこにあるホットな課題なんです。

**コメント by sion:**  
前から気になってたので、この機会にと、早速 Amazon で購入。読んでみました。普段の開発工程と、かなりの部分で、酷似していて、明確に「テスト」を意識するかどうか、程度の違いだけだったため、うんうん、そうそう、と、抵抗なく読み進められました。ペアプロにも興味深々なのだけど、なかなか、踏み切れない・・・。
アカデミックで、ホットな情報、いつも感謝しています。
