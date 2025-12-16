# Descripción de datos Netezza
> Los datos son generados y no están relacionados con la situación real del mercado de valores

`INVESTMENTS` database `EQUITY_TRANSACTIONS` schema  
Contiene información sobre operaciones de mercado bursátil de 2019 a 2025 para diferentes bolsas y acciones.

![ERD](attachments/2025-04-25-10-34-28-pasted-vscode.png)

## 📁 `fact_transactions` — Tabla de hechos central que registra todas las transacciones de acciones
El número total de transacciones se establece en 1 200 000. Consideramos los precios en una sola moneda (USD) y no calcularemos conversiones ni efectos de tipo de cambio.

| Nombre de columna | Tipo           | Descripción                                                  | Posibles valores / Notas                       |
|-------------------|----------------|--------------------------------------------------------------|------------------------------------------------|
| `transaction_id`  | INT            | Identificador único de cada transacción                      | Auto-incremental o generado                    |
| `account_id`      | INT            | Referencia a la tabla `dim_account`                          | Foreign key                                     |
| `stock_id`        | INT            | Referencia a la tabla `dim_stock`                            | Foreign key                                     |
| `exchange_id`     | INT            | Referencia a la tabla `dim_exchange`                         | Foreign key                                     |
| `date_id`         | INT            | Referencia a la tabla `dim_date`                             | Foreign key                                     |
| `order_type`| VARCHAR(10)    | Tipo de transacción                                         | `'BUY'`, `'SELL'`                               |
| `quantity`          | INT            | Número de acciones negociadas                                | Enteros positivos                               |
| `price`           | DECIMAL(10,2)  | Precio por acción al momento de la transacción               | Decimales positivos                             |
| `total_value`     | DECIMAL(18,2)  | Valor total calculado (`quantity * price`)                   | Calculado automáticamente                       |

## 👤 `dim_account` — Metadatos de cuentas, incluidos detalles del cliente y de trading
Los clientes pueden tener varias cuentas abiertas; en el conjunto de datos actual hay 123 000 clientes y 246 301 cuentas.

| Nombre de columna   | Tipo           | Descripción                                                | Posibles valores / Notas                     |
|---------------------|----------------|------------------------------------------------------------|----------------------------------------------|
| `account_id`        | INT            | Identificador único de la cuenta                           | Primary key                                   |
| `account_type`      | VARCHAR(50)    | Tipo de cuenta                                             | `'Retail'`, `'Institutional'`, `'Margin'`     |
| `status`            | VARCHAR(20)    | Estado actual de la cuenta                                 | `'Active'`, `'Suspended'`, `'Closed'`         |
| `opening_date`      | DATE           | Fecha de apertura de la cuenta                             | Fechas pasadas                                |
| `risk_level`        | VARCHAR(10)    | Perfil de riesgo asignado                                  | `'Low'`, `'Medium'`, `'High'`                 |
| `balance`           | DECIMAL(18,2)  | Saldo actual de la cuenta                                  | `$1,000 - $1,000,000`                         |
| `margin_enabled`    | BOOLEAN        | Indica si el margin trading está habilitado                | `True`, `False`                               |
| `trading_experience`| VARCHAR(20)    | Experiencia de trading autoevaluada por el usuario         | `'Beginner'`, `'Intermediate'`, `'Expert'`    |

## 📈 `dim_stock` — Información sobre acciones individuales
La mayoría de las acciones, aparte de cuatro (BAC, IBM, AMZN, HD) que usaremos en los labs posteriores, son datos sintéticos (empresas inexistentes); hay 100 empresas ficticias.

| Nombre de columna | Tipo           | Descripción                                            | Posibles valores / Notas           |
|------------------|----------------|--------------------------------------------------------|------------------------------------|
| `stock_id`       | INT            | ID único de cada acción                               | Primary key                         |
| `stock_symbol`   | VARCHAR(10)    | Símbolo ticker de la acción                           | `'YATE'`, `'IBM'`, etc.             |
| `stock_name`     | VARCHAR(255)   | Nombre completo de la acción/compañía                 | `'Yates-Rhodes.'`, etc.             |
| `sector`         | VARCHAR(100)   | Clasificación de sector                               | `'Technology'`, `'Healthcare'`, etc.|
| `industry`       | VARCHAR(100)   | Industria específica                                  | `'Software'`, `'Banking'`, etc.     |
| `market_cap`     | DECIMAL(18,2)  | Capitalización de mercado en USD                      | `$1B`, `$100M`, etc.                |

## 📅 `dim_date` — Dimensión de fechas para consultar con diferentes granularidades

En el conjunto de datos actual (completo) tenemos fechas desde el 1.1.2019 hasta el 31.3.2025.

| Nombre de columna  | Tipo         | Descripción                                    | Posibles valores / Notas           |
|--------------------|--------------|------------------------------------------------|------------------------------------|
| `date_id`          | INT          | Clave sustituta de la fecha                     | Primary key                        |
| `date` | DATE         | Fecha real de ejecución de la transacción                                     | `'2024-04-01'`, etc.               |
| `year`             | INT          | Año                                             | `2024`, etc.                       |
| `quarter`          | INT          | Trimestre del año                               | `1`, `2`, `3`, `4`                 |
| `month`            | INT          | Mes del año                                     | `1` a `12`                         |
| `day_of_week`              | INT          | Día de la semana                                | `0` a `6`                          |
| `is_weekend`          | VARCHAR(15)  | Indica si el día es fin de semana                        | `True`, `False`, etc.              |

## 🏛️ `dim_exchange` — Detalles de bolsas de valores
Información sobre las bolsas donde se realizaron las transacciones; se usará más adelante para calcular obligaciones fiscales según el país de la bolsa.
| Nombre de columna | Tipo           | Descripción                                      | Posibles valores / Notas              |
|------------------|----------------|--------------------------------------------------|---------------------------------------|
| `exchange_id`    | INT            | ID único de la bolsa                            | Primary key                            |
| `exchange_name`  | VARCHAR(100)   | Nombre de la bolsa                              | `'NYSE'`, `'NASDAQ'`, `'SGX'`         |
| `country`        | VARCHAR(50)    | País donde se ubica la bolsa                    | `'USA'`, `'Singapore'`, `'UK'`, etc.  |
| `timezone`       | VARCHAR(10)    | Zona horaria local de la bolsa                  | `'EST'`, `'GMT'`, `'SGT'`, etc.       |
| `currency`       | VARCHAR(10)    | Moneda predeterminada de negociación            | `'USD'`, `'SGD'`, `'GBP'`, etc.       |
