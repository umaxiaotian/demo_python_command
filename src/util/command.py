#!/usr/bin/python3.6

# -*- coding: utf-8 -*-
import logging
import subprocess
import datetime
from . import logdir as log
##初期定義
dt_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#ディレクトリがなければ作成
log.mkdir()

#ログ出力ファイル
logging.basicConfig(filename='./log/command.log',level=logging.DEBUG)

# logging.debug('debug')
# logging.info('info')
# logging.warning('warnig')
# logging.error('error')
# logging.critical('critical')

class exec:
    # 標準出力、標準エラー出力を返す関数
    def cmd(command):
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #returnコード0以外が正常値として取得される可能性があるので、何も入力がstderrになければ
        if result.stderr == b"":
            #stderrがなければ
            logging.info(f"[{dt_now}] [{result.returncode}] [{command}] [{result.stdout}]")
        else:
            #stderrが有効であれあ
            logging.warning(f"[{dt_now}] [{result.returncode}] [{command}] [{result.stderr}]")

        return result
    #変数を自前のselfに格納し、ドッド演算子で参照できるようにする
    def __init__(self,command):
        cmd_res = exec.cmd(command)
        self.returncode = cmd_res.returncode
        self.stdout = cmd_res.stdout.decode('utf-8')
        self.stderr = cmd_res.stderr.decode('utf-8')



