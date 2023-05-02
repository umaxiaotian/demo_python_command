#!/usr/bin/python3.9

# -*- coding: utf-8 -*-
import sys
import argparse

def get_args():
    # 準備
    parser = argparse.ArgumentParser()

    # 標準入力以外の場合
    if sys.stdin.isatty():
        parser.add_argument("--useradd", help="please set me", type=str)

    parser.add_argument("useradd", help="ユーザーを追加するユーティリティを実行できます", type=str)
    parser.add_argument("--type", type=int)
    parser.add_argument("--alert", help="optional", action="store_true")

    # 結果を受ける
    args = parser.parse_args()

    return(args)

def main():
    args = get_args()

    if hasattr(args, 'file'):
        print(args.file)
    print(args.type)
    print(args.alert)

    if args.alert:
        None;# alertが設定されている場合

if __name__ == '__main__':
    main()