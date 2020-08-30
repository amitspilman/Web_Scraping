from bs4 import BeautifulSoup
import urllib.request

f = open('file.csv','w')
f.write('user name,stars,date,title,content,comments,span'+'\n')
for index in range(1, 5):
    num=str(index)
    url = 'https://www.amazon.com/product-reviews/B07GNPDMRP/ref=cm_cr_getr_d_paging_btm_next_'+ num +'/144-9847830-9079603?ie=UTF8&pd_rd_i=B07GNPDMRP&pd_rd_r=3deed5cf-45cf-11e9-87a3-d1c5d12b63d5&pd_rd_w=BDDXx&pd_rd_wg=bIHmf&pf_rd_p=90485860-83e9-4fd9-b838-b28a9b7fda30&pf_rd_r=NE7QZZPR7NK9VH6NQ1ZN&refRID=NE7QZZPR7NK9VH6NQ1ZN&pageNumber='+ num
    response = urllib.request.urlopen(url)
    html=response.read()
    soup = BeautifulSoup(html,'html.parser')
    Posts=soup.findAll('div',attrs={'data-hook':'review'})
    if len(Posts)>0:
        for Post in Posts:
            f.write(str((Post.find('span',attrs={'class':'a-profile-name'})).text.strip()).replace(',','')+',')    #user name
            f.write(str((Post.find('span',attrs={'class':"a-icon-alt"})).text.strip())[0].replace(',','')+',')    #stars
            f.write(str((Post.find('span',attrs={'class':"a-size-base a-color-secondary review-date"})).text.strip()).replace(',','/')+',')   #date
            f.write(str((Post.find('a',attrs={'class':"a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold"})).text.strip()).replace(',','')+',')   #title
            f.write(str((Post.find('span',attrs={'class':"a-size-base review-text review-text-content"})).text.strip()).replace(',','')+',')     #content
            f.write(str((Post.find('span',attrs={'class':"review-comment-total aok-hidden"})).text.strip()).replace(',','')+',')  #number of comments
            x=Post.find('span',attrs={'class':"a-size-base a-color-tertiary cr-vote-text"})
            if x is not None:
                temp=str(x.text.strip()).replace(',','')
                num=temp[:temp.index(' ')]
                f.write(num)  #people found this helpful
            f.write('\n')