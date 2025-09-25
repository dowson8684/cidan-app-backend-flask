import pytest
from app.models.user import User


def test_user_creation(app):
    """测试用户创建"""
    with app.app_context():
        user = User(username='testuser', email='test@example.com')
        assert user.username == 'testuser'
        assert user.email == 'test@example.com'
        assert user.password_hash is None


def test_password_hashing(app):
    """测试密码哈希功能"""
    with app.app_context():
        user = User(username='testuser', email='test@example.com')
        user.set_password('cat')
        assert user.check_password('cat') is True
        assert user.check_password('dog') is False
        assert user.password_hash is not None