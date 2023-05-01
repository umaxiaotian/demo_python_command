#!/usr/bin/python3.6

# -*- coding: utf-8 -*-
import os
#ログディレクトリ作成

#ログディレクトリが存在しなければ、作成する関数
def mkdir(): 
    logging_dir = "log"
    if not os.path.exists(logging_dir):
        # ディレクトリが存在しない場合、ディレクトリを作成する
        os.makedirs(logging_dir)
