# 学生信息管理系统 (Student Management System)

基于 **FastAPI + SQLAlchemy + MySQL** 的学生信息管理系统，提供学生信息的增删改查 RESTful API，并自动生成 Swagger 交互式 API 文档。

## 技术栈

| 层 | 技术 |
|---|---|
| Web 框架 | FastAPI + Uvicorn |
| ORM | SQLAlchemy 2.x |
| 数据库 | MySQL（PyMySQL 驱动） |
| 数据校验 | Pydantic v2 |

## 功能特性

- 📋 **学生信息管理**：新增、查询、修改、删除学生记录
- ✅ **数据校验**：成绩字段限定 0~100 分，非法输入自动拦截（422）
- 📖 **自动 API 文档**：`/docs` 提供 Swagger UI，可直接在线调试接口
- 🔗 **分层架构**：路由（router）→ 服务（service）→ 仓储（repository）→ 模型（model）四层分离

## 项目结构

```
student-management-system/
├── app/                        # 应用主目录
│   ├── main.py                 # FastAPI 入口，注册路由
│   ├── routers/
│   │   └── students.py         # 学生相关 API（增删改查）
│   ├── service/
│   │   └── student_service.py  # 业务逻辑层（处理异常/事务）
│   ├── repositories/
│   │   └── student_repository.py  # 数据访问层（SQLAlchemy 操作）
│   ├── models/
│   │   └── student.py          # Student 数据库模型
│   ├── database/
│   │   └── session.py          # 数据库连接与 Session
│   └── storage/                # 本地 JSON 存储（遗留）
├── .env                        # 环境变量（数据库连接配置）
├── test_mysql.py               # MySQL 连接测试脚本
└── requirements 说明            # 依赖安装见下文
```

## 快速启动

### 1. 配置数据库

在 `.env` 中配置 MySQL 连接串：

```
MYSQL_URL=mysql+pymysql://root:<你的密码>@localhost:3306/student_db
```

先在 MySQL 中创建数据库与表：

```sql
CREATE DATABASE IF NOT EXISTS student_db DEFAULT CHARSET utf8mb4;

USE student_db;

CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    score INT
);
```

### 2. 安装依赖

```bash
pip install fastapi uvicorn sqlalchemy pymysql pydantic python-dotenv
```

### 3. 启动服务

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

启动后：

- Swagger 文档：http://127.0.0.1:8000/docs
- 健康检查：http://127.0.0.1:8000/hello

## API 接口

| 方法 | 路径 | 说明 | 请求体 | 响应 |
|---|---|---|---|---|
| GET | `/students/{student_id}` | 按 ID 查询学生 | 无 | `StudentResponse` |
| POST | `/students` | 新增学生 | `StudentData` | `MessageResponse` |
| PUT | `/students/{student_id}` | 修改学生成绩/姓名 | `StudentUpdate` | `MessageResponse` |
| DELETE | `/students/{student_id}` | 删除学生 | 无 | `MessageResponse` |
| GET | `/hello` | 连通性测试 | 无 | `{"message": "Hello FastAPI"}` |

### 数据模型

- **StudentData / StudentResponse**：`id`(int)、`name`(str)、`score`(int，0~100)
- **StudentUpdate**：`name`(str)、`score`(int，0~100)
- **MessageResponse**：`message`(str)，操作成功提示

### 示例

查询学生：

```bash
curl http://127.0.0.1:8000/students/101
```

```json
{"id": 101, "name": "张三", "score": 80}
```

新增学生：

```bash
curl -X POST http://127.0.0.1:8000/students \
  -H "Content-Type: application/json" \
  -d '{"id": 200, "name": "李四", "score": 90}'
```

```json
{"message": "已成功添加"}
```

### 错误处理

| 状态码 | 场景 | 返回体 |
|---|---|---|
| 404 | 学生不存在 | `{"detail": "Student Not Found"}` |
| 409 | 学生 ID 已存在 | `{"detail": "Student Already Exists"}` |
| 422 | 请求参数不合法（如成绩超出 0~100） | 校验错误详情 |

## 架构说明

请求处理流程（分层调用，职责清晰）：

```
客户端 → Router(参数校验/响应模型) → Service(业务逻辑/事务) → Repository(数据访问) → Model/DB
```

- **Router**：定义 URL 与请求/响应模型，不写业务代码
- **Service**：处理业务规则与异常（如重复 ID、记录不存在），管理事务提交/回滚
- **Repository**：只负责 SQLAlchemy 数据库操作
- **Model**：ORM 映射，对应 `students` 表

## 开发环境

- Python 3.13
- FastAPI + Uvicorn（异步 Web 框架）
- SQLAlchemy 2.x + PyMySQL
- MySQL 8.x
