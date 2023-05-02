#!/usr/bin/python3.9

# -*- coding: utf-8 -*-
import csv
from util import command as cmd
from util import log
import argparse

#共通変数
passwd_account = []

# パーサー作成
parser = argparse.ArgumentParser(
            prog='Useradd Module', # プログラム名
            usage='By adding the required configuration file to this program, \nthe user information described in that configuration file is added to the system.', # プログラムの利用方法
            description='description', # 引数のヘルプの前に表示
            epilog='end', # 引数のヘルプの後で表示
            add_help=True, # -h/–help オプションの追加
            )
 
# 引数の追加
parser.add_argument('-f', '--file', help='The -f or --file option must be used to specify the configuration file.',required=True)
 
# 引数を解析する
args = parser.parse_args()

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

with open(args.file, 'r') as f:
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
            try:
                #ユーザー名存在チェック
                if " " in line[0] or "" == line[0] :
                    raise SyntaxError(f"The UserName has been entered with a blank space!")
                #パスワードチェック
                if " " in line[1] or "" == line[1] :
                    raise SyntaxError(f"The Password has been entered with a blank space!")
                # ユーザー名競合チェック
                if row[0] == line[0]:
                    raise SyntaxError(f"Conflicts with UserName:{line[0]} in existing system!")
                # ユーザーIDチェック
                if row[2] == line[2]:
                    raise SyntaxError(f"Conflicts with UserID:{line[2]} in existing system!")
            except Exception as e:
                log.write.error(f"An exception error has occurred : {e}")
                print(e)
                exit(1)
        
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
        try:
            #例外ハンドリング
            if result.stderr != "":
                raise ValueError(f"{result.stderr}")
        except Exception as e:
            log.write.error(f"Execute command returned an error : {e}")
            print(e)
            exit(1)