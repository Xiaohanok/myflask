from flask import Flask


def create_app():
    app = Flask(__name__)
    # 修改默认的模板文件夹路径
    #app = Flask(__name__, template_folder='ok')

    # 导入并注册蓝图
    from .routes import main
    app.register_blueprint(main)

    return app