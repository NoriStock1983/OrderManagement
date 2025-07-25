# プロジェクト構造

## 概要

これはPythonプロジェクトで、現在は`main.py`にシンプルな「Hello, World!」アプリケーションが含まれています。

## 推奨するプロジェクト構造（クリーンアーキテクチャ）

```
claude/
├── main.py                # エントリーポイント
├── requirements.txt       # 外部依存関係
├── .gitignore            # Git除外設定
├── CLAUDE.md             # プロジェクトメモリ
├── docs/                 # ドキュメント
├── tests/                # テストコード
├── src/                  # ソースコード
│   ├── domain/           # ドメインレイヤー
│   │   ├── entities/     # エンティティ
│   │   ├── value_objects/ # 値オブジェクト
│   │   ├── repositories/ # リポジトリインターフェース
│   │   └── services/     # ドメインサービス
│   ├── application/      # アプリケーションレイヤー
│   │   ├── use_cases/    # ユースケース
│   │   ├── services/     # アプリケーションサービス
│   │   └── dtos/         # データ転送オブジェクト
│   ├── infrastructure/   # インフラストラクチャレイヤー
│   │   ├── repositories/ # リポジトリ実装
│   │   ├── external_apis/ # 外部API
│   │   └── database/     # データベース関連
│   └── presentation/     # プレゼンテーションレイヤー
│       ├── controllers/  # コントローラー
│       ├── views/        # ビュー
│       └── serializers/  # シリアライザー
└── .claude/              # Claude固有のファイル
    └── settings.local.json
```

## ファイル・ディレクトリ命名規則

### ディレクトリ
- `snake_case` を使用
- 複数形を使用（例：`entities/`, `use_cases/`）
- 階層を明確にする

### ファイル
- `snake_case.py` を使用
- 単数形を使用（例：`user_repository.py`, `order_service.py`）
- 責務を明確にする命名

### 例
```
src/domain/entities/user.py           # Userエンティティ
src/domain/repositories/user_repository.py  # UserRepositoryインターフェース
src/application/use_cases/create_user_use_case.py  # CreateUserUseCase
src/infrastructure/repositories/user_repository_impl.py  # UserRepository実装
```

## 設定ファイル

### requirements.txt
外部依存関係を管理：
```
pytest>=7.0.0
black>=22.0.0
flake8>=4.0.0
```

### .gitignore
Python固有の除外設定：
```
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.env
.DS_Store
```

### pytest.ini
テスト設定（推奨）：
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```