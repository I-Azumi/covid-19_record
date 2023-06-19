while True:
    try:
        month = int(input('今日は何月ですか。数字のみ入力してください：'))
        if 1 <= month <= 12:
            break
        else:
            print('正しく入力されていません。')
    except:
        print('正しく入力されていません。')

while True:
    try:
        day = int(input('何日ですか。数字のみ入力してください：'))
        if 1 <= day <= 31:
            break
        else:
            print('正しく入力されていません。')
    except:
        print('正しく入力されていません。')
        
while True:
    try:
        btem = float(input('体温を半角数字のみで入力してください：'))
        if type(btem) == float:
            break
        else:
            type(btem) == str
            print('正しく入力されていません。')
    except:
        print('正しく入力されていません。')
        
with open('体温記録.txt', mode = 'a', encoding = 'utf-8') as f:
    f.write(str(month) + '月'+ str(day) + '日'+ '　')
    f.write(str(btem) +'°\n')
    
print('今日の体調はいかがですか。\n1.平熱よりかなり高い\n2.風邪の症状(鼻水・のどの痛み)がある\n3.倦怠感を感じだるさを感じる\
\n4.息苦しさを感じる\n5.特に変わった症状はない')
while True:
    try:
        condition = int(input('1~5の中から当てはまる番号を1つ入力してください：'))
        if 1 <= condition <= 5:
            break
        else:
            print('1~5で入力しなければいけません。')
    except:
        print('入力してください')
          
if condition == 5:
    print('忘れ物はありませんか？今日も元気にいってらっしゃい！')
    
else:
    print('登校禁止です！のちに【公認欠席の申請】が可能なので必ず休みましょう')
    print('味覚障害・呼吸困難・強い倦怠感・高熱・風邪の症状が３日以上続いていますか。\n1.はい\n2.いいえ')
    while True:
        try:
            ifcorona = int(input('1か2で答えてください：'))
            if 1 <= ifcorona <= 2:
                break
            else:
                print('1か2で入力してください')
        except:
            print('入力してください')
        
    if ifcorona == 2:
        with open('経過観察者用.txt', mode = 'r', encoding = 'utf-8') as f:
            s = f.read()
            print(s)
            
    else:
        print('コロナウイルス感染の疑いがあります。今すぐ大学に連絡しましょう。\
\n金沢工業大学　扇が丘診療所　076-246-1393\n以後、医療機関等の指示に従ってください。')
        


        