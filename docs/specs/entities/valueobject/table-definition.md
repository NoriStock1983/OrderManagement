  ### テーブル定義

  #### authmstテーブル
  ##### テーブル構成
  | 項目名 | 型 | 主キー | NOT NULL | 説明 |
  | --- | --- | --- | --- | --- |
  | authcd | nvarchar(2) | PRIMARY KEY | NOT NULL | 権限コード |
  | authname | nvarchar(50) | | NOT NULL | 権限名 |
  | activeflg | boolean | | NOT NULL | 死活フラグ |
  | created_by | nvarchar(8) | | NOT NULL | 作成者 |
  | created_date | datetime | | NOT NULL | 作成日時 |
  | updated_by | nvarchar(8) | | NOT NULL | 更新者 |
  | updated_date | datetime | | NOT NULL | 更新日時 |
  | updatecounter | number | | NOT NULL | 更新カウンタ |


  #### companymstテーブル
  ##### テーブル構成
  | 項目名 | 型 | 主キー | NOT NULL | 説明 |
  | --- | --- | --- | --- | --- |
  | belonged_companycode | nvarchar(3) | PRIMARY KEY | NOT NULL | 所属会社コード |
  | belonged_companyname | nvarchar(50) | | NOT NULL | 所属会社名 |
  | belonged_companynam_short | nvarchar(10) | | NOT NULL | 所属会社名（略称） |
  | subcontract_class | nvarchar(2) | | NOT NULL | 外注区分 |
  | created_by | nvarchar(8) | | NOT NULL | 作成者 |
  | created_date | datetime | | NOT NULL | 作成日時 |
  | updated_by | nvarchar(8) | | NOT NULL | 更新者 |
  | updated_date | datetime | | NOT NULL | 更新日時 |
  | updatecounter | number | | NOT NULL | 更新カウンタ |


#### deptmstテーブル
##### テーブル構成
  | 項目名 | 型 | 主キー | NOT NULL | 説明 |
  | --- | --- | --- | --- | --- |
  | belonged_deptcode | nvarchar(4) | PRIMARY KEY | NOT NULL | 所属部署コード |
  | belonged_deptname | nvarchar(50) | | NOT NULL | 所属部署名 |
  | belonged_deptname_short | nvarchar(10) | | NOT NULL | 所属部署名（略称） |
  | belonged_companycode | nvarchar(3) | | NOT NULL | 所属会社コード |
  | created_by | nvarchar(8) | | NOT NULL | 作成者 |
  | created_date | datetime | | NOT NULL | 作成日時 |
  | updated_by | nvarchar(8) | | NOT NULL | 更新者 |
  | updated_date | datetime | | NOT NULL | 更新日時 |
  | updatecounter | number | | NOT NULL | 更新カウンタ |

  ##### foregin key
  | FK名 | カラムリスト | 参照先エンティティ名 | 参照先カラムリスト |
  | --- | --- | --- | --- |
  |  | belonged_companycode | companymst | belonged_companycode |


#### usermstテーブル
##### テーブル構成
  | 項目名 | 型 | 主キー | NOT NULL | 説明 |
  | --- | --- | --- | --- | --- |
  | usercode | nvarchar(7) | PRIMARY KEY | NOT NULL | ユーザコード |
  | user_first_name | nvarchar(50) |  | NOT NULL | 氏 |
  | user_last_name | nvarchar(50) |  | NOT NULL | 名 |
  | belonged_companycode | nvarchar(3) |  | NOT NULL | 所属会社コード |
  | belonged_deptcode | nvarchar(4) |  | NOT NULL | 所属部署コード |
  | authcode | nvarchar(2) |  | NOT NULL | 権限コード |
  | created_by | nvarchar(8) | | NOT NULL | 作成者 |
  | created_date | datetime | | NOT NULL | 作成日時 |
  | updated_by | nvarchar(8) | | NOT NULL | 更新者 |
  | updated_date | datetime | | NOT NULL | 更新日時 |
  | updatecounter | number | | NOT NULL | 更新カウンタ |

  ##### foregin key
  | FK名 | カラムリスト | 参照先エンティティ名 | 参照先カラムリスト |
  | --- | --- | --- | --- |
  |  | belonged_companycode | companymst | belonged_companycode |
  |  | belonged_deptcode | deptmst | belonged_deptcode |
  |  | authcd | authmst | authcode |
