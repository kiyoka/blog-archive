---
layout: post
title: "そろそろオレ言語でもやっておくか(11)"
date: 2009-04-10
categories: 言語
---
このClojureのtutorialが非常に参考になる。本家のドキュメントではないけどたいへん分かりやすい。
 [Clojure Tutorial For the Non-Lisp Programmer | Moxley Stratton](http://www.moxleystratton.com/article/clojure/for-non-lisp-programmers)
ClojureがJavaのClassライブラリをアクセスする構文を持っている。
対して、NendoはRubyのClassライブラリをアクセスする必要があるので、言語仕様を考える上でClojureの例は大変参考になる。

例えばこれは参考になる。
 Clojure provides the ability to interface with Java objects and
 primitives. Knowing how to do this is essential for non-trival
 programs.

 Let's start by instantiating a Java java.util.Date object:
```javascript
   user=> (new java.util.Date)
   Mon May 26 10:25:25 PDT 2008
```

 To pass arguments to the object's constructor, just include them in
 the call to new:
```javascript
   user=> (new StringBuffer "This is the initial value")
   This is the initial value
```
 To call an object's method use the dot (.) form:
```javascript
   user=> (. (new java.util.Date) (toString))
   "Mon May 26 11:12:15 PDT 2008"
```

 The dot form uses a dot character (.) as the operator. The second
 argument is the object whose method will be called. The

 third argument is a list containing the method name and the method's
 arguments, if any:
```javascript
   user=> (. (new java.util.HashMap) (containsKey "key"))
   false
```

 Static methods can be called in the same way:
```javascript
   user=> (. Boolean (valueOf "true"))
   true
```
