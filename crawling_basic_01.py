html = '''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>멀티캠퍼스 마켓</title>
</head>
<body>
    <h1> 멀캠 마켓_mulcam_market </h1>
    <div class="sale">
        <p id="fruits1" class="fruits">
            <span class="'name"> 바나나 </span>
            <span class="'price"> 3000원 </span>
            <span class="'inventory"> 500개 </span>
            <span class="'store"> 선릉센터 </span>
            <a href="http://google.co.kr"> 홈페이지 </a>
        </p>
    </div>
    <div class="prepare">
        <p id="fruits2" class="fruits">
            <span class="'name"> 파인애플 </span>
        </p>
    </div>
</body>
</html>

'''

# bs4 : beautifulsoup 정적 웹문서를 파싱 하는 툴

from bs4 import BeautifulSoup

soup = BeautifulSoup(html,'html.parser')
# print(soup)

# print(soup.select('span'))

# print(soup.select('span')[0])
# print(soup.select('span')[-1])

# '#' : id , '.' : class

# print(soup.select('#fruits1'))

# print(soup.select('.price'))

# print(soup.select('span.name'))

tags = soup.select('span.name')

# print(tags[0])
# print(tags[1]) 

# print(tags[0].text)
# print(tags[1].text)

# print(tags[0].text.strip)
# print(tags[1].text.strip)
