#!/usr/bin/python3.6

# -*- coding: utf-8 -*-
from util import command as cmd

##################################################
#実行前チェック
##################################################

#共通変数
passwd_account = []

#現在のアカウントを取得
passwd = cmd.exec("cat /etc/passwd")
for line in passwd.stdout.split("\n"):
    #特定の文字のインデックスを取得
    idx = line.find(':')
    passwd_account.append(line[:idx])
    
print(passwd_account)
