# Mutual Fund Analytics Data Dictionary

## 01_fund_master

Contains metadata for all mutual fund schemes.

Important Fields:
- amfi_code
- fund_house
- scheme_name
- category
- sub_category
- benchmark
- expense_ratio_pct
- fund_manager

---

## 02_nav_history

Daily NAV records for all schemes.

Important Fields:
- amfi_code
- date
- nav

---

## 08_investor_transactions

Investor transaction level data.

Important Fields:
- investor_id
- transaction_date
- transaction_type
- amount_inr
- state
- city
- age_group
- gender