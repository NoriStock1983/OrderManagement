# リファクタリングガイド

## Martin Fowlerのリファクタリング手法

### リファクタリングの定義

外部から見た振る舞いを変えずに、コードの内部構造を改善すること

## 基本的なリファクタリング手法

### 1. 関数の抽出 (Extract Function)

```python
# Before
def print_owing(invoice):
    print_banner()
    
    # print details
    print(f"name: {invoice.customer}")
    print(f"amount: {invoice.amount}")

# After
def print_owing(invoice):
    print_banner()
    print_details(invoice)

def print_details(invoice):
    print(f"name: {invoice.customer}")
    print(f"amount: {invoice.amount}")
```

**手順:**

1. 抽出する部分を特定
2. 新しい関数を作成
3. パラメータと戻り値を決定
4. 元のコードを関数呼び出しに置き換え
5. テストを実行

### 2. 変数のインライン化 (Inline Variable)

```python
# Before
base_price = an_order.base_price
return base_price > 1000

# After
return an_order.base_price > 1000
```

**手順:**

1. 変数への参照を式で置き換え
2. テストを実行
3. 変数宣言を削除

### 3. 関数の名前変更 (Rename Function)

```python
# Before
def get_annual_income():
    pass

# After
def calculate_yearly_salary():
    pass
```

**手順:**

1. 新しい名前の関数を作成
2. 古い関数から新しい関数を呼び出す
3. 全ての呼び出し元を更新
4. 古い関数を削除

### 4. 変数のカプセル化 (Encapsulate Variable)

```python
# Before
default_owner = {"first_name": "Martin", "last_name": "Fowler"}

# After
class Owner:
    def __init__(self):
        self._data = {"first_name": "Martin", "last_name": "Fowler"}
    
    def get_default_owner(self):
        return self._data.copy()
    
    def set_default_owner(self, owner):
        self._data = owner.copy()
```

### 5. パラメータオブジェクトの導入 (Introduce Parameter Object)

```python
# Before
def amount_invoiced(start_date, end_date):
    pass

def amount_received(start_date, end_date):
    pass

# After
class DateRange:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

def amount_invoiced(date_range):
    pass

def amount_received(date_range):
    pass
```

### 6. 条件記述の分解 (Decompose Conditional)

```python
# Before
if not date.is_before(SUMMER_START) and not date.is_after(SUMMER_END):
    charge = quantity * summer_rate
else:
    charge = quantity * regular_rate

# After
if is_summer(date):
    charge = summer_charge(quantity)
else:
    charge = regular_charge(quantity)

def is_summer(date):
    return not date.is_before(SUMMER_START) and not date.is_after(SUMMER_END)

def summer_charge(quantity):
    return quantity * summer_rate

def regular_charge(quantity):
    return quantity * regular_rate
```

## コードの臭い (Code Smells)

### 1. 長すぎるメソッド (Long Method)

- **症状**: 10行を超えるメソッド
- **対処**: Extract Function

### 2. 巨大なクラス (Large Class)

- **症状**: 多すぎる責任を持つクラス
- **対処**: Extract Class, Extract Subclass

### 3. 長すぎるパラメータリスト (Long Parameter List)

- **症状**: 3つ以上のパラメータ
- **対処**: Introduce Parameter Object, Preserve Whole Object

### 4. データの塊 (Data Clumps)

- **症状**: 同じデータ項目群が一緒に現れる
- **対処**: Extract Class, Introduce Parameter Object

### 5. 基本データ型への執着 (Primitive Obsession)

- **症状**: 基本データ型で複雑な概念を表現
- **対処**: Replace Primitive with Object

### 6. スイッチ文 (Switch Statements)

- **症状**: 同じスイッチ文が複数箇所に現れる
- **対処**: Replace Conditional with Polymorphism

### 7. 並行して変更されるクラス (Parallel Inheritance Hierarchies)

- **症状**: クラスを追加するたびに別の階層にもクラスを追加
- **対処**: Move Method, Move Field

### 8. 怠惰なクラス (Lazy Class)

- **症状**: 十分な仕事をしないクラス
- **対処**: Inline Class, Collapse Hierarchy

### 9. 推測による一般化 (Speculative Generality)

- **症状**: 将来のための不要な抽象化
- **対処**: Collapse Hierarchy, Inline Class, Inline Function

### 10. 一時的属性 (Temporary Field)

- **症状**: 特定の状況でのみ値を持つ属性
- **対処**: Extract Class, Introduce Null Object

## リファクタリングの手順

### 1. 準備フェーズ

1. **テストの確認**: 既存のテストが全て通ることを確認
2. **テストの追加**: カバレッジが不十分な場合はテストを追加
3. **バージョン管理**: 現在の状態をコミット

### 2. リファクタリング実行

1. **小さな変更**: 一度に一つのリファクタリングのみ実行
2. **テスト実行**: 各ステップ後にテストを実行
3. **コミット**: 各リファクタリング完了後にコミット

### 3. 検証フェーズ

1. **全テスト実行**: 全てのテストが通ることを確認
2. **パフォーマンス確認**: 必要に応じてパフォーマンステスト
3. **コードレビュー**: チームメンバーによるレビュー

## リファクタリングのタイミング

### 1. 追加前のリファクタリング

新機能を追加しやすくするためのリファクタリング

### 2. 理解のためのリファクタリング

コードを理解した後、その理解を反映させるリファクタリング

### 3. ゴミ拾いリファクタリング

小さな問題を見つけたらすぐに修正

### 4. 計画的リファクタリング

技術的負債を返済するための計画的な活動

## リファクタリングの原則

### 1. 振る舞いの保持

- 外部から見た振る舞いを変えない
- 機能追加とリファクタリングを混ぜない

### 2. 小さなステップ

- 一度に大きな変更をしない
- 各ステップでテストを実行

### 3. 頻繁なコミット

- 小さな改善ごとにコミット
- いつでも前の状態に戻れるように

### 4. テストファースト

- リファクタリング前にテストを用意
- テストがセーフティネットとなる

## プロジェクトでの適用

### クリーンアーキテクチャとの統合

- リファクタリング時も依存関係の方向を維持
- レイヤー間の境界を尊重

### TDDサイクルとの統合

- Red-Green-Refactorサイクルの一部として実施
- Greenフェーズでのみリファクタリング

### 継続的な改善

- 完璧を求めすぎない
- 少しずつ、しかし継続的に改善

## 参考文献

- "Refactoring: Improving the Design of Existing Code" by Martin Fowler
- "Clean Code" by Robert C. Martin
- "Working Effectively with Legacy Code" by Michael Feathers
