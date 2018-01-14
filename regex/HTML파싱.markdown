정규표현식
==========


따옴표 사이에 문자열
------------------

이런 문자가 있다고 치자
```
<a href='../aaaaa-mdm_.html'>Title asdkf.ask3!93</a>........</a>
```

따옴표 사이에 문자열은 `[^']`와 `[^"]`를 사용해서 선택할 수 있다.

```
href='[^']*'
href="[^"]*"
```

태그와 그룹
-------------------


```
style='text-decoration:line-through'>[\w\s.]*</a>
```


C#예제
------------------
```
public void find(ref List<Link> rst, string category, int startPage, int endPage)
{
    string urlFormat = "https://torrentkim5.net/{0}/torrent{1}.htm";

    for(int iPage = startPage; iPage <= endPage; iPage++)
    {
        var request = (HttpWebRequest)WebRequest.Create(string.Format(urlFormat, category, iPage));
        var response = (HttpWebResponse)request.GetResponse();
        var resStream = response.GetResponseStream();
        var streamReader = new StreamReader(resStream, Encoding.UTF8);

        /*
         * html에서 이렇게 생긴 줄을 찾아서 잘라낸다.
         * <a href='../torrent_game/72329.html' style='text-decoration:line-through'>Kerbal Space Program 1.2.2</a>
         */
        string html = streamReader.ReadToEnd();
        string pattern = "<a href='([^']*)' style='text-decoration:line-through'>([^<]*)</a>";

        foreach (Match m in Regex.Matches(html, pattern))
        {
            //Groups[0] 전체
            //Groups[1] 첫번째 그룹
            string relUrl = m.Groups[1].Value;
            string absUrl = relUrl.Replace("../", "https://torrentkim5.net/");
            Link link;
            link.Text = m.Groups[2].Value;
            link.URL = absUrl;
            rst.Add(link);
        }
    }
}
```
