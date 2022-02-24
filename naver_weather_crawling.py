from bs4 import BeautifulSoup
import requests

weather_area = input('날씨를 알고 싶은 지역을 입력하세요:')
# weather_area = '구월동'

weather_html = requests.get(f'https://search.naver.com/search.naver?query={weather_area}날씨')
# print(weather_html) # 200 응답코드 확인 # print(weather_html.text) # text 를 써줘야 됨

weather_soup = BeautifulSoup(weather_html.text, 'html.parser') # 파싱한 응답결과 html
# print(weather_soup)
try:
    area_title = weather_soup.find('h2', {'class':'title'}).text # 날씨를 검색한 지역명 크롤링 (string 을 써도되는데 text가 제일 간단하다)
    # print(area_title)
    today_temper = weather_soup.find('div', {'class':'temperature_text'}).text # 오늘 기온 크롤링
    today_temper = today_temper[6:9].strip() # 오늘 기온만 인덱싱한 후 양쪽 공백문자 제거
    # print(today_temper)

    yesterday_weather = weather_soup.find('p', {'class':'summary'}).text # 어제날씨비교 크롤링
    yesterday_weather = yesterday_weather[0:13].strip()
    # print(yesterday_weather)
    # print(len(yesterday_weather)) 길이 확인
    today_weather = weather_soup.find('span', {'class':'weather before_slash'}).text # 오늘날씨(ex:맑음, 흐림, 구름많음.)
    # print(today_weather)
    today_rein = weather_soup.find('dd', {'class':'desc'}).text # 강수확률
    # print(today_rein)


    # 강수확률, 습도, 풍속 크롤링
    # weather_list = weather_soup.select('dl.summary_list>dd')
    # print('강수확률:', weather_list[0].text)
    # print('습도:', weather_list[1].text)
    # print('풍속:', weather_list[2].text)
    # print(weather_list)

    dust_info = weather_soup.find_all('span',{'class':'txt'}) # 미세먼지 정보
    dust1 = dust_info[0].text # 미세먼지
    dust2 = dust_info[1].text # 초미세먼지
except:
    # 해외 도시 검색시 크롤링될 태그 정의
    try:
        area_title = weather_soup.find('span',{'class': 'btn_select'}).text # 날씨를 검색한 지역명 크롤링
        area_title = area_title.strip()
        today_temper = weather_soup.find('span', {'class': 'todaytemp'}).text # 오늘 기온 크롤링
        today_temper = f"{today_temper}°"
        today_weather = weather_soup.find('p', {'class': 'cast_txt'}).text # 오늘 날씨
        today_weather = today_weather[0:2].strip()
        yesterday_weather = weather_soup.find('p', {'class': 'cast_txt'}).text
        today_rein = '-'
        dust1 = '-'
        dust2 = '-'
    except:
        area_title = '검색한 지역은 날씨정보가 없음'
        today_temper = '-'
        today_weather = '-'
        yesterday_weather = '-'
        today_rein = '-'
        dust1 = '-'
        dust2 = '-'

print('******** 오늘의 날씨 정보 ********')
print('검색지역:', area_title)
print('오늘의 날씨:', today_weather)
print('어제와의 비교:', yesterday_weather)
print('오늘의 기온:', today_temper)
print('강수량:', today_rein)
print('미세먼지:', dust1)
print('초미세먼지:', dust2)
print('*******************************')