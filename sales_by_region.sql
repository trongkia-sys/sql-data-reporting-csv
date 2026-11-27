SELECT
    customers.region,
    COUNT(*) AS completed_orders,
    SUM(orders.amount_cents) AS revenue_cents
FROM orders
JOIN customers ON customers.id = orders.customer_id
WHERE orders.status = 'completed'
GROUP BY customers.region
ORDER BY revenue_cents DESC, customers.region;
