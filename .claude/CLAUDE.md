# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 🚨 最重要ルール TOP5
1. **クリーンアーキテクチャの厳守** - 依存関係は内側から外側への一方向のみ
2. **ValueObjectの必須使用** - Entityのプロパティは必ずValueObject化
3. **テスト駆動開発** - 実装前に必ずテストを書く
4. **日本語での応答** - すべての説明とコメントは日本語で記載
5. **既存コードの規約遵守** - 新規コードは既存の命名規則・スタイルに従う

## 📋 作業開始前チェックリスト
- [ ] 関連するドキュメント（@docs/specs/）を確認した
- [ ] 既存の類似コードを参照した
- [ ] 適切なレイヤーで作業することを確認した
- [ ] テストファイルの配置場所を確認した

## 🏗️ アーキテクチャルール

### ✅ 必須事項
- **依存方向**: Domain → Application → Infrastructure（逆は禁止）
- **各レイヤーの責務を厳守**:
  - Domain: ビジネスロジックのみ
  - Application: ユースケース実装
  - Infrastructure: 技術的詳細

### ❌ 禁止事項
- Domainレイヤーで外部ライブラリをインポートしない
- EntityからRepositoryを直接参照しない
- ValueObjectにビジネスロジックを持たせない

### 📂 ディレクトリ構造
```
src/
├── domain/
│   ├── entity/        # ビジネスエンティティ
│   ├── valueobject/   # 値オブジェクト
│   └── repository/    # リポジトリインターフェース
├── application/
│   └── service/       # アプリケーションサービス
└── infrastructure/
    └── repository/    # リポジトリ実装
```

## 💻 コーディング規約

### Entity作成時
1. **必須メソッド**:
   - `__init__`: ValueObjectのみを引数に取る
   - `create`: プリミティブ値からインスタンス生成
   - `to_dict`: プリミティブ値の辞書を返す
   - `__eq__`: 等価性判定

### ValueObject作成時
1. **必須要素**:
   - バリデーションロジック
   - イミュータブル（不変）
   - `value`プロパティ
   - `__eq__`と`__hash__`メソッド

### 良い例 ✅
```python
class CompanyCode:
    def __init__(self, value: str):
        self._validate(value)
        self._value = value
    
    def _validate(self, value: str) -> None:
        # バリデーションロジック
```

### 悪い例 ❌
```python
class Company:
    def __init__(self, code: str):  # ValueObjectを使っていない
        self.code = code
```

## 🧪 テスト駆動開発

### 実装手順
1. **赤**: 失敗するテストを書く
2. **緑**: テストを通す最小限の実装
3. **リファクタリング**: コードを改善

### テストファイル配置
```
tests/
└── [srcと同じ構造]/
    └── test_[対象ファイル名].py
```

## 📚 参照ドキュメント

### プロジェクト構造
@docs/rules/project-structure.md

### クリーンアーキテクチャ詳細
@docs/rules/clean-architecture.md

### 開発ガイドライン
@docs/rules/development-guide.md

### TDDガイド
@docs/rules/test-driven-guide.md

### リファクタリングガイド
@docs/rules/refactoring-guide.md

## 🔍 エラー時の対処

### インポートエラーが発生したら
- 依存関係の方向を確認
- 適切なインターフェースを使用しているか確認

### テストが失敗したら
- まずテスト自体が正しいか確認
- 最小限の実装から始める

## 🌐 表示言語

**すべての応答は日本語で行ってください。**
- コメント: 日本語
- エラーメッセージ: 日本語
- ドキュメント: 日本語
- 変数名・関数名: 英語（既存の命名規則に従う）