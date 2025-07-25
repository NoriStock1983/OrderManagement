# 開発ガイドライン

## よく使うコマンド

### アプリケーションの実行

```bash
python main.py
```

### Python バージョン

モダンなPython機能との互換性のため、Python 3.13以上を使用してください。

## このプロジェクトを拡張する際の推奨事項

1. 外部依存関係が必要な場合は`requirements.txt`を追加
2. Pythonプロジェクト用の`.gitignore`ファイルの追加を検討（`__pycache__/`、`*.pyc`、`.env`などを含める）
3. テストフレームワークとしてpytestの使用を検討
4. リンティングとフォーマッティングには`black`、`flake8`、`ruff`などのツールの使用を検討

## コーディング規約

### ファイル命名規則

- Pythonファイル: `snake_case.py`
- クラス名: `PascalCase`
- 関数・変数名: `snake_case`
- 定数: `UPPER_SNAKE_CASE`

### ディレクトリ命名規則

- パッケージ: `snake_case`
- テストディレクトリ: `tests/`
- ドキュメント: `docs/`

### インポート順序

1. 標準ライブラリ
2. サードパーティライブラリ  
3. ローカルアプリケーション/ライブラリ

例：

```python
import os
import sys

import requests
import pytest

from domain.entities.user import User
from application.use_cases.create_user import CreateUserUseCase
```

### 型ヒント

Python 3.6以上では型ヒントを積極的に使用：

```python
def create_user(name: str, age: int) -> User:
    return User(name, age)
```

### ドキュメント

関数・クラスにはdocstringを記述：

```python
def calculate_total(items: list[Item]) -> float:
    """
    商品リストの合計金額を計算する
    
    Args:
        items: 商品のリスト
        
    Returns:
        合計金額
        
    Raises:
        ValueError: 商品リストが空の場合
    """
    if not items:
        raise ValueError("商品リストが空です")
    
    return sum(item.price for item in items)
```
