from urllib import request



def GetHtml(url):
    page = request.urlopen(url).read()
    return page

def SaveHtml(file_name,file_content):
    with open(file_name + ".html", "wb") as f:
        f.write(file_content)


aurl = "https://movie.douban.com/cinema/nowplaying/beijing/"
page_content = GetHtml(aurl)
save_page_content = SaveHtml("DouMovie",page_content)