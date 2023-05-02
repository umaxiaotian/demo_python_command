#!/usr/bin/python3.9

# -*- coding: utf-8 -*-
import os
import logging
import datetime

##初期定義
dt_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#ログ出力ファイル
logging.basicConfig(filename='./log/command.log',level=logging.DEBUG)
class mkdir:
#ログディレクトリが存在しなければ、作成する関数
    def make_directory(): 
        logging_dir = "log"
        if not os.path.exists(logging_dir):
            # ディレクトリが存在しない場合、ディレクトリを作成する
            os.makedirs(logging_dir)

class write:
    def critical(log):
        logging.critical(f"[{dt_now}] {log}")
    def error(log):
        logging.error(f"[{dt_now}] {log}")
    def warning(log):
        logging.warning(f"[{dt_now}] {log}")
    def info(log):
        logging.info(f"[{dt_now}] {log}")
    def debug(log):
        logging.debug(f"[{dt_now}] {log}")
        
#ディレクトリがなければ作成
mkdir.make_directory()