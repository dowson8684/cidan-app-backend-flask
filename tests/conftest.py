import os
import pytest
from app import create_app, db
from app.models.user import User
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


@pytest.fixture
def app():
    """创建并配置用于测试的Flask应用实例"""
    app = create_app(TestConfig)
    
    # 创建数据库表
    with app.app_context():
        db.create_all()
    
    yield app
    
    # 清理数据库
    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """创建测试客户端"""
    return app.test_client()


@pytest.fixture
def runner(app):
    """创建测试CLI运行器"""
    return app.test_cli_runner()


@pytest.fixture
def init_database(app):
    """初始化测试数据库并添加测试数据"""
    with app.app_context():
        # 创建测试用户
        user = User(username='test_user', email='test@example.com')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()
        
        yield db  # 提供数据库会话给测试