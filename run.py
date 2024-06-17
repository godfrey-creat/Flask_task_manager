from app.app_factory import create_app

app = create_app()

if __name__ == '__main__':
    create_db()
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
