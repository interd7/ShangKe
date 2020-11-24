# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :excel_to_mysql
# @Date     :2020/11/18 7:14 下午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pandas as pd
from sqlalchemy import create_engine

df1 = pd.read_excel("兔宝宝(002043)_资产负债表.xls")


#
# df1 = df1.drop('19700101',1)
# df1 = df1.drop('20040630',1)
# df1 = df1.drop('20040930',1)
df1 = df1.drop('报表日期',1)
df1 = df1.drop('单位',1)
df1 = df1.drop('其他应收款',1)
df1 = df1.drop('长期应付款',1)
df1 = df1.drop('在建工程(合计)',1)
df1 = df1.drop('少数股东权益',1)

old_columns1 = ["流动资产", "货币资金", "交易性金融资产", "衍生金融资产", "应收票据及应收账款", "应收票据", "应收账款", "应收款项融资", "预付款项",
               "其他应收款(合计)", "应收利息", "应收股利", "买入返售金融资产", "存货", "划分为持有待售的资产",
               "一年内到期的非流动资产", "待摊费用", "待处理流动资产损益", "其他流动资产", "流动资产合计", "非流动资产", "发放贷款及垫款", "可供出售金融资产", "持有至到期投资",
               "长期应收款", "长期股权投资", "投资性房地产", "在建工程", "工程物资",
               "固定资产及清理(合计)", "固定资产净额", "固定资产清理", "生产性生物资产", "公益性生物资产", "油气资产", "使用权资产", "无形资产", "开发支出", "商誉", "长期待摊费用",
               "递延所得税资产", "其他非流动资产", "非流动资产合计", "资产总计", "流动负债", "短期借款",
               "交易性金融负债", "应付票据及应付账款", "应付票据", "应付账款", "预收款项", "应付手续费及佣金", "应付职工薪酬", "应交税费", "其他应付款(合计)", "应付利息",
               "应付股利", "其他应付款", "预提费用", "一年内的递延收益", "应付短期债券", "一年内到期的非流动负债",
               "其他流动负债", "流动负债合计", "非流动负债", "长期借款", "应付债券", "租赁负债", "长期应付职工薪酬", "长期应付款(合计)", "专项应付款",
               "预计非流动负债", "递延所得税负债", "长期递延收益", "其他非流动负债", "非流动负债合计", "负债合计", "所有者权益", "实收资本(或股本)","资本公积",
               "减：库存股", "其他综合收益", "专项储备", "盈余公积", "一般风险准备", "未分配利润", "归属于母公司股东权益合计", "所有者权益(或股东权益)合计",
               "负债和所有者权益(或股东权益)总计"
               ]
new_columns1 = [
    "current_assets",
    "money_funds",
    "transactional_financial_assets",
    "derivative_financial_assets",
    "notes_receivable_accounts_receivable",
    "bill_receivable",
    "accounts_receivable",
    "receivable_financing",
    "prepayments",
    "other_receivables",
    "interest_receivable",
    "dividend_receivable",
    "bfaura",
    "stock",
    "diahfs",
    "ncadwoy",
    "prepaid_expenses",
    "pcagal",
    "other_current_assets",
    "total_current_assets",
    "non_current_assets",
    "loans_and_advances",
    "available_sale_financial_assets",
    "held_to_maturity_investments",
    "long_term_receivables",
    "long_term_equity_investment",
    "Investment_real_estate",
    "construction_in_progress",
    "engineer_material",
    "fixed_assets_and_liquidation",
    "net_fixed_assets",
    "fixed_assets_liquidation",
    "productive_biological_assets",
    "public_welfare_biological_assets",
    "oil_and_gas_asset",
    "right_of_use_asset",
    "intangible_assets",
    "development_expenditure",
    "goodwill",
    "long_term_prepaid_expenses",
    "deferred_tax_assets",
    "other_non_current_assets",
    "total_non_current_assets",
    "total_assets",
    "current_liabilities",
    "short_term_loan",
    "transactional_financial_liabilities",
    "notes_payable_accounts_payable",
    "bills_payable",
    "accounts_payable",
    "advance_receipt",
    "fees_and_commissions",
    "employee_compensation_payable",
    "taxes_payable",
    "other_payables_total",
    "interest_payable",
    "dividend_payable",
    "other_payables",
    "accrued_fees",
    "deferred_within_one_year",
    "short_term_bonds_payable",
    "current_liabilities_one_year",
    "other_current_liabilities",
    "total_current_liabilities",
    "non_current_liabilities",
    "long_term_loan",
    "bonds_payable",
    "lease_liability",
    "ltecp",
    "long_term_payables",
    "special_payables",
    "estimated_non_current_liabilities",
    "deferred_income_tax_liabilities",
    "long_term_deferred_income",
    "other_non_current_liabilities",
    "total_non_current_liabilities",
    "total_liabilities",
    "owners_equity",
    "paid_in_capital_or_equity",
    "capital_reserve",
    "less_treasury_stock",
    "other_comprehensive_income",
    "special_reserves",
    "surplus_reserve",
    "general_risk_preparation",
    "undistributed_profit",
    "teatsotpc",
    "toeose",
    "tlaoeose",
    "company_year",
    "company_name",
    "company_id"

]
print(len(old_columns1))
print(len(new_columns1))

# 更改列名称
for i in range(0, 89):
    df1 = df1.rename(columns={str(old_columns1[i]):str(new_columns1[i])})

print(df1.head(3))

df1.rename(columns={'category': 'category-size'})
df1 = df1.drop('少数股东权益',1)
engine = create_engine("mysql+mysqlconnector://root:root1234@127.0.0.1:3306/dymtest",echo=False)

# df.to_sql(name='student',con=engine,if_exists='replace')

df1.to_sql(name='TbbZcfz',con=engine,if_exists='replace',index='basis_assets_id')

print(engine.execute("show create table TbbZcfz").first()[1])

# 显示插入表的语句
# print(engine.execute("show create table Tbb").first()[1])
# 统计多少行
# print(engine.execute("select count(1) from Tbb").first())
# 输出前5行
# print(engine.execute("select * from Tbb limit 5").fetchall())
# print(df.head(10))
# df.index.name = "id"
# df.to_excel("/Users/inter.d/PycharmProjects/ShangKe/pa/学生信息表.xls")
