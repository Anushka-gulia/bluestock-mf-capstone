-- Total Funds

SELECT COUNT(*) FROM fund_master;

-- Total Transactions

SELECT COUNT(*) FROM transactions;

-- Top States by Investment

SELECT
    state,
    SUM(amount_inr) AS total_amount
FROM transactions
GROUP BY state
ORDER BY total_amount DESC;

-- Transaction Type Distribution

SELECT
    transaction_type,
    COUNT(*) AS total_count
FROM transactions
GROUP BY transaction_type;

-- Top Fund Houses

SELECT
    fund_house,
    COUNT(*) AS schemes
FROM fund_master
GROUP BY fund_house
ORDER BY schemes DESC;