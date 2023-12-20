# 商品情報管理アプリケーションのバックエンド

## 概要

このプロジェクトは、商品情報（商品名と数量）のCRUD操作を行うWebアプリケーションのバックエンドを構築するものです。商品の追加、削除、一覧の取得など、基本的なCRUD操作が可能です。

## 使用言語と環境

- **OS:** Ubuntu 22.04
- **言語:** Python
- **Webアプリケーションフレームワーク:** Flask
- **Database:** MySQL
- **Webサーバー:** Gunicorn

## 実行環境のセットアップ

1. リポジトリをクローンします: `git clone https://github.com/tokageeee/flask_crud.git`
2. 必要なパッケージをインストールします: `pip install -r requirements.txt`
3. MySQLデータベースをセットアップし、接続情報を `env.json` に設定します。

## 使用法

- 商品の追加:
  curl -X POST -H "Content-Type: application/json" -d '{"name": "ProductA", "amount": 10}' http://localhost:5000/items
- 商品の一覧取得:
  curl http://localhost:5000/items