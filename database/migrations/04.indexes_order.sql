SELECT 
    tablename,
    indexname
FROM pg_indexes
WHERE tablename IN ('orders', 'process_events', 'projects')
ORDER BY tablename, indexname;