from app import app, db, Post

if __name__ == "__main__":
    with app.app_context():
        # データベースを作成
        db.create_all()

        # 複数のポストを作成
        posts = [
            Post(title="first post1", body="This is the first post1"),
            Post(title="second post", body="This is the second post"),
            Post(title="third post", body="This is the third post")
        ]

        # セッションに追加
        for post in posts:
            db.session.add(post)

        # コミットしてデータベースに保存
        db.session.commit()

        print("新しいポストが追加されました！")