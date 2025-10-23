create index if not exists idx_process_events_order_stage_created
on process_events(order_id, stage, created_at desc);

create index if not exists idx_vendors_process_types
on vendors(process_types);
