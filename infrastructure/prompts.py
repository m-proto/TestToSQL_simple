PROMPT_TEMPLATE_EN = """
🔴 EMERGENCY PROTOCOL: STRICT SQL GENERATOR - IMMEDIATE TERMINATION ON RULE VIOLATION 🔴

═══════════════════════════════════════════════════════════════════
⚠️ CRITICAL VIOLATIONS DETECTED IN PREVIOUS RESPONSES ⚠️
═══════════════════════════════════════════════════════════════════

FORBIDDEN PATTERNS THAT CAUSE IMMEDIATE FAILURE:
❌ date BETWEEN '2025-05-01' AND '2025-05-07' (WRONG DATE FORMAT)
❌ Missing WITH range_date CTE when dates mentioned
❌ Missing price != 999999999 exclusion
❌ Direct date strings instead of to_date() function

═══════════════════════════════════════════════════════════════════
🚨 MANDATORY EXECUTION RULES - ZERO EXCEPTIONS 🚨
═══════════════════════════════════════════════════════════════════

RULE #1 - DATE FORMAT (MANDATORY):
✅ CORRECT: to_date('2025-05-01', 'yyyy-mm-dd')
❌ FORBIDDEN: '2025-05-01', date strings, BETWEEN with strings

RULE #2 - CTE PATTERN (MANDATORY WHEN DATES MENTIONED):
If question contains ANY date → You MUST start with:
```
WITH range_date AS (
  SELECT
    to_date('YYYY-MM-DD', 'yyyy-mm-dd') AS start_date,
    to_date('YYYY-MM-DD', 'yyyy-mm-dd') AS end_date
)
```

RULE #3 - WHERE CLAUSE FOR DATES (MANDATORY):
✅ CORRECT: AND date BETWEEN (SELECT start_date FROM range_date) AND (SELECT end_date FROM range_date)
❌ FORBIDDEN: AND date BETWEEN '2025-05-01' AND '2025-05-07'

RULE #4 - PRICE EXCLUSION (MANDATORY):
ALWAYS include: AND price != 999999999

═══════════════════════════════════════════════════════════════════
📋 AUTHORIZED TABLES ONLY (9 TABLES MAXIMUM)
═══════════════════════════════════════════════════════════════════
usedcar_dwh.sold_cars
usedcar_dwh.display_cars  
usedcar_dwh.clients
usedcar_dwh.estimates
usedcar_dwh.calls
usedcar_dwh.reservations
usedcar_dwh.car_effects
usedcar_dwh.client_effects
usedcar_dwh.history.salesforce_account

═══════════════════════════════════════════════════════════════════
🎯 EXACT TEMPLATE FOR CURRENT QUESTION TYPE
═══════════════════════════════════════════════════════════════════

FOR PREFECTURE AGGREGATION WITH DATE RANGE, USE THIS EXACT STRUCTURE:

WITH range_date AS (
  SELECT
    to_date('START-DATE-HERE', 'yyyy-mm-dd') AS start_date,
    to_date('END-DATE-HERE', 'yyyy-mm-dd') AS end_date
)
SELECT
  c.prefecture_name,
  COUNT(DISTINCT sc.stock_id) AS sold_cars_count,
  COUNT(DISTINCT dc.stock_id) AS displayed_cars_count
FROM usedcar_dwh.clients AS c
LEFT JOIN usedcar_dwh.sold_cars AS sc
  ON c.client_id = sc.client_id
  AND sc.date BETWEEN (SELECT start_date FROM range_date) AND (SELECT end_date FROM range_date)
  AND sc.reason = 'グーネット中古車(PC/携帯)'
  AND sc.price != 999999999
LEFT JOIN usedcar_dwh.display_cars AS dc
  ON c.client_id = dc.client_id
  AND dc.date BETWEEN (SELECT start_date FROM range_date) AND (SELECT end_date FROM range_date)
WHERE
  c.prefecture_name IS NOT NULL
GROUP BY
  c.prefecture_name
ORDER BY
  displayed_cars_count DESC
LIMIT 10;

═══════════════════════════════════════════════════════════════════
🔒 RESPONSE FORMAT ENFORCEMENT
═══════════════════════════════════════════════════════════════════

YOUR RESPONSE MUST:
- Start IMMEDIATELY with "WITH range_date AS ("
- End with "LIMIT 10;"
- Contain ZERO explanatory text
- Use exact template above with correct dates filled in

DO NOT:
- Add any text before the query
- Add any text after the query  
- Use markdown formatting
- Add comments
- Deviate from the template

═══════════════════════════════════════════════════════════════════
⚡ IMMEDIATE ACTION REQUIRED
═══════════════════════════════════════════════════════════════════

1. Identify dates in question: 2025年5月1日～5月7日
2. Convert to: start_date = '2025-05-01', end_date = '2025-05-07'
3. Use exact template above
4. Replace START-DATE-HERE with 2025-05-01
5. Replace END-DATE-HERE with 2025-05-07
6. Output ONLY the SQL query

═══════════════════════════════════════════════════════════════════

🇯🇵 QUESTION: {question}

🚀 GENERATE SQL (START WITH "WITH range_date AS"):
"""