# javascript 정규표현식

# exec 

```js
var myRe = new RegExp("d(b+)d", "g");
var myArray = myRe.exec("cdbbdbsbz");
```

# 정규식에서 쓰이는 메소드


| Method  | Description |
|:-------:|:------------|
| exec	  | 일치하는 문자열을 찾는 RegExp 메소드입니다. 정보를 가지고 있는 배열을 반환합니다. |
| test	  | 일치하는 문자열을 검사하는 RegExp 메소드 입니다. true 나 false를 반환합니다. |
| match	  | 일치하는 문자열을 찾는 String 메소드입니다. 정보를 가지고 있는 배열을 반환하거나 일치하지 않는 부분을 null로 반환합니다. |
| search  | 일치하는 문자열을 검사하는 String 메소드입니다. 일치하는 인덱스를 반환하거나 검색에 실패할 시 -1을 반환합니다. |
| replace | 일치하는 문자열을 찾는 String 메소드입니다. 일치하는 문자열을 replacement 로 대체합니다. |
| split	  | 정규표현식 or 고정된 문자열로 대상 문자열을 나누어 배열로 반환하는 String 메서드입니다. |


# Regular expression flags
| Flag | Description |
|:----:|:------------|
|  g   | Global search. |
|  i   | 대소문자 미구별 검색 |
|  m   | 다중행(multi-line) 검색 |
|  y   | Perform a "sticky" search that matches starting at the current position in the target string. |

`exec`는 문자열이 일치하면 이후의 문자열은 검색하지 않는다.


# 정규식 실행결과


| Object | Property or index | Description	In this example                                        |
|:------:|:-----------------:|:--------------------------------------------------------------------|
| myArray|                   | 일치하는 문자열 그리고 괄호로 기억된 부분 문자열.	["dbbd", "bb"]        |
|        | index             | 입력 문자열에서 일치하는 문자의 인덱스. => 1                           |
|        | input             | 원본 문자열 "cdbbdbsbz"                                              |
|        | [0]               | 마지막으로 일치하는 문자 "dbbd"                                       |
| myRe   | lastIndex         | The index at which to start the next match. (This property is set only if the regular expression uses the g option, described in Advanced Searching With Flags.) |
|        | source            | The text of the pattern. Updated at the time that the regular expression is created, not executed.


# replace

```js
var re = /(\w+)\s(\w+)/;
var str = "John Smith";
var newstr = str.replace(re, "$2, $1");
console.log(newstr);
```


# match
```js
var re = /\w+\s/g;
var str = "fee fi fo fum";
var myArray = str.match(re);
console.log(myArray);

// Output: 
// ["fee ", "fi ", "fo "]
```


# 정규표현식을 문자열로 치환하기

```js
function escapeRegExp(string){
  return string.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); // $&는 일치한 전체 문자열을 의미합니다.
}
```

