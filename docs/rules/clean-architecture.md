# クリーンアーキテクチャルール

## アーキテクチャ構造（依存関係の方向）

```
Presentation → Application → Domain
Infrastructure → Application → Domain
```

## レイヤー定義と責務

### 1. Domain Layer（最内層）

- **責務**: ビジネスロジック、エンティティ、ドメインサービス
- **依存関係**: 他のレイヤーに依存しない
- **配置**: `domain/` ディレクトリ
- **含むもの**: エンティティ、値オブジェクト、ドメインサービス、リポジトリインターフェース

### 2. Application Layer（ユースケース層）

- **責務**: アプリケーションのユースケース、ビジネスフロー
- **依存関係**: Domainレイヤーのみに依存
- **配置**: `application/` ディレクトリ
- **含むもの**: ユースケース、アプリケーションサービス、DTOs

### 3. Infrastructure Layer（インフラ層）

- **責務**: 外部システムとの連携、データ永続化
- **依存関係**: ApplicationとDomainレイヤーに依存
- **配置**: `infrastructure/` ディレクトリ
- **含むもの**: リポジトリ実装、外部API、データベース接続

### 4. Presentation Layer（プレゼンテーション層）

- **責務**: UI、コントローラー、入出力の処理
- **依存関係**: ApplicationとDomainレイヤーに依存
- **配置**: `presentation/` ディレクトリ
- **含むもの**: コントローラー、ビュー、シリアライザー

## 実装ルール

### 必須ルール

1. **依存関係逆転の原則**: 外側のレイヤーは内側のレイヤーに依存する
2. **インターフェース分離**: 抽象化（インターフェース）は内側のレイヤーで定義
3. **フレームワーク独立**: Domainレイヤーは外部フレームワークに依存しない
4. **データベース独立**: Domainレイヤーはデータベースの実装詳細を知らない

### 禁止事項

- Domainレイヤーから外側レイヤーへの直接参照
- Applicationレイヤーから Infrastructure/Presentation レイヤーへの直接参照
- 具体実装への直接依存（抽象化を使用する）

## ディレクトリ構造例

```
src/
├── domain/
│   ├── entities/
│   ├── value_objects/
│   ├── repositories/  # インターフェースのみ
│   └── services/
├── application/
│   ├── use_cases/
│   ├── services/
│   └── dtos/
├── infrastructure/
│   ├── repositories/  # 実装
│   ├── external_apis/
│   └── database/
└── presentation/
    ├── controllers/
    ├── views/
    └── serializers/
```

## コード作成時の注意点

### ファイル作成ルール

1. **新しいファイルを作成する前に**：
   - 既存のファイル構造を確認
   - 適切なレイヤーのディレクトリに配置
   - 命名規則に従う（例：`user_repository.py`、`user_service.py`）

2. **クラス・関数の命名**：
   - エンティティ: `User`、`Order`（単数形）
   - リポジトリ: `UserRepository`（インターフェース）、`UserRepositoryImpl`（実装）
   - ユースケース: `CreateUserUseCase`
   - サービス: `UserDomainService`

3. **依存関係の注入**：
   - コンストラクタでインターフェースを受け取る
   - 具体実装は外側のレイヤーで注入
   - 依存関係逆転の原則を徹底

### インポート規則

- Domainレイヤー: 標準ライブラリのみ
- Applicationレイヤー: domain パッケージのみインポート可
- Infrastructure/Presentation: 全レイヤーをインポート可

### 実装パターン

#### Domainレイヤー

```python
# エンティティ例
class User:
    def __init__(self, user_id: str, name: str):
        self._user_id = user_id
        self._name = name
    
    def change_name(self, new_name: str):
        # ビジネスルールをここに実装
        pass

# リポジトリインターフェース例
from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        pass
    
    @abstractmethod
    def find_by_id(self, user_id: str) -> User:
        pass
```

#### Applicationレイヤー

```python
# ユースケース例
class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository
    
    def execute(self, request: CreateUserRequest) -> CreateUserResponse:
        # ユースケースのロジック
        pass
```

#### Infrastructureレイヤー

```python
# リポジトリ実装例
from domain.repositories.user_repository import UserRepository

class UserRepositoryImpl(UserRepository):
    def save(self, user: User) -> None:
        # データベース操作の実装
        pass
```

### 禁止パターン

- ❌ Domainレイヤーから外部ライブラリのインポート
- ❌ Applicationレイヤーから具体実装の直接インポート
- ❌ ビジネスロジックをPresentation/Infrastructureレイヤーに記述
- ❌ データベース固有の処理をDomainレイヤーに記述

### テスト戦略

- Domainレイヤー: 単体テスト中心
- Applicationレイヤー: ユースケーステスト
- Infrastructure: 統合テスト
- Presentation: E2Eテスト
