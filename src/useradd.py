#!/usr/bin/python3.9

# -*- coding: utf-8 -*-
import csv
from util import command as cmd
from util import log

#共通変数
passwd_account = []
##################################################
#実行前チェック
##################################################

#現在のアカウントを取得
passwd = cmd.exec("cat /etc/passwd")
for line in passwd.stdout.split("\n"):
    #特定の文字のインデックスを取得
    # idx = line.find(':')
    # passwd_account.append(line[:idx])
    passwd = line.split(':')
    #空白が入っている場合は、無視
    if "" == passwd[0]:
        continue
    passwd_account.append(passwd)

##################################################
#ユーザー作成メイン
##################################################
#登録ユーザー
userlist = []
with open('useradd.csv', 'r') as f:
    reader = csv.reader(f)

#http://linuxjm.osdn.jp/html/shadow/man8/useradd.8.html
#特に制限はなさそう。グループのところに空白を入れるのはNGとのことなのでそこだけチェック

    #ユーザー存在チェック
    for index,line in enumerate(reader):
        #先頭行は説明なので無視します。
        if index == 0:
            continue
        # print(passwd_account)
        #バリデーションチェック
        for row in passwd_account:
            #ユーザー名存在チェック
            if " " in line[0] or "" == line[0] :
                raise ValueError(f"The UserName has been entered with a blank space!")
            #パスワードチェック
            if " " in line[1] or "" == line[1] :
                raise ValueError(f"The Password has been entered with a blank space!")
            # ユーザー名競合チェック
            if row[0] == line[0]:
                raise ValueError(f"Conflicts with UserName:{line[0]} in existing system!")
            # ユーザーIDチェック
            if row[2] == line[2]:
                raise ValueError(f"Conflicts with UserID:{line[2]} in existing system!")
        userlist.append(line)
    
    #ユーザー作成部分
    for user in userlist:
        print(user[0])
        add_command = f""
    
        
            # print(row[2])
# log.write.critical("TEETTETETE")

