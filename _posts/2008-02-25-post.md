---
layout: post
title: "Schemerにとって理想のRubyとは(1)"
date: 2008-02-25
categories: Ruby
---
- Schemerはこんなコードを書きたいと思うはず。defとlambdaは同じであるべきだ。

```python
def func1( x )
  x + 1
end
p *1,2,3*.map( func1 )
```

- なんでdefは内部でlambdaに置換されないんだろうか。えっ？class/moduleとの整合？私はそんなの知らない。
ところで、Ruby1.8.6ではクロージャをmapに渡すためにはこう書くしかない。

```lisp
func1 = lambda {|x|
  x + 1
}
p *1,2,3*.map {|x|
  func1.call(x) 
}
```

-- せめてこれくらい書ければいいなぁ。

```lisp
func1 = lambda {|x|
  x + 1
}
p *1,2,3*.map( func1 )
```
 
-- でもエラーとな...残念だ。
```python
bash-3.2$ ruby ./t.rb
./t.rb:5:in `map': wrong number of arguments (1 for 0) (ArgumentError)
	from ./t.rb:5
```

私が知らないだけで本当はもっと簡潔に書く方法があるのかな？
