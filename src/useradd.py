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
        gid_count = 0
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
            # GID存在チェック
            if row[3] == line[3]:
                gid_count = gid_count + 1 
        #GIDの存在がなければ例外を発出
        if gid_count == 0:
            raise ValueError(f"The GID:{line[3]} you specified cannot be found in this system.")
    
        ###################################
        #ユーザー作成部分
        ###################################
        
        #変数
        USERID=""
        GID=""
        GNAME=""
        HOMEDIR=""
        EXPIRE_DATE=""
        DISABLE_DATE=""
        COMMENT=""
        LOGIN_SHELL=""
        
        #オプション生成
        if "" != line[2]:
            USERID=f"-u {line[2]}"
        if "" != line[3]:
            GID=f"-g {line[3]}"
        if "" != line[4]:
            GNAME=f"-G {line[4]}"
        if "" != line[5]:
            HOMEDIR=f"-b {line[5]}"
        if "" != line[6]:
            EXPIRE_DATE=f"-e {line[6]}"
        if "" != line[7]:
            DISABLE_DATE=f"-f {line[7]}"
        if "" != line[8]:
            COMMENT=f"-c {line[8]}"
        if "" != line[9]:
            LOGIN_SHELL=f"-s{line[9]}"

        #生成コマンド
        add_command = f"useradd {USERID} {GID} {GNAME} {HOMEDIR} {EXPIRE_DATE} {DISABLE_DATE} {COMMENT} {LOGIN_SHELL} -p {line[1]} {line[0]}"
        
        #コマンド実行
        result = cmd.exec(add_command)
        
        #例外ハンドリング
        if result.stderr != "":
            raise ValueError(f"{result.stderr}")