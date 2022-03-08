import os
import urllib.request

#把这个python文件和guilded表情链接文件放在一个文件夹里
#guilded表情文件命名为emojis.txt
guilded_emoji_link_file = 'emojis.txt'

def get_webp_emoji():
    print('开始执行')

    file = open(guilded_emoji_link_file,'r')
    
    if os.path.exists('emojis'):
        os.mkdir('empjis')
    
    lines = file.readlines()
    for line in lines:
        try:
            url = line.strip()
            filename = url.split('/')[-1]
            found = (filename.find('?') != -1) or (filename.find('&')!= -1)
            if found == True:
                idx = filename.find('webp')
                filename = filename[:idx]+'webp'
            contents = urllib.request.urlopen(url).read()
            wfile = open('emojis\\'+ filename,'wb')
            wfile.write(contents)
            wfile.close()
            print('下载成功:' + filename)
        except:
            print('下载失败: ' + url)
    file.close()
    print('执行完成')

if __name__=='__main__':
    get_webp_emoji()