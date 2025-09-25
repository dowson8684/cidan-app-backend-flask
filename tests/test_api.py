import json
import pytest
from app import db
from app.models.user import User


def test_ping_endpoint(client):
    """测试ping端点是否正常工作"""
    response = client.get('/api/ping')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'pong'
    assert data['status'] == 'success'