# Pythonについて
  
2,3,5はPython独自の書き方を中点に

1. Pythonの環境構築
    - python3のインストール
    - pip3のインストール
    - VS CodeのPython拡張機能

2. 資料型
    - 数字型
    - 文字型
    - Boolean
    - List
    - Tuple
    - Dictionary
    - Set

3. 制御文
    - インデント
    - if文
    - 比較演算子
    - in
    - while
    - for文

4. 例外処理

5. Object
    - 関数
    - Class
    - Module
    - Pacakge

6. 練習問題

7. 拡張機能
    - lambda
    - ファイル入出力
    - AWS Boto3 upload&download

8. FrameWorkについて

---

## Pythonの環境構築

*Python3 インストール*  
Pythonは Python2とPython3の二つのバージョンがありあます。Python2の弱みを直すためにPython3は内部を変更して両方のコードとライブラリーが互換できません。Python2は現在バグ修正のみアップデートされていますし2020年支援が終了される予定なので、Python3を使う事がお勧めです。
現在(2018/09/11)の最新バージョンはPython3.7.0です。

1.Windows  
<https://www.python.org/downloads/windows/>  
インストール確認 : `$ python --version`

2.Mac
MacにはPython2が基本設置されています。  
<https://www.python.org/downloads/mac-osx/>  
インストール確認 : `$ python3 --version`

*pip3 インストール*  
pipはpythonモジュールやパッケージを手やすくインストールするツールです。Python3をインストールしたら一緒にインストールされますが、Python2や問題が発生した時は手動でインストールします。

1. <https://bootstrap.pypa.io/get-pip.py>からget-pip.pyをダウンロード
2. `$ pyhton get-pip.py`または `$ python3 get-pip.py`
3. `$ pip --version`または`$ pip3 --version`でインストール確認

*開発ツールについて*  
IDE : PyCharm, Eclipse(PyDev plug-in), QPython(Android)  
Text Editor : Sublime Text, Atom, Notepad++, VS code 他

*VS Codeで使うPython関連Plugーin*  
Python - Linting, Debugging  
Django template - Django template language support  

---

## 資料型

### 数字型  

Pythonは変数の宣言の時に資料型の宣言をしない

```python
>>> a = 1 # int
>>> b = 1.5 # float
```

Python3では定数/定数の演算の時、結果が実数なら実数に自動型変換になる。

```python
>>> a = 6
>>> b = 4
>>> a/b
1.5
```

(+, -, *, /, %)演算子は他の言語と同じですが、

```python
>>> 3**4
81 # 3^4の演算
>>> 9//4
2 # 割算の商
```

8進数と16進数の書き方

```python
a = 0o177 # 8進数は頭に0+o(数字0+英字o)をつける
b = 0x8ff # 16進数は頭に0xをつける
```

---

### 文字型

他の言語と同じく’’や””で使います。
改行があるテキストなら''' '''や""" """"を使えばエスケープ文字を入れなくても改行がある文字列に認識される

```python
>>> multilne = """
    multi
    line
    """
>>> print(multine)
    multi
    line
```

文字列には'+'と'*'の演算子が使用可能です。

```python
>>> head = "Life"
>>> tail = " is too short"
>>> print(head + tail)
Life is too short
>>>
>>> a = "Python"
>>> print(a*2)
PythonPython
```

[参考] : 数字型と文字型の'+'演算はエラーになります。合わせるとが必要な場合`str()`関数や`format()`関数を使います。

文字列は他の言語の配列みたいにIndexingができます。

```python
>>> a = "Life is too short, You need Python"
>>> a[0]
'L'
>>> a[3]
'e'
>>> a[-1]
'n'
>>> a[-4]
't'
>>> a[-0]
'L'
```

[ ]の中の数字が負数なら後ろから数えます。ただし[-0]は[0]と同じく最初の文字を指定します。

':'を使って文字列を好きなだけSlicingすることもできます。

```python
>>> a = "Life is too short, You need Python"
>>> a[0:3]
'Life'
>>> a[4:8]
' is t'
>>> a[19:] # 後ろの数字を省略したら始まりの番ごから最後まで取る。
'You need Python'
>>> a[:17] # 始まりの番号を省略したら一番最初から終わりの番後まで取る。
'Life is too short'
>>> a[:] # 両方省略したら、文字列の全部を取る。
'Life is too short, You need Python'
>>> a[19:-7] #Slicingでも負数を使う事ができる。
'You need'
```

[参考] : 文字列はその中身を変更できないタイプなので直接変更することはできません。

```python
>>> a = "text"
>>> a[0] = "a"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

文字列の中に変数を入れる時にC系の言語で使う%s,%dみたいなコードを使う事ができますが、format()関数を使うともっと便利です。

最近はformat()関数を使う方法がお勧めです。

```python
>>> "format %s" %"test"
'format test'
>>>"format %d" % 10
'format 10'
>>> "format {0}".format("test")
'format test'
>>> "format {0}".format(3)
'format 3'
>>> "format {0}, {1}".format("test", 3)
'format test, 3'
>>>
```

format()は単純に文字列の中に値を入れる事以外にも書式変換もできます。

参考サイト : <https://note.nkmk.me/python-format-zero-hex/>

---

Pythonにも他言語と同じ機能を持ってるビルトイン関数があり、文字列関連の関数中よく使うものを技術します。

`Count(str)`  
文字列の中に該当するものがいくつあるのか数える

```python
>>> a = "text"
>>> a.count("t")
2
```

`find(str)` `index(str)`  
該当するものが一番最初の位置を返還する。  
存在しない値を入力した場合findは-1、indexはエラーを返還する。

```python
>>> a = "It is indexing tst"
>>> a.find("i")
3
>>> a.find("z")
-1
>>> a.index("t")
1
>>> a.index("y")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
```

`join(str)`  
文字列を挿入します。

```python
>>> a= ", "
>>> a.join('abcd')
'a, b, c, d'
```

`lstrip()` `rstrip()` `strip()`  
空白を消す関数です。

```python
>>> a = "    trim    "
>>> a.lstrip() # 左の空白を消す
'trim    '
>>> a.rstrip() # 右の空白を消す
'    trim'
>>> a.strip() # 左右の空白を消す
'trim'
```

`replace(str1, str2)`  
文字列の入れ替えます。

```python
>>> a = "You need Python"
>>> a.replace("Python", "Java")
'You need Java'
```

`split(str)`
文字列をリストで割ります。()の中に何も入れなけらば空白を基準に割ります。

```python
>>> a = "You need Python"
>>> a.split()
['You', 'need', 'Python']
>>> b = "1, 2, 3, 4"
>>> b.split(", ")
['1', '2', '3', '4']
```

[参考] : 改行なしで`print()`使う方法  
`print()`の引数としてend=''を入れれば改行をしません。

```python
a = "test1"
b = "test2"
c = "test3"
print(a, end='')
print(b)
print(c)
```

```python
test1test2
test3
```

---

### Boolean

Pythonではブーリアン型として `True` `Flase` を使う。最初が大文字ので書く時気をつけてください。  
数字0または文字列、チュープル、リストなどが空いているとFalseになることは他の言語と同じです。  
しかし、他の言語のnullに対することはNoneと書きます。  
比較演算子の使い型は他の言語とほぼほぼ同じですが、一部気をつける部分があります。

`==` `!=`  
==と!=はequality testです。左右の値が同じかないかのみ判別します。

`is`, `not`  
isとnotはidentity testとしてreferenceを(Cならpointer)をする演算子です。

[参考] : Javaでは`==`がidentity testで `.equlas()`がequality testのでJavaを先に習得した方は間違えないように気をつけてください。

```python
>>> a = "You need Python"
>>> b = "You need Python"
>>> a==b
True
>>> a is b
False
```

notは一般的に条件文でFalseを否定してTrueを作ることに使えます。

```python
True
>>> not False
True
>>> not None
True
>>> not 0
True
```

[参考] : PythonではInterningとしてすでに生成されたオブジェクトを再使用する機能があります。これはintern()関数で指定することもできますが、メモリーの節約のためPythonで基本的に指定するInterningがあります。  

1. 文字列 : 20字未満の空白と特殊文字を含めない文字列
2. 定数 : -5から255までの定数

この二つの場合は同じpointerが割り当てされますので注意する必要があります。

```python
>>> a = "test"
>>> b = "test"
>>> a is b
True
>>> a = 255
>>> b = 255
>>> a is b
True
>>> a = 1024
>>> b = 1024
>>> a is b
False
```

---

### List

他の言語の配列みたいに多数のデータをリストとして便利に管理する事ができます。  
リストを作ろ時には[]で囲んで要素は,で区分します。  
リストの中にはリストを含めた全ての資料型を全部入る事ができます。

```python
a = [ ]
b = [1, 2, 3]
c = ["a", "b", "c"]
d = [1, "a", [1, 2]]
e = list() # 空いているリストを生成
```

リストもIndexingとSlicingができます

```python
>>> a = [1, 2, 3, 4, 5]
>>> a[1]
2
>>> a[0:2]
[1, 2]
```

リストにも`+`と`*`演算子が使用可能です。

```python
>>> a = [1, 2]
>>> b = [3, 4]
>>> a+b
[1, 2, 3, 4]
>>> a*2
[1, 2, 1, 2]
```

*リストの修正と削除*  
リストの中にある要素は修正と削除ができます。
IndexingとSlicingを使ってリストの要素の値を修正できます。

```python
>>> a = [1, 2, 3, 4, 5]
>>> a[0] = 2
>>> a
[2, 2, 3, 4, 5]
>>> a[1:2] = ["a", "b"]
>>> a
[2, 'a', 'b', 3, 4, 5]
```

[参考] : 上の例で`a[1:2]=["a", "b"]`と`a[1]=["a,"b"]`は完全に違う結果が出るので気をつけてください。

```python
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a[1] = ["a", "b"]
>>> b[1:2] = ["a", "b"]
>>> a
[1, ['a', 'b'], 3] # リストそのままa[1]に入る
>>> b
[1, 'a', 'b', 3]
```

リストの要素を削除する方法は下の二つとビルトイン関数を使う方法があります。ビルトイン関数については後で説明します。

```python
>>> a = [1, 2, 3, 4, 5]
>>> a[1:2] = []
>>> a
[1, 3, 4, 5]
>>> del a[1] # del関数
>>> a
[1, 4, 5]
```

[参考] : slicingじゃなく要素一個を指定して空きリストを入れたら空きリストそのまま元のリストに入りますので気をつけてください。

```python
>>> a[1] = []
>>> a
[1, [], 5]
```

---

リストでよく使うビルトイン関数について記述します。

`list(str)`
文字列を1字づつリストに入れる。

```python
>>> a = "abcd"
>>> list(a)
['a', 'b', 'c', 'd']
```

`append(obj)`  
リストに要素を追加する。

```python
>>> a = [1, 2]
>>> a.append(3)
>>> a
[1, 2, 3]
>>> a.append([4,5])
>>> a
[1, 2, 3, [4, 5]]
```

`insert(int, obj)`  
リストの中に要素を挿入する関数。

```python
>>> a = [1, 2, 3]
>>> a.insert(1, 4)
>>> a
[1, 4, 2, 3]
```

`remove(obj)`
リストで最初に出るobjを削除する関数。

```python
>>> a = [1, 2, 1, 2]
>>> a.remove(2)
>>> a
[1, 1, 2]
```

`pop(int)`  
リストでint番めの要素をリターンした後、その要素を削除する。
引数を入れないと一番最後の要素をリターンして削除する。

```python
>>> a = [1, 2, 3, 4]
>>> a.pop(2)
3
>>> a
[1, 2, 4]
>>> a.pop()
4
>>> a
[1, 2]
```

`sort()` `reverse()`  
sort()->上昇  
sort(reverse=True) -> 下降  
reverse() -> リストを逆にする(下降じゃない)  

```python
>>> a = [4, 9, 6, 3, 7]
>>> a.sort()
>>> a
[3, 4, 6, 7, 9]
>>> a = [4, 9, 6, 3, 7]
>>> a.sort(reverse=True)
>>> a
[9, 7, 6, 4, 3]
>>> a = [4, 9, 6, 3, 7]
>>> a.reverse()
>>> a
[7, 3, 6, 9, 4]
```

[参考] : keyオプションで整列の方を調整できます。

```python
>>> a = ["Life", "is", "too", "short"]
>>> a.sort(key=len) # 文字列の長さの上昇
>>> a
['is', 'too', 'Life', 'short']
```

---

### Tuple

チュープルはほぼほぼリストと同じですが要素の値を変更できない事が違います。  
宣言は`(obj, obj)`でします。

```python
>>> a = (1, 2)
>>> a
(1, 2)
>>> a = 1, 2, 3 # ()がなくてもチュープルが生成されます。
>>> a
(1, 2, 3)
>>> a[0] = 3 # 変更ができません。
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

[参考] : 要素がひとつならチュープルは生成されません。しかし迂回する方法があります。

```python
>>> a = (1)
>>> a
1
>>> a = (1,) # ,の後ろに何も書けないとチュープルになります。
>>> a
(1,)
>>> len(a) # このチュープルのサイズを調べます。
1
```

---

### Dictionary

ディクショナリーはAssociatve arrayまたはHashと呼ばれるKeyとValueの組み合わせでなり立てる資料型です。JAVAならMapに対します。  
ディクショナリーの要素は順番がないのでfor文などに回した時、同じ手順を保証できないです。
ディクショナリーは基本的にこういう形です。

```python
{Key1:Value1, Key2:Value2, ・・・}
```

基本的な宣言と追加削除方法はこうなります。

```python
>>> dic = {"Baseball" : 9, "Football" : 11} # 宣言
>>> dic
{'Baseball': 9, 'Football': 11} # 追加
>>> dic["Basketball"] = 5
>>> dic
{'Baseball': 9, 'Football': 11, 'Basketball': 5}
>>> del dic["Basketball"] # 削除
>>> dic
{'Baseball': 9, 'Football': 11}
```

ディクショナリーの修正は二つの方法があります。  
一個の修正は直接指定します。

```python
>>> sports = {'Baseball': 9, 'Football': 11, 'Basketball': 5}
>>> sports['Baseball'] = 10 #
>>> sports
{'Baseball': 10, 'Football': 11, 'Basketball': 5}
```

二つ以上の要素を変更する時はupdate()関数を使います。  
もしKeyが既にいないKeyを設定したら、追加します。

```python
>>> sports.update({'Baseball':9, 'Handball':7})
>>> sports
{'Baseball': 9, 'Football': 11, 'Basketball': 5, 'Handball': 7}
```

値を得る方法はこうなります。

```python
>>> sports = {'Baseball': 9, 'Football': 11, 'Basketball': 5}
>>> sports["Football"]
11
>>> sports.get("Football")
11
```

二つの方法の違いはディクショナリーにいないKeyを入力した時のリターンです。

```python
>>> sports["Volleyball"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Volleyball'

>>> sports.get("Volleyball")
```

dic[Key]はエラーになりますが`get(Key)`はエラーがなりません。タイプを調べると

```python
>>> sports.get("Volleyball")
>>> type(sports.get("Volleyball"))
<class 'NoneType'>
```

Noneがリターンされた事が確認できます。  

`get(Key, Default)`の形て該当するKeyがいなければディフォルトの値をリターンすることもできます。

```python
>>> sports.get('Volleyball', 'No entry')
'No entry'
```

---
KeysとValuesそれとも両方をリストで管理するオブジェクトがあります。

```python
>>> sports.keys()
dict_keys(['Baseball', 'Football', 'Basketball'])
>>> sports.values()
dict_values([9, 11, 5])
>>> sports.items()
dict_items([('Baseball', 9), ('Football', 11), ('Basketball', 5)])
>>> for k in sports.keys(): # リストで使える。
...     print(k)
...
Baseball
Football
Basketball
```

しかし、このdict_XXX オブジェクトはリストのように使えることはできるけどリストのビルトイン関数(append, pop, sortなど)が使えません。

```python
>>> a = sports.keys()
>>> a.pop(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict_keys' object has no attribute 'pop'
```

リストのビルトイン関数を使いたいなら`list()`を使います。

```python
>>> a = list(sports.items())
>>> a.pop(1)
('Football', 11)
>>> a # pop()関数がちゃんと動ける事が確認。
[('Baseball', 9), ('Basketball', 5)]
```

該当するKeyがあるかどうか検索することは`in`を使って可能です。

```python
>>> sports = {'Baseball': 9, 'Football': 11, 'Basketball': 5}
>>> 'Baseball' in sports
True
>>> 'Volleyball' in sports
False
```

[参考] : Keyはimmuatableなオブジェクトのみ使えます。mutableなオブジェクトを指定したらエラーになります。

```python
>>> a = {(1,2) : 1} # tupleはimmutable
>>> a
{(1, 2): 1}
>>> a = {[1,2] : 1 } # listはmutable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

[参考] : 手順が固定されたディクショナリーが必要な場合にはOrderedDictライブラリーを使います。

```python
from collections import OrderedDict

colours = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
for key, value in colours.items():
    print(key, value)
```

```bash
Red 198
Green 170
Blue 160
```

入力手順が維持されます。

---

### Set

集合型は数学の集合のような資料型です。ディクショナリーと似ていますけどKeyがないです。集合型の要素は順番がなくUniqueな値になります。  

```python
>>> s = {1,3,5}
>>> s
{1, 3, 5}
>>> type(s)
<class 'set'>
```

set()の括弧の中に文字列を入れて作ることもできます。  

```python
>>> s = set("Hello")
>>> s
{'l', 'e', 'H', 'o'} # 順番がない、重複は自動的に除外
```

追加、更新、削除もディクショナリーなりとほぼ同じです。

```python
>>> s = {1, 3, 5}
>>> s.add(2) # 一個追加
>>> s
{1, 2, 3, 5}
>>> s.update([4,5,6]) # 多数追加
>>> s
{1, 2, 3, 4, 5, 6}
>>> s.remove(3) # 削除
>>> s
{1, 2, 4, 5, 6}
```

Pythonでは集合演算に対する機能も提供してます。

`|`, `union(set)`  
合集合

```python
>>> s1 = {1, 3, 5}
>>> s2 = {1, 2, 4}
>>> s1|s2
{1, 2, 3, 4, 5}
>>> s1.union(s2)
{1, 2, 3, 4, 5}
```

`&`, `intersection(set)`  
交集合

```python
...
>>> s1 & s2
{1}
>>> s1.intersection(s2)
{1}
```

`-`, `difference(set)`  
差集合

```python
...
>>> s1-s2
{3, 5}
>>> s1.difference(s2)
{3, 5}
>>> s2-s1
{2, 4}
>>> s2.difference(s1)
{2, 4}
```

`^`  
対称差集合(合集合-交集合)

```python
>>> s1^s2
{2, 3, 4, 5}
```

[参考] : この演算子たちは`|=`,`&=`,`-=`,`^=`の形で演算と同時に割当することもできます。この時pointerは同じです。

```python
>>> s1 = {1,2,3}
>>> s2 = {2,3,4}
>>> id(s1)
4547172616
>>> s1|=s2
>>> s1
{1, 2, 3, 4}
>>> id(s1)
4547172616
```

これらの集合の基本演算以外にも多数の集合に関する関数が用意されましたけど、集合の演算以外にはあんまり使わないものですので必要な時にドキュメントを探してください。

---

## 制御文

### インデント

Pythonには { }が無く他の言語で { }を使うところをインデント(正確にはSpace4回)で処理します。  

```python
a = 3
if a > 1:
    print("a is greater than 1") # if文の中身はSpace 4回でインデントつけて書く
b = 4 # if文の外ではインデントつけない
...
```

インデントが必要なところでインデントがなければエラーになります。

[参考] : インデントは`Tab`じゃなく`space4回` がおすすめされています。その理由は一部のエディターでは`Tab`が`space2回`もしくは`ひとつのTab`の場合があるらしいです。  
しかし、VSCode及び多数のテキストエディターではPythonに関する設定をしたら`Tab`を押した時、自動的に`space4回`に変更して入力してる機能がありますのでこういう機能を使ったら問題ないです。

---

### if文

if文の基本的な書き方はこうなります。

```python
...
if 条件文:
    実行文
elif:
    実行文
else:
    実行文
...
```

elifは他の言語の`else if`に対します。  
条件文は括弧で囲まなく書くことと`:`を書いた後、改行してインデントを入れます。  
もし条件分岐のなかにまたifが入るならこうなります。

```python
if 条件文:
    実行文
    if 条件文:
        実行文
else:
    実行文
```

---

### 比較演算子

基本的には他言語で使う比較演算子と同じように使います。`True`,`False`,`is`,`not`についてはBooleanの項目に既に技術しています。

`and`, `or`
条件を判断する時、他の言語で使う&, &&, |, || じゃなく`and`, `or`を使って条件文を作成します。

[参考] : Pythonでは`|`が`or`ではないので注意してください。

```python
a = 2
b = 1
if a>1 | b>1:
    print(True)
else:
    print(False)
```

```bash
False
```

```python
if a>1 or b>1:
    print(True)
else:
    print(False)
```

```bash
True
```

---

### in

Pythonでは`in`と言う特別な条件文を提供します。文字そのままの意味で`in`の後ろに来るリスト、チュープル、文字列のなかに`in`の前に書いたオブジェクトがあるのか判定します。`not`を使って否定することもできます。

```python
>>> 1 in [1,2,3]
True
>>> 4 in [1,2,3]
False
>>> "t" in "test"
True
>>> "t" not in "test"
False
```

---

### while

while文は他の言語とほぼ同じです。書き方はこうなります。

```python
while 条件文:
    実行文
```

下の文章をスキップしてループを回す`conitnue`とループを強制中止する`break`ももちろん使えます。

---

### for文

他の言語ではfor, foreach, for ofなど色んな方法のfor文を提供しますが、Pythonでは`for in`のひとつの形しか提供しません。  
しかし`in`の前と後ろに描き方がいくつかあります。

`range`  
一般的なfor文に対することはrangeを使う方法です。  
rangeは`range(start, end, step)`の形になっています。  
startから初めてendに辿るとループが中止します。  
stepは省略が可能でその場合は1づつ増えることになります。

```java
# Java 0から9まで出力
for(int i=0; i<10; i++){
    System.out.println(i);
}
```

```python
#Python 0から9まで出力
for i in range(0,10):
    print(i)
```

`for items in iterable`  
iterableは文字そのまま反復可能なオブジェクトを言います。一般的にはリスト、文字列、ディクショナリーをよく使います。  
他の言語のforeach文とよく似ています。

```python
test = [1,3,5]
for items in test:
    print(items)
```

```bash
1
3
5
```

```python
for items in "test":
    print(items)
```

```bash
t
e
s
t
```

[参考] : ディクショナリーはただ使ったらKeyのみ割当される。Valueまたは両方を割当するようには書き方がちょっと違います。

```python
dic = {'a':10, 'b':20, 'c':30}
for key in dic:
    print(key)
```

```bash
a
b
c
```

```python
for val in dic.values(): #Valueを割当するにはvalues()使う
    print(val)
```

```bash
10
20
30
```

```python
for key, val in dic.items(): #items()でKeyとValue両方を割当
    print("key={0}, value={1}".format(key,val))
```

```bash
key=a, value=10
key=b, value=20
key=c, value=30
```

この例題では順番通り出てましたけど、本来ディクショナリーは順番が無いオブジェクトですから、実行し順番がズレることがあります。

`enumerate`  
時々これが何回目のループか確認が必要な時かあります。enumerateはこんな時index番号を提供してくれます。  
`enumarte(sequence, start=0)`の形でかいて`start=0`は省略が可能な基本値です。もし0じゃなく他の番号から採番が必要な場合いれば良いです。
enumarteは`(index, value)`のチュープるでリターンします。

```python
text = "Python"
for val in enumerate(text):
    print(val)
```

```bash
(0, 'P')
(1, 'y')
(2, 't')
(3, 'h')
(4, 'o')
(5, 'n')
```

しかし、チュープるじゃ無い形でindex番号とvalueを別々にもらいたい時があります。  
その時には`for`の後ろに変数を二つ書ければ一番目にはindex、二番目にはvalueが割当されます。

```python
test = ['a','b','c','d']
for i, val in enumerate(test):
    print("{0}番目の要素は{1}です。".format(i,val))
```

```bash
0番目の要素はaです。
1番目の要素はbです。
2番目の要素はcです。
3番目の要素はdです。
```

[参考] : リストの`i`番目と`i+1`番目を両方使う時、PythonではJavaとかでよく使う`arr.length`みたいな範囲設定はしない方がおすすめされています。

例えです。

```java
for(int = i; i<s_arr.length; i++ ){
    if(s_arr[i] > s_arr[i+1]){
        ...
    }
}
```

みたいなコードを入れる時、

```python
# おすすめされない
for i in range(len(s_list)):
    if s_list[i] > s_list[i+1]:
        ...

# おすすめ
for i, _ in enumerate(s_list):
    if s_list[i] > s_list[i+1]

```

下のようにリストの値を直接使わない場合には`_`とかの変数で指定して`enumerate()`の順番変数を使ってコードを作成します。  
ただし、リストの範囲を超える値に対した対応が必要です。

---

## 例外処理

基本的な書き方としてはこうなります。

```python
try:
    ...
except 発生エラー as エラーメッセージ変数: # エラーメッセージ変数は省略可能
    実行文
else:
    例外が発生しなかった場合実行文
finally:
    例外の有無に関わらず実行する文
```

elseを使用する時には必ずexceptの次に来るべきです。exceptを多数書くことも可能ですが、エラーが発生した場合一番最初に掛ったエラーしか発生しません。  
例えはこうなります。

```python
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
finally:
    print("End")
```

```bash
list index out of range
End
```

この場合はIndexErrorが先に発生したのでZeroDvisionErrorは見えません。

`Pass`

特定なエラーが発生しても無視する時に使います。

```python
try:
    4/0
except ZeroDivisionError:
    pass
finally:
    print("End")
```

```bash
End
```

`Raise`

逆にエラーをわざと起こせる必要がある場合もあります。

```python
>>> raise Exception()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
Exception
```

自分がエラーを作る場合の例題です。

```python
class testError(Exception):
    def __init__(self):
        super().__init__("Error MSG")

try:
    raise testError()
except testError as e:
    print(e)
>>> # 実行
Error MSG
```

[参考] : Pythonエラーの種類ドキュメント
<https://docs.python.jp/3/library/exceptions.html#ValueError>

---

## Object

### 関数

Pythonで関数はこの形になります。

```python
def 関数名(引数):
    実行文
    ...
    return 戻り値
```

引数の数が確定じゃ無い場合の時は引数の前に`*`を入れます。

```python
def sum_many(*args):
    result = 0
    for i in args:
        result+=i
    return result

result = sum_many(1,2,3)
print(result)
result = sum_many(1,2,3,4)
print(result)
```

```bash
6
10
```

argsはargumentsの略で慣例的に使う変数名です。  
`*引数`の引数を使うとき他の引数も普通に使用できます。

```python
def cal(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result+=i
    elif choice == "mul":
        result = 1
        for i in args:
            result*=i
    return result

result = cal("sum", 2,3,4)
print(result)
result = cal("mul", 2,3,4)
print(result)
```

```bash
9
24
```

`*引数`を使う時には必ず一番後ろの引数として使わなければなりません。そうしないとエラーになります。

`**kwargs`
kwargsはkeyword argumentsの略で`key=value`形の引数をもらってディクショナリーに保存する時に使います。

[参考] : 初期値が必要な場合には引数で設定が可能です。

```python
def test(name="John Smith", age=20):
    print("{0}/{1}".format(name, age))

test("Orpheus",10)
test()
```

```bash
Orpheus/10
John Smith/20
```

---

### Class

#### 構造

pythonのクラスの基本的な姿はこうなります。

```python
class ClassName:

    def method_name(self, first, second):
        ...
        return
    ...
```

一般的にPyhtonではsnake_caseで変数名を作成しますが
ClassはCamelCaseで作成するのが一般的です。

Pythonではクラスの中にはあるインスタンスメソッドの一番目の引数は必ず`self`を書きます。その理由はPythonの構造にありますので詳しく説明するのは深くて簡単に要点だけ書けば、オブジェクトを呼び出した時そのオブジェクト自身が伝達されると考えると楽です。

---

#### Constructer

コンストラクタがが必要な場合は`__init__()`を使います。

```python
class TestClass:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

a = TestClass(2,3)
print(a.first)
a.first = 4
print(a.first)
```

```bash
2
4
```

[参考] : メソッドの中で自分の引数、またはクラスの中の他のメソッドを使う時は必ず`self.~`をつけます。つけないとクラスの外の対象を使う宣言になります。

---

#### Inheritance

継承は次のように書きます。

```python
class SonClass(ParentsClass):
    ...
```

親クラスのすべての機能を使えるし、メソッドオバーライディングで書き換えることもできます。

[参考] : Pythonは基本的にアクセス修飾子が無いです。全部publicの状態です。それともメソッドのオバーロードも無いです。同じメソッド名を引数を変えても一番下にあるメソッドだけ維持します。

---  

#### クラス属性

コンストラクタで作った変数はインスタンス化されてますけど、場合によってはみんなが一緒に使う変数も必要です。

次の例文を見ますと

```python
class Person:
    def __init__(self):
        self.token = 0

    def put_token(self, token):
        self.token = token

    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person()
james.put_token(50)
james.put_bag('book')

maria = Person()
maria.put_token(100)
maria.put_bag('key')

print("{0}cent and {1} in bag".format(james.token, james.bag))
print("{0}cent and {1} in bag".format(maria.token, maria.bag))
```

```bash
50cent and ['book', 'key'] in bag
100cent and ['book', 'key'] in bag
```

tokenの部分は`__init__`によりインスタンス化されて二つのオブジェクトに違う値が割り当てされていますが、bagはただクラスのなかで宣言した変数なので二つのオブジェクトが一緒に同じリストを使っています。

[参考] : クラスの中でしか使えない変数は慣例的に名前の一番先に`_`をつけます。  
また、他の言語のように外から接近を止める(privateような)変数は名前の一番先に`__`をつけます

```python
class Test:

    def __init__(self):
        self.__name = "John"

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

a = Test()
print(a.get_name())
a.set_name("Maria")
print(a.get_name())
a.__name = "Jack"
print(a.get_name())
```

```bash
John
Maria
Maria # a.__name = "Jack"は無視されている
```

---

#### static method

インスタンスを通じではなくクラスから直接呼び出しできるメソッドです。この場合には引数として`self`を指定しないです。

```python
class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)

    @staticmethod
    def mul(a,b):
        print(a*b)

Calc.add(10,20)
Calc.mul(10,20)
```

```bash
30
200
```

メソッドの上に`@staticmethod`のアノテーションを付けたら、そのメソッドはstaticメソッドになります。

---

#### class method

クラスメソッドはインスタンスなくて使うのは同じですけどメソッドのなかでクラスの変数とか他のクラスメソッドに接近する時ち使います。

一番べの引数として`cls`を使って`@classmethod`アノテーションを付けます。

```python
class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def print_count(cls):
        print('{0} person in here.'.format(cls.count))  

james = Person()
maria = Person()

Person.print_count()  
```

```txt
2 person in here.
```

[参考] : static method vs class method

```python
class Language:
    default_language = "English"

    def __init__(self):
        self.show = self.default_language

    @classmethod
    def class_my_language(cls):
        return cls()

    @staticmethod
    def static_my_language():
        return Language()

    def print_language(self):
        print(self.show)


class JapanessLanguage(Language):
    default_language = "日本語"

a = JapanessLanguage.static_my_language()
b = JapanessLanguage.class_my_language()
a.print_language()
b.print_language()
```

```bash
English
日本語
```

両方の違いは継承で明らかに出てます。static methodはクラス属性を持たせるのでEnglishをリターンしましたが、class methodはclsを使って現在クラスのクラス属性を待たせて日本語をリターンます。

---

#### Abstract Class

抽象クラスの形はこうなります。

```python
from abc import *
class AbstractClassName(metaclass=ABCMeta):
     @abstractmethod
        def abstract_method(self):
            pass
```

必ず`abc`モジュールをインポートしなければなりません。  
クラスの括弧に`metaclass=ABCMeta`を入れてメソッドの上に`@abstractmethod`を付けます。

以外他の抽象クラスに対した基本的な規則は他の言語と同じです。

---

### Module

Pythonではモジュールは関数や変数またはクラスなどが入っているPythonファイルを指します。

```python
import modulename
from modulename import def1, def2
```

一番目の方法は該当するファイルの全てをインポートします。  
二つ目の方法は一部の機能のみインポートします。`,`で区分して多数の機能を１行で呼べます。`*`を使ったらファイルの全てをインポートします。

---

### Package

パッケージは`.`を使ってモジュールをディレクトリ構造で管理することです。

例えば

```bash
game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
```

```python
# echo.py
def echo_test():
    print ("echo")
```

このような構造になっていると仮定したら、

```python
>>> import game.sound.echo
>>> game.sound.echo.echo_test()
echo
```

```python
>>> from game.sound import echo
>>> echo.echo_test()
echo
```

```python
>>> from game.sound.echo import echo_test
>>> echo_test()
echo
```

この三つの方法で`game.sound.echo.echotest()`を使えます。

[参考] : `__init__.py`について  

`__init__.py`は該当ディレクトリがパッケージの一部だと知らせる役割をしています。python3.3からは`__init__.py`がなくてもちゃんと認識しますが、レガシー支援のために生成するのが一般的です。

基本的には空きファイルですが、たまにパッケージの初期化コードとか`__all__`変数でインポートの時モジュールを持たせる範囲を決めるコードが入れる場合があります。

---

## 演習問題

```txt
n個の定数を持っている配列がある。この配列は正の定数と負の定数を両方持っている。あなたはこの配列を次に規則によって整列する。
1. 負の定数は正の定数より先の来る。
2. 負の定数の中と正の定数中のそれぞれの順番は変更しない。
ex) -1 1 3 -2 2
ans: -1 -2 1 3 2

(Googleの電話面接問題)
```

```txt
あなたは新しいダーツゲームの点数計算のロジックを組みます。

1. ダーツは3回投げる。
2. 各機会に得る点数は0から10の間である。
3. 点数と共にSingle(S), Double(D), Triple(T)がの領域が存在し、各領域に当たる場合点数で1乗、2乗、3乗する。
4. オプションで*と#があり、*が当る場合は該当する点数とすぐ前の点数を2倍にする。#が当る場合には該当点数がマイナスになる。
5. *が一番最初に当たった場合には該当する点数のみ2倍にする。
6. *の効果がかぶる場合は4倍になる。
7. *と#がかぶる場合にはマイナス2倍になる。
8. Single(S), Double(D), Triple(T)はひとつづつ、必ず存在する。
9. *と#は点数づつ、どっちかとひとつのみ存在し、存在しないすることもできる。

入力形式
点数｜ボーナス｜オプション　の文字列

出力形式
該当する定数値

例
ex  dartResult  answer  説明
1   1S2D*3T     37      1^1 * 2 + 2^2 * 2 + 3^3
2   1D2S#10S    9       1^2 + 2^1 * (-1) + 10^1
3   1D2S0T      3       1^2 + 2^1 + 0^3
4   1S*2T*3S    23      1^1 * 2 * 2 + 2^3 * 2 + 3^1
5   1D#2S*3S    5       1^2 * (-1) * 2 + 2^1 * 2 + 3^1
6   1T2D3D#     -4      1^3 + 2^2 + 3^2 * (-1)
7   1D2S3T*     59      1^2 + 2^1 * 2 + 3^3 * 2

(Kakao Blind Test)
```

```txt
整列されているk個のリストがある。
k個のリストの中、せめてひとつの数字を含む区間の中一番間隔が狭い範囲をて探しなさい。
例
List 1: [4, 10, 15, 24, 26]
List 2: [0, 9, 12, 20]
List 3: [5, 18, 22, 30]
この例題では、一番範囲が狭い区間は[20,24]であるこの区間にはList1で24、List2で20、List3で22を含めている。
(Google 対人面接)
```

<https://www.careercup.com/question?id=16759664>

---

## 拡張昨日

### lambda

lambdaで匿名関数を作って式を簡単に書けます。

```python
lambda 引数 : 表現式
```

いくつかのラムダ式の例題です。

```python
>>> x = lambda a : a + 10
>>> print(x(5))
15
>>>x = lambda a, b : a * b
>>>print(x(5, 6))
30
```

```python
>>> my_list = [lambda a,b:a+b, lambda a,b:a*b]
>>> my_list[0](3,4)
7
>>> my_list[1](3,4)
12
>>> my_list
```

lambdaを活用する例

```python
li = [-2, -3, 5, 6]

# 正数をリターン
def ft(li):
    result = []
    for e in li:
        if e > 0:
            result.append(e)
        else:
            pass
    return result


# filterを使う
def positive(x):
  return x > 0

list(filter(positive, li))

# filter + lambda 使う
list(filter(lambda x: x > 0, li))
```

```python
from functools import reduce
reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
# = ((((1+2)+3)+4)+5)と同じ
reduce(lambda x, y: x*y, range(1, 6))
# = ((((((1*2)*3)*4)*5)*6)と同じ
```

---

### Comprehensions

ラムダ式と似てる方法でリスト、ディクショナリー、集合を作成する時、表現式がもっと分かりやすいし、処理速度も早いです。

```python
>>> a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
>>> [x for x in a if x > 5 and x < 10]
[8, 7, 9]
```

この表現式は慣れたら特に何かのリストから新しい結果をリストに入れることが楽になります。

---

### ファイル入出力

Pythonでコンソール上のファイルの読み込み、書き込みは`open()`とか`read()`または`write()`みたいな関数をそれぞれの役割に合わせて使います。  
[参考] : <https://note.nkmk.me/python-file-io-open-with/>

---

### AWS Boto3

`Uplaod`

```python
import boto3

bucketName = "Your S3 BucketName"
Key = "Original Name and type of the file you want to upload into s3"
outPutname = "Output file name(The name you want to give to the file after we upload to s3)"

s3 = boto3.client('s3')
s3.upload_file(Key,bucketName,outPutname)

```

`Download`

```python
import boto3
import botocore

Bucket = "Your S3 BucketName"
Key = "Name of the file in S3 that you want to download"
outPutName = "Output file name(The name you want to save after we download from s3)"

s3 = boto3.resource('s3')
try:
    s3.Bucket(Bucket).download_file(Key, outPutName)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
```

---

## Frameworkについて

Pythonのウェブ制作を助けるFWはflaskとDjango二つがあります。  
DjangoはFull-stack FWでFlaskはMicro-FWなので、プロジェクトに合わせて必要な、ツールを使ってください。

---

## Author

MW_尹 (s.yoon@micro-wave.net)