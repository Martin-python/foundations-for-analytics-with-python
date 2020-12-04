###***md教程***
> <https://www.runoob.com/markdown/md-tutorial.html>

# Python数据分析基础

## 第1章 Python基础

### 1.3 与命令行交互的几项技巧

>####为什么要在打印时使用.format
>Python 并不要求每条print 语句都必须使用.format，但是.format 确实功能强大，可以
为你节省很多输入。在上面的示例中，注意`print("Output #3: {0}, {1}, {2}".format(a,
b, c)) `的最终结果是用逗号分隔的3 个变量。如果你想在不使用.format 的情况下得到
同样的结果，那么就应该这样写：`print("Output #3: ",a,", ",b,", ",c)`，但这是一段非
常容易出现输入错误的代码。后面还会介绍.format 的其他用法，但是从现在开始，你
就应该熟练掌握它的用法，以便在需要的时候加以使用。

### 1.4 Python语言基础要素

#### 1.数值
    * 整数 `{0:d}.format(x)`
    * 浮点数 `{0:.3f}.format(x)`
#### 2. 字符串
    * 字符串 `{0:s}.format(x)` 

>####type 函数
>Python 提供一个名为 `type` 的函数，你可以对所有对象调用这个函数，来获得关于Python 如何处理这个对象的更多信息。如果你对一个数值
变量调用这个函数，它会告诉你这个数值是整数还是浮点数，还会告诉你这个数值是否能当作字符串进行处理。函数的语法非常简单：
`type(varible)` 会返回 Python 中的数据类型。此外，因为Python 是一种“面向对象”的语言，所以你可以对 Python 中所有命名对象调用
type函数，不仅是变量，还有函数、语句等。如果你的代码出现了意外的错误，调用 type函数可以帮助你进行错误诊断。

>字符串多行可以用/或3引号表示，但使用/时必须保证/在每一行最末尾

>split 函数可以在括号中使用两个附加参数。第一个附加参数表示使用哪个字符进行拆分。第二个附加参数表示进行拆分的次数

>join 函数将一个参数放在 join 前面，表示使用这个字符（或字符串）在子字符串之间进行组合

>strip、lstrip 和 rstrip 函数从字符串两端删除不想要的字符。这 3 个函数都可以在括号中使用一个附加参数来设定要从字符串两端删除
的字符（或字符串）。

>replace 函数将字符串中的一个或一组字符替换为另一个或另一组字符。这个函数在括号中使用两个附加参数，
第一个参数是要在字符串中查找替换的字符或一组字符，第二个参数是要用来替换掉第一个参数的字符或一组字符：

>lower 和 upper 函数分别用来将字符串中的字母转换为小写和大写。capitalize 函数对字符串中的第一个字母应用upper 函数，
对其余的字母应用 lower 函数

#### 3.正则表达式与模式匹配

通过导入 re 模块，你可以使用一大波函数和元字符来创建和搜索任意复杂的模式。元字符（metacharacter）是正则表达式中具有特殊意义的字符。
每个元字符都有特殊意义，它们使正则表达式能够匹配特定的字符串。常用的元字符包括 |，()，[]，.，*，+，?，^，$ 和 (?P<name>)。
如果你在正则表达式中见到这些字符，要知道程序不是要搜索这些字符本身，而是要搜索它们描述的东西。

    # 计算字符串中模式出现的次数 
    string = "The quick brown fox jumps over the lazy dog." 
    string_list = string.split() 
    pattern = re.compile(r"The", re.I) 
    count = 0 
    for word in string_list: 
        if pattern.search(word):
        count += 1 
    print("Output #38: {0:d}".format(count))

>第一行将字符串变量 string 赋值为 The quick brown fox jumps over the lazy dog.。
>
>下一行将字符串拆分列表，列表中的每个元素都是一个单词。
>
>再下一行使用 re.compile 和 re.I 函数以及用 r 表示的原始字符串，创建一个名为 pattern的正则表达式。
>re.compile 函数将文本形式的模式编译成为编译后的正则表达式。正则表达式不是必须编译的，但是编译是个好习惯，
>
>因为这样可以显著地提高程序运行速度。 re.I 函数确保模式是不区分大小写的，能同时在字符串中匹配“The”和“the”。
>
>原始字符串标志 r 可以确保 Python 不处理字符串中的转义字符，比如 \、\t 或 \n。这样在进行模式匹配时，
>
>字符串中的转义字符和正则表达式中的元字符就不会有意外的冲突。在上面的例子中，字符串中没有转义字符，所以 r 不是必需的，
>
>但是在正则表达式中使用原始字符串标志是一个好习惯。接下来的一行代码创建了一个变量 count 来保存字符串中模式出现的次数，初始值设为 0。
>
>再下一行是个 for 循环语句，在列表变量 string_list 的各个元素之间进行迭代。它取出的第一个元素是“The”这个单词，
>
>取出的第二个元素是“quick”这个单词，以此类推，直到取出列表中所有的单词。
>
>接下来的一行使用 re.search 函数将列表中的每个单词与正则表达式进行比较。如果这个单词与正则表达式相匹配，函数就返回 True，
>
>否则就返回 None 或False。所以 if 语句的意义就是：如果单词与正则表达式匹配，那么 count 的值就加 1。
>
>最后，print 语句打印出正则表达式在字符串中找到模式“The”（不区分大小写）的次数，在本例中，找到了两次。

    # 在字符串中每次找到模式时将其打印出来 
    string = "The quick brown fox jumps over the lazy dog." 
    string_list = string.split() 
    pattern = re.compile(r"(?P<match_word>The)", re.I)</match_word> 
    print("Output #39:") 
    for word in string_list: 
        if pattern.search(word):
            print("{:s}".format(pattern.search(word).group('match_word')

>第二个示例与第一个示例的区别在于，这个示例是想在屏幕上打印出每个匹配的字符串，而不是匹配的次数。要想得到匹配的字符串，将它们打印到屏幕上或存储在文件中，需要使用 (?P<name>) 元字符和 group 函数。这个示例中的多数代码和前一个示例中讨论过的代码是一样的，所以这里重点解释新的部分。
第一个新代码片段是 (?P<name>)，这是一个出现在 re.compile 函数中的元字符。这个元字符使匹配的字符串可以在后面的程序中通过组名符号 <name> 来引用。在这个示例中，这个组被称为 <match_word>。
最后一个新代码片段出现在 if 语句中。这个代码片段的意义是：“如果结果为 True（也就是说，如果单词与模式匹配），那么就在 search 函数返回的数据结构中找出 match_word 组中的值，并把这些值打印在屏幕上。”

    # 使用字母“a”替换字符串中的单词“the” 
    string = "The quick brown fox jumps over the lazy dog." 
    string_to_find = r"The" 
    pattern = re.compile(string_to_find, re.I) 
    print("Output #40: {:s}".format(pattern.sub("a", string)

#### 4. 日期

    from datetime import date, time, datetime, timedelta
    # 常用的对象和函数：today, year, month, day, timedelta, strftime, strptime
    # 通过使用 date.today()，你可以创建一个 date 对象，其中包含了年、月、日，但不包含时间元素，比如时、分、秒。
    # 相反，通过 datetime.today() 创建的对象则包含时间元素。
    # {0!s} 中的 !s 表示传入到 print 语句中的值应该格式化为字符串，尽管它是个数值型数据。

* 日期格式  
 ref fs line185
 
#### 5.列表

1. 创建列表  
 ref fs line203

2. 索引值   
 ref fs line217
 
3. 列表切片  
 ref fs line228    
 列表切片引用的是列表中从第一个索引值到第二个索引值的前一个元素    

4. 列表复制    
 ref fs line236
 
5. 列表连接    
 ref fs line240
 
6. 使用in 和 not in    
 ref fs line244

7. 追加、删除和弹出元素   
 ref fs line254

8. 列表反转     
 ref fs line267     

9. 列表排序     
 ref fs line275
 
10. sorted排序函数
 ref fs line284
    * lambda 函数
    * 表示使用索引位置为 3 的值（也就是列表中的第四个元素）对列表进行排序。
    * operator 标准模块，可以使用多个关键字对列表、元组和字典进行排序 line289
    * 先按照索引位置 3 中的值对列表进行排序，然后，在这个排序基础上，按照索引位置 0 中的值对列表进一步排序。

#### 6.元组
 * 不能被修改
 
1. 创建元组     
 ref fs line296

2. 元组解包     
 ref fs line304
 
3. 元组转换成为列表（及列表转换成为元组）      
 ref fs line314

#### 7.字典
1. 创建字典     
 ref fs line321

2. 引用字典中的值      
 ref fs line333

3. 复制       
 ref fs line337

4. 键、值和项目   
 ref fs line341

5. 使用in, not in和 get    
 ref fs line349     
 get(第二种测试具体键值的方式是使用 get 函数，这个函数也可以按照键值取得相应的字典值。和前一种测试键值的方式不同，如果字典中存在这个键，
 get 函数就返回键值对应的字典值；如果字典中不存在这个键，则返回 None。此外，get 函数还可以使用第二个参数，表示如果字典中不存在键值时函数的返回值。
 通过这种方式，如果字典中不存在该键值，可以返回除 None 之外的一些其他内容。)

6. 排序   
 ref fs line363

#### 8.控制流
1. if-else  
 ref fs line379

2. if-elif-else     
 ref fs line386

3. for循环    
 ref fs line394

4. 简化for循环：列表、集合与字典生成式      
 列表生成式      
 ref fs line418     
 集合生成式      
 ref fs line423     
 字典生成式      
 ref fs line430
 
5. while循环      

6. 函数   

7. 异常   

8. try-except   
 ref fs line456

9. try-except-else-finally  
 ref fs line468

###1.5 读取文本文件

1. 创建文本文件   
 ref fs line479

2. 脚本和输入文件在同一位置

3. 读取文件的新型语法

###1.6 使用glob读取多个文本文件

    print("Output #143:")
    # READ MULTIPLE FILES
    # Read multiple text files
    inputPath = sys.argv[1]
    for input_file in glob.glob(os.path.join(inputPath,'*.txt')):
        with open(input_file, 'r', newline='') as filereader:
            for row in filereader:
               print("{}".format(row.strip()))
    # key word: glob.glob(os.path.join(inputPath, '*.txt'))

###1.7 写入文本文件

1. 向first_script.py添加代码

2. 写入CSV文件

###1.8 print语句


