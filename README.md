# 彩蛋APP后端Flask服务

这是彩蛋APP的后端服务，基于Flask框架开发，提供API接口和数据库访问功能。

## 项目结构

```
cidan-app-backend-flask/
├── app/                    # 应用主目录
│   ├── api/                # API路由
│   └── models/             # 数据模型
├── migrations/             # 数据库迁移文件
├── tests/                  # 测试用例
├── .flaskenv               # Flask环境配置
├── .github/workflows/      # GitHub Actions CI/CD配置
├── config.py               # 应用配置
├── requirements.txt        # 依赖包列表
└── run.py                  # 应用入口
```

## 开发环境设置

1. 克隆仓库
```bash
git clone https://github.com/dowson8684/cidan-app-backend-flask.git
cd cidan-app-backend-flask
```

2. 创建并激活虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 配置数据库
```bash
flask db upgrade
```

5. 运行应用
```bash
flask run
```

## API文档

- `/api/ping`: 测试API是否正常工作

## CI/CD流程

本项目使用GitHub Actions进行CI/CD自动化，包括：
- 代码质量检查（flake8, black）
- 自动化测试（pytest）
- 构建和部署