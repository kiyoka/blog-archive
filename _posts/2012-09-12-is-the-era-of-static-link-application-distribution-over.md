---
layout: post
title: "static linkしたアプリケーション配布の時代は終わったのだろうか"
date: 2012-09-12
categories: Linux
---
LinuxにはたくさんのDistributionがある。
昔は配布するビルド済みバイナリを1種類にしたい場合はglibcをstatic linkしたバイナリを配布するのが一般的だったように思う。
２００５年くらいのMySQLはstaticバイナリを配布していて、rpm以外のディストリビューションの場合はそれを選べた。(Debianとか)
最近ではMySQLはrpmパッケージしか配布していない。

## JDK
JDKはどうかと調べてみたら、JDK-1.7.0_05にはtar.gz版バイナリも置いてあったので中身を調べてみた。

 *64bit版のJDK-7u7*
```javascript
 $ tar zxf jdk-7u7-linux-x64.tar.gz
 $ cd jdk1.7.0_07/bin
 $ ldd java
	linux-vdso.so.1 =>  (0x00007fff4cdff000)
	libpthread.so.0 => /lib/libpthread.so.0 (0x00007fd4cc205000)
	libjli.so => /home/kiyoka/Dropbox/temp/jdk1.7.0_07/bin/./../jre/lib/amd64/jli/libjli.so (0x00007fd4cbfee000)
	libdl.so.2 => /lib/libdl.so.2 (0x00007fd4cbdea000)
	libc.so.6 => /lib/libc.so.6 (0x00007fd4cba88000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fd4cc431000)
 $ ldd javac
	linux-vdso.so.1 =>  (0x00007fff7e3ff000)
	libpthread.so.0 => /lib/libpthread.so.0 (0x00007f413512c000)
	libjli.so => /home/kiyoka/Dropbox/temp/jdk1.7.0_07/bin/./../jre/lib/amd64/jli/libjli.so (0x00007f4134f15000)
	libdl.so.2 => /lib/libdl.so.2 (0x00007f4134d11000)
	libc.so.6 => /lib/libc.so.6 (0x00007f41349af000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f4135358000)
```

ネットの情報をあさってみたが、最近のglibcはもうstaticリンクできないようだ。
JDKもglibcのstaticリンクはあきらめているようだが、これで、どのDistributionでも動くのかなぁ。なんか不安だなあ。

## Rubyは？
さて、自分が作りたい全方位Distribution対応Rubyバイナリはどうすれば作れるか。
Debian squeeze(64bit環境)でオプション無しのconfigureで ruby-1.9.3-p194 をビルドすると次のようになる。
 (1) *./configure 版*
```javascript
 $ ldd ./ruby-1.9.3-p194/bin/ruby
	linux-vdso.so.1 =>  (0x00007fffc25ff000)
	libpthread.so.0 => /lib/libpthread.so.0 (0x00007fc720431000)
	librt.so.1 => /lib/librt.so.1 (0x00007fc720228000)
	libdl.so.2 => /lib/libdl.so.2 (0x00007fc720024000)
	libcrypt.so.1 => /lib/libcrypt.so.1 (0x00007fc71fded000)
	libm.so.6 => /lib/libm.so.6 (0x00007fc71fb6a000)
	libc.so.6 => /lib/libc.so.6 (0x00007fc71f808000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fc72065d000)
```

 (2) *./configure --with-static-linked-ext --disable-shared*
 かつ、ext/Setupを次のように変更したバージョン
これは、拡張ライブラリがruby本体にスタティックリンクされるオプションのようだが…

```javascript
 $ ldd ruby
	linux-vdso.so.1 =>  (0x00007fff554f3000)
	libpthread.so.0 => /lib/libpthread.so.0 (0x00007fdf7e270000)
	librt.so.1 => /lib/librt.so.1 (0x00007fdf7e067000)
	libdl.so.2 => /lib/libdl.so.2 (0x00007fdf7de63000)
	libcrypt.so.1 => /lib/libcrypt.so.1 (0x00007fdf7dc2c000)
	libm.so.6 => /lib/libm.so.6 (0x00007fdf7d9a9000)
	libc.so.6 => /lib/libc.so.6 (0x00007fdf7d647000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fdf7e49c000)
```

あれ？ 結局glibc部分はshared objectにリンクされるのはかわないのか…
というわけで、staticリンクはあきらめた。

## 解決策
要は、ユーザーのLinuxシステムがどのようなミニマム構成であっても自分のプログラムが動いてほしいということなのだ。opensslとかgdbmとかを使いたい。
実は、必要な *.so を自分でビルドしいっしょに配布すればよいのだった。
そして起動スクリプトで、LD_LIBRARY_PATHの先頭に、パスを追加すればよいだけだ。

うっかり深入りする前に気がついてよかった…
