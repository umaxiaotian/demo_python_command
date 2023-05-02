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
    idx = line.find(':')
    passwd_account.append(line[:idx])
    
# print(passwd_account)

##################################################
#ユーザー作成メイン
##################################################

# with open('start.csv', 'r') as f:
#     reader = csv.reader(f)
#     for line in reader:
#         print(line)
log.write.critical("TEETTETETE")