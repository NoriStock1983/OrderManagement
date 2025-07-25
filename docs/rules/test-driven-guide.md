# TDD（テスト駆動開発）ルール

テスト駆動開発の手順に従った開発ルールです。

## TDDの基本サイクル（Red-Green-Refactor）

### 1. Red（失敗するテストを書く）

- **目的**: 最初に失敗するテストを作成する
- **手順**:
  1. まだ存在しない機能のテストを書く
  2. テストが失敗することを確認する
  3. 最小限のテストケースから始める

### 2. Green（テストを通すための最小限のコードを書く）

- **目的**: テストを通すための最小限の実装を行う
- **手順**:
  1. テストを通すために必要最小限のコードを書く
  2. 汚いコードでも構わない（後でリファクタリングする）
  3. テストが通ることを確認する

### 3. Refactor（コードを改善する）

- **目的**: テストを通したまま、コードの品質を向上させる
- **手順**:
  1. 重複を取り除く
  2. 意図を明確にする
  3. テストが通り続けることを確認しながら改善する

## TDD実践ルール

### テスト作成の原則

#### 1. 最小限のテストから始める

```python
# ❌ 悪い例：一度に複雑なテストを書く
def test_user_registration_with_validation_and_notification():
    # 複雑すぎる
    pass

# ✅ 良い例：最小限のテストから始める
def test_user_can_be_created():
    user = User("Alice")
    assert user.name == "Alice"
```

#### 2. 1つのテストは1つの観点のみをテストする

```python
# ❌ 悪い例：複数の観点を1つのテストでテスト
def test_user_creation_and_validation():
    # 作成とバリデーションを同時にテスト
    pass

# ✅ 良い例：1つの観点のみをテスト
def test_user_creation():
    user = User("Alice")
    assert user.name == "Alice"

def test_user_name_validation():
    with pytest.raises(ValueError):
        User("")
```

#### 3. テスト名は仕様を表現する

```python
# ❌ 悪い例：実装詳細を表現
def test_user_constructor():
    pass

# ✅ 良い例：仕様・振る舞いを表現
def test_user_name_should_be_set_when_user_is_created():
    pass

def test_should_raise_error_when_user_name_is_empty():
    pass
```

### テスト構造のパターン

#### AAA（Arrange-Act-Assert）パターン

```python
def test_user_can_change_name():
    # Arrange（準備）
    user = User("Alice")
    new_name = "Bob"
    
    # Act（実行）
    user.change_name(new_name)
    
    # Assert（検証）
    assert user.name == new_name
```

#### Given-When-Then パターン

```python
def test_user_can_change_name():
    # Given（前提条件）
    user = User("Alice")
    
    # When（操作）
    user.change_name("Bob")
    
    # Then（期待結果）
    assert user.name == "Bob"
```

## 実装手順

### 1. 機能追加時の手順

1. **要件を理解する**
   - 何を作るかを明確にする
   - 受け入れ条件を定義する

2. **最初のテストを書く**
   - 最もシンプルなケースから始める
   - 期待する振る舞いを表現する

3. **実装する**
   - テストを通すための最小限のコード
   - ハードコードでも構わない

4. **リファクタリング**
   - 重複を排除
   - 意図を明確にする

5. **次のテストケースに進む**
   - より複雑なケースを追加
   - サイクルを繰り返す

### 2. バグ修正時の手順

1. **バグを再現するテストを書く**
   - 失敗するテストでバグを確認
   - 期待する正しい動作を表現

2. **バグを修正する**
   - テストが通るように修正
   - 最小限の変更で対応

3. **リファクタリング**
   - 必要に応じてコードを改善
   - テストが通り続けることを確認

## テストファイルの構成

### ディレクトリ構造

```Folder
tests/
├── unit/                    # 単体テスト
│   ├── domain/
│   │   ├── entities/
│   │   └── services/
│   └── application/
│       └── use_cases/
├── integration/             # 統合テスト
│   ├── infrastructure/
│   └── presentation/
└── e2e/                     # E2Eテスト
    └── scenarios/
```

### テストファイル命名規則

- `test_[対象ファイル名].py`
- 例：`user.py` → `test_user.py`
- 例：`user_service.py` → `test_user_service.py`

### テストクラス構成

```python
class TestUser:
    """Userエンティティのテスト"""
    
    class TestCreation:
        """ユーザー作成に関するテスト"""
        
        def test_should_create_user_with_valid_name(self):
            pass
            
        def test_should_raise_error_when_name_is_empty(self):
            pass
    
    class TestNameChange:
        """名前変更に関するテスト"""
        
        def test_should_change_name_when_valid_name_provided(self):
            pass
```

## アンチパターン（避けるべきパターン）

### 1. テストを後回しにする

```python
# ❌ 悪い例：実装を先に書く
def create_user(name):
    # 実装を先に書いてからテストを書く
    pass

# ✅ 良い例：テストを先に書く
def test_should_create_user_with_name():
    # テストを先に書く
    user = create_user("Alice")
    assert user.name == "Alice"
```

### 2. 複雑すぎるテスト

```python
# ❌ 悪い例：複雑なセットアップ
def test_complex_user_workflow():
    # 複雑なセットアップ
    # 複数の操作
    # 複数のアサーション
    pass

# ✅ 良い例：シンプルなテスト
def test_user_creation():
    user = User("Alice")
    assert user.name == "Alice"
```

### 3. 実装詳細をテストする

```python
# ❌ 悪い例：内部実装をテスト
def test_user_internal_state():
    user = User("Alice")
    assert user._internal_id is not None  # 内部実装

# ✅ 良い例：公開インターフェースをテスト
def test_user_has_unique_id():
    user1 = User("Alice")
    user2 = User("Bob")
    assert user1.id != user2.id  # 公開インターフェース
```

## ツールとライブラリ

### 推奨テストフレームワーク

- **pytest**: Python標準のテストフレームワーク
- **unittest**: Python標準ライブラリ

### テスト支援ライブラリ

- **pytest-mock**: モックライブラリ
- **factory_boy**: テストデータ生成
- **pytest-cov**: カバレッジ測定

### テスト実行コマンド

```bash
# 全テスト実行
pytest

# 特定のテストファイル実行
pytest tests/unit/domain/test_user.py

# カバレッジ付きで実行
pytest --cov=src

# 失敗したテストのみ再実行
pytest --lf
```

## TDD実践時の心構え

### 1. 小さなステップで進む

- 一度に大きな機能を作らない
- 最小限の変更で確実に進歩する

### 2. テストファーストを徹底する

- 実装前に必ずテストを書く
- テストが失敗することを確認する

### 3. リファクタリングを恐れない

- テストがあるので安全にリファクタリングできる
- 継続的にコードを改善する

### 4. テストもコードの一部として扱う

- テストコードも読みやすく保つ
- 重複を排除し、保守しやすくする
