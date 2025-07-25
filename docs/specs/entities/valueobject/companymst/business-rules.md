#### ビジネスルール

  1. 会社コードは一意である必要がある
  2. 更新時は必ずupdatecounterをインクリメントする
  3. created_dateとcreated_byは作成時のみ設定し、更新時は変更しない
  4. updated_dateとupdated_byは更新のたびに設定する
