-- 1. Create the schema if it doesn't exist
--DROP SCHEMA EQUITY_TRANSACTIONS_LY CASCADE;
CREATE SCHEMA equity_transactions_ly;

-- 2. Create the dim_account table
DROP TABLE equity_transactions_ly.dim_account IF EXISTS;
CREATE TABLE equity_transactions_ly.dim_account (
    account_id INT PRIMARY KEY,  
    account_type VARCHAR(50),
    status VARCHAR(20),
    opening_date DATE,
    risk_level VARCHAR(10),
    balance DECIMAL(18,2),
    margin_enabled BOOLEAN,
    trading_experience VARCHAR(20)
);

-- 3. Create the dim_stock table
DROP TABLE equity_transactions_ly.dim_stock IF EXISTS;
CREATE TABLE equity_transactions_ly.dim_stock (
    stock_id INT PRIMARY KEY,
    stock_symbol VARCHAR(10) UNIQUE,                  
    stock_name VARCHAR(255),
    sector VARCHAR(100),
    industry VARCHAR(100),
    market_cap DECIMAL(18,2)  
);

-- 4. Create the dim_exchange table
DROP TABLE equity_transactions_ly.dim_exchange IF EXISTS;
CREATE TABLE equity_transactions_ly.dim_exchange (
    exchange_id INT PRIMARY KEY,
    exchange_name VARCHAR(100) UNIQUE,
    country VARCHAR(50),
    timezone VARCHAR(10),
    currency VARCHAR(10)
);

-- 5. Create the dim_date table
DROP TABLE equity_transactions_ly.dim_date IF EXISTS;
CREATE TABLE equity_transactions_ly.dim_date (
    date_id INT PRIMARY KEY,
    transaction_date DATE,
    year INT,
    quarter INT,
    month INT,
    week INT,
    day_of_week INT,
    is_weekend BOOLEAN
);

-- 6. Create the fact_transactions table
DROP TABLE equity_transactions_ly.fact_transactions IF EXISTS;
CREATE TABLE equity_transactions_ly.fact_transactions (
    transaction_id INT PRIMARY KEY,
    account_id INT REFERENCES equity_transactions_ly.dim_account(account_id),
    stock_id INT REFERENCES equity_transactions_ly.dim_stock(stock_id),
    date_id INT REFERENCES equity_transactions_ly.dim_date(date_id),
    exchange_id INT REFERENCES equity_transactions_ly.dim_exchange(exchange_id),
    transaction_type VARCHAR(10) CHECK (transaction_type IN ('BUY', 'SELL')),
    quantity INT CHECK (quantity > 0),
    price DECIMAL(10,2) CHECK (price > 0),
    total_value DECIMAL(18,2)
);

-- 7. Insert data into dim_account from the equivalent schema where year > 2024
INSERT INTO equity_transactions_ly.dim_date
SELECT *
FROM equity_transactions.dim_date
WHERE year > 2024;

-- Insert into fact_transactions (filtered by dim_date)
INSERT INTO equity_transactions_ly.fact_transactions
SELECT ft.*
FROM equity_transactions.fact_transactions ft
JOIN equity_transactions_ly.dim_date d ON ft.date_id = d.date_id;

-- Insert into dim_account (using filtered fact_transactions)
INSERT INTO equity_transactions_ly.dim_account
SELECT DISTINCT a.*
FROM equity_transactions.dim_account a
JOIN equity_transactions_ly.fact_transactions ft ON a.account_id = ft.account_id;

-- Insert into dim_stock (using filtered fact_transactions)
INSERT INTO equity_transactions_ly.dim_stock
SELECT DISTINCT s.*
FROM equity_transactions.dim_stock s
JOIN equity_transactions_ly.fact_transactions ft ON s.stock_id = ft.stock_id;

-- Insert into dim_exchange (using filtered fact_transactions)
INSERT INTO equity_transactions_ly.dim_exchange
SELECT DISTINCT e.*
FROM equity_transactions.dim_exchange e
JOIN equity_transactions_ly.fact_transactions ft ON e.exchange_id = ft.exchange_id;
