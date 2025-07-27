---
layout: post
title: "Nendo 0.6.2 リリース"
date: 2012-02-10
categories: Nendo
---
*[Nendo*] 0.6.2をリリースしました。(リリースノート: *[Nendo.ReleaseNote*])
![img]({{ "/assets/images/rubygems_icon_128.png" | relative_url }})
## リリースの概要
gem単体でテストが走る rubygems-test への対応が中心です。
これまで、Nendoはgitリポジトリ上でしたテストが走りませんでした。
これからは、
```bash
$ gem install rubygems-test
$ gem test nendo
```
でテストが走ります。
 参考: [Gem Testers](http://test.rubygems.org:/)

以下リリースノートです。
## version 0.6.2
- Supported testable gem
   Please install rubygems-test and "gem test".
- Modified Rakefile to build the debian package.
   to invoke rspec with "ruby `which rspec` ..." instead of "rspec ..."
- Changed dependency rules of gemspec.

## 次の目標
*[Nendo*]については今のところ目標はありません。
使いながら足りないものから機能追加していきます。



---

**コメント by Lisa:**  
Yeah that's what I'm takling about baby--nice work!