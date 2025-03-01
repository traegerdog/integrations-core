# (C) Datadog, Inc. 2024-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

METRIC_MAP = {
    'milvus_build_info': {'type': 'metadata', 'label': 'version', 'name': 'version'},
    'milvus_cgo_active_future_total': 'cgo.active_future_total',
    'milvus_cgo_cgo_duration_seconds': 'cgo.cgo_duration_seconds',
    'milvus_cgo_cgo_queue_duration_seconds': 'cgo.cgo_queue_duration_seconds',
    'milvus_cgo_running_cgo_call_total': 'cgo.running_cgo_call_total',
    'milvus_datacoord_channel_checkpoint_unix_seconds': {
        'name': 'datacoord.time_since_channel_checkpoint',
        'type': 'time_elapsed',
    },
    'milvus_datacoord_collection_num': 'datacoord.collection_num',
    'milvus_datacoord_consume_datanode_tt_lag_ms': 'datacoord.consume_datanode_tt_lag_ms',
    'milvus_datacoord_datanode_num': 'datacoord.datanode_num',
    'milvus_datacoord_import_tasks': 'datacoord.import_tasks',
    'milvus_datacoord_index_node_num': 'datacoord.index.node_num',
    'milvus_datacoord_index_req_count': 'datacoord.index.req',
    'milvus_datacoord_index_task_count': 'datacoord.index.task',
    'milvus_datacoord_segment_num': 'datacoord.segment_num',
    'milvus_datacoord_stored_binlog_size': 'datacoord.stored.binlog_size',
    'milvus_datacoord_stored_index_files_size': 'datacoord.stored.index_files_size',
    'milvus_datacoord_stored_rows_num': 'datacoord.stored.rows_num',
    'milvus_datacoord_task_execute_max_latency': 'datacoord.task_execute_max_latency',
    'milvus_datacoord_watched_dml_chanel_num': 'datacoord.watched_dml_chanel_num',
    'milvus_datanode_autoflush_buffer_op_count': 'datanode.autoflush_buffer_op',
    'milvus_datanode_consume_bytes_count': 'datanode.consume.bytes',
    'milvus_datanode_consume_msg_count': 'datanode.consume.msg',
    'milvus_datanode_consume_tt_lag_ms': 'datanode.consume.tt_lag_ms',
    'milvus_datanode_encode_buffer_latency': 'datanode.encode_buffer_latency',
    'milvus_datanode_flowgraph_num': 'datanode.flowgraph_num',
    'milvus_datanode_flush_buffer_op_count': 'datanode.flush.buffer_op',
    'milvus_datanode_flush_req_count': 'datanode.flush.req',
    'milvus_datanode_flushed_data_rows': 'datanode.flushed_data.rows',
    'milvus_datanode_flushed_data_size': 'datanode.flushed_data.size',
    'milvus_datanode_msg_dispatcher_tt_lag_ms': 'datanode.msg.dispatcher_tt_lag_ms',
    'milvus_datanode_msg_rows_count': 'datanode.msg.rows',
    'milvus_datanode_save_latency': 'datanode.save_latency',
    'milvus_flushed_segment_file_num': 'flushed_segment_file_num',
    'milvus_indexnode_build_index_latency': 'indexnode.build_index_latency',
    'milvus_indexnode_encode_index_latency': 'indexnode.encode_index_latency',
    'milvus_indexnode_index_task_count': 'indexnode.index.task',
    'milvus_indexnode_index_task_latency_in_queue': 'indexnode.index.task_latency_in_queue',
    'milvus_indexnode_knowhere_build_index_latency': 'indexnode.knowhere_build_index_latency',
    'milvus_indexnode_save_index_latency': 'indexnode.save_index_latency',
    'milvus_meta_kv_size': 'meta.kv_size',
    'milvus_meta_op_count': 'meta.op',
    'milvus_meta_request_latency': 'meta.request_latency',
    'milvus_msg_queue_consumer_num': 'msg_queue_consumer_num',
    'milvus_msgstream_op_count': 'msgstream.op',
    'milvus_msgstream_request_latency': 'msgstream.request_latency',
    'milvus_num_node': 'num_node',
    'milvus_proxy_apply_pk_latency': 'proxy.apply.pk_latency',
    'milvus_proxy_apply_timestamp_latency': 'proxy.apply.timestamp_latency',
    'milvus_proxy_assign_segmentID_latency': 'proxy.assign_segmentID_latency',
    'milvus_proxy_cache_hit_count': 'proxy.cache.hit',
    'milvus_proxy_cache_update_latency': 'proxy.cache.update_latency',
    'milvus_proxy_delete_vectors_count': 'proxy.delete_vectors',
    'milvus_proxy_msgstream_obj_num': 'proxy.msgstream_obj_num',
    'milvus_proxy_mutation_send_latency': 'proxy.mutation_send_latency',
    'milvus_proxy_rate_limit_req_count': 'proxy.rate_limit_req',
    'milvus_proxy_report_value': 'proxy.report_value',
    'milvus_proxy_req_count': 'proxy.req',
    'milvus_proxy_req_in_queue_latency': 'proxy.req.in_queue_latency',
    'milvus_proxy_req_latency': 'proxy.req.latency',
    'milvus_proxy_send_bytes_count': 'proxy.send_bytes',
    'milvus_proxy_sq_decode_result_latency': 'proxy.sq.decode_result_latency',
    'milvus_proxy_sq_reduce_result_latency': 'proxy.sq.reduce_result_latency',
    'milvus_proxy_sq_wait_result_latency': 'proxy.sq.wait_result_latency',
    'milvus_proxy_sync_segment_request_length': 'proxy.sync_segment_request_length',
    'milvus_proxy_tt_lag_ms': 'proxy.tt_lag_ms',
    'milvus_querycoord_collection_num': 'querycoord.collection_num',
    'milvus_querycoord_current_target_checkpoint_unix_seconds': {
        'name': 'querycoord.current_target_checkpoint_unix_seconds',
        'type': 'time_elapsed',
    },
    'milvus_querycoord_load_latency': 'querycoord.load.latency',
    'milvus_querycoord_load_req_count': 'querycoord.load.req',
    'milvus_querycoord_partition_num': 'querycoord.partition_num',
    'milvus_querycoord_querynode_num': 'querycoord.querynode_num',
    'milvus_querycoord_release_latency': 'querycoord.release.latency',
    'milvus_querycoord_release_req_count': 'querycoord.release.req',
    'milvus_querycoord_task_num': 'querycoord_task_num',
    'milvus_querynode_apply_bf_latency': 'querynode.apply_bf_latency',
    'milvus_querynode_collection_num': 'querynode.collection_num',
    'milvus_querynode_consume_bytes_counter': 'querynode.consume.bytes_counter',
    'milvus_querynode_consume_msg_count': 'querynode.consume.msg',
    'milvus_querynode_consume_tt_lag_ms': 'querynode.consume.tt_lag_ms',
    'milvus_querynode_disk_cache_evict_bytes': 'querynode.disk.cache.evict.bytes',
    'milvus_querynode_disk_cache_evict_duration': 'querynode.disk.cache.evict.duration',
    'milvus_querynode_disk_cache_evict_global_duration': 'querynode.disk.cache.evict.global_duration',
    'milvus_querynode_disk_cache_evict': 'querynode.disk.cache.evict',
    'milvus_querynode_disk_cache_load_bytes': 'querynode.disk.cache.load.bytes',
    'milvus_querynode_disk_cache_load_duration': 'querynode.disk.cache.load.duration',
    'milvus_querynode_disk_cache_load_global_duration': 'querynode.disk.cache.load.global_duration',
    'milvus_querynode_disk_cache_load': 'querynode.disk.cache.load',
    'milvus_querynode_disk_used_size': 'querynode.disk.used_size',
    'milvus_querynode_dml_vchannel_num': 'querynode.dml_vchannel_num',
    'milvus_querynode_entity_num': 'querynode.entity.num',
    'milvus_querynode_entity_size': 'querynode.entity.size',
    'milvus_querynode_execute_bytes_counter': 'querynode.execute_bytes_counter',
    'milvus_querynode_flowgraph_num': 'querynode.flowgraph_num',
    'milvus_querynode_forward_delete_latency': 'querynode.forward_delete_latency',
    'milvus_querynode_load_index_latency': 'querynode.load.index_latency',
    'milvus_querynode_load_segment_concurrency': 'querynode.load.segment.concurrency',
    'milvus_querynode_load_segment_latency': 'querynode.load.segment.latency',
    'milvus_querynode_msg_dispatcher_tt_lag_ms': 'querynode.msg_dispatcher_tt_lag_ms',
    'milvus_querynode_partition_num': 'querynode.partition_num',
    'milvus_querynode_process_insert_or_delete_latency': 'querynode.process_insert_or_delete_latency',
    'milvus_querynode_read_task_concurrency': 'querynode.read_task.concurrency',
    'milvus_querynode_read_task_ready_len': 'querynode.read_task.ready_len',
    'milvus_querynode_read_task_unsolved_len': 'querynode.read_task.unsolved_len',
    'milvus_querynode_search_group_nq': 'querynode.search.group.nq',
    'milvus_querynode_search_group_size': 'querynode.search.group.size',
    'milvus_querynode_search_group_topk': 'querynode.search.group.topk',
    'milvus_querynode_search_nq': 'querynode.search.nq',
    'milvus_querynode_search_topk': 'querynode.search.topk',
    'milvus_querynode_segment_access_duration': 'querynode.segment.access.duration',
    'milvus_querynode_segment_access_global_duration': 'querynode.segment.access.global_duration',
    'milvus_querynode_segment_access': 'querynode.segment.access',
    'milvus_querynode_segment_access_wait_cache_duration': 'querynode.segment.access.wait_cache.duration',
    'milvus_querynode_segment_access_wait_cache_global_duration': 'querynode.segment.access.wait_cache.global_duration',
    'milvus_querynode_segment_access_wait_cache': 'querynode.segment.access.wait_cache',
    'milvus_querynode_segment_latency_per_vector': 'querynode.segment.latency_per_vector',
    'milvus_querynode_segment_num': 'querynode.segment.num',
    'milvus_querynode_sq_core_latency': 'querynode.sq.core_latency',
    'milvus_querynode_sq_queue_latency': 'querynode.sq.queue.latency',
    'milvus_querynode_sq_queue_user_latency': 'querynode.sq.queue.user_latency',
    'milvus_querynode_sq_reduce_latency': 'querynode.sq.reduce_latency',
    'milvus_querynode_sq_req_count': 'querynode.sq.req',
    'milvus_querynode_sq_req_latency': 'querynode.sq.req.latency',
    'milvus_querynode_sq_segment_latency': 'querynode.sq.segment_latency',
    'milvus_querynode_sq_wait_tsafe_latency': 'querynode.sq.wait_tsafe_latency',
    'milvus_querynode_wait_processing_msg_count': 'querynode.wait_processing_msg',
    'milvus_querynode_watch_dml_channel_latency': 'querynode.watch_dml_channel_latency',
    'milvus_rootcoord_collection_num': 'rootcoord.collection_num',
    'milvus_rootcoord_credential_num': 'rootcoord.credential_num',
    'milvus_rootcoord_ddl_req_count': 'rootcoord.ddl_req',
    'milvus_rootcoord_ddl_req_latency': 'rootcoord.ddl_req.latency',
    'milvus_rootcoord_ddl_req_latency_in_queue': 'rootcoord.ddl_req.latency_in_queue',
    'milvus_rootcoord_dml_channel_num': 'rootcoord.dml_channel_num',
    'milvus_rootcoord_entity_num': 'rootcoord.entity_num',
    'milvus_rootcoord_force_deny_writing_counter': 'rootcoord.force_deny_writing_counter',
    'milvus_rootcoord_id_alloc_count': 'rootcoord.id_alloc',
    'milvus_rootcoord_indexed_entity_num': 'rootcoord.indexed_entity_num',
    'milvus_rootcoord_msgstream_obj_num': 'rootcoord.msgstream_obj_num',
    'milvus_rootcoord_num_of_roles': 'rootcoord.num_of_roles',
    'milvus_rootcoord_partition_num': 'rootcoord.partition_num',
    'milvus_rootcoord_produce_tt_lag_ms': 'rootcoord.produce_tt_lag_ms',
    'milvus_rootcoord_proxy_num': 'rootcoord.proxy_num',
    'milvus_rootcoord_qn_mem_high_water_level': 'rootcoord.qn_mem_high_water_level',
    'milvus_rootcoord_sync_timetick_latency': 'rootcoord.sync_timetick_latency',
    'milvus_rootcoord_timestamp': 'rootcoord.timestamp',
    'milvus_rootcoord_timestamp_saved': 'rootcoord.timestamp_saved',
    'milvus_runtime_info': 'runtime_info',
    'milvus_storage_kv_size': 'storage.kv_size',
    'milvus_storage_op_count': 'storage.op',
    'milvus_storage_request_latency': 'storage.request_latency',
    'bf_search_cnt': 'bf_search_cnt',
    'bitset_ratio': 'bitset_ratio',
    'build_latency': 'build_latency',
    'cache_hit_cnt': 'cache_hit_cnt',
    'diskann_range_search_iters': 'diskann.range_search_iters',
    'diskann_search_hops': 'diskann.search_hops',
    'diskann_bitset_ratio': 'diskann_bitset_ratio',
    'exec_latency': 'exec_latency',
    'filter_connectivity_ratio': 'filter.connectivity_ratio',
    'filter_mv_activated_fields_cnt': 'filter.mv.activated_fields_cnt',
    'filter_mv_change_base_cnt': 'filter.mv.change_base_cnt',
    'filter_mv_only_cnt': 'filter.mv.only_cnt',
    'filter_mv_supplement_ep_bool_cnt': 'filter.mv.supplement_ep_bool_cnt',
    'go_gc_duration_seconds': 'go.gc_duration_seconds',
    'go_goroutines': 'go.goroutines',
    'go_info': 'go.info',
    'go_memstats_alloc_bytes': {'name': 'go.memstats.alloc_bytes', 'type': 'native_dynamic'},
    'go_memstats_buck_hash_sys_bytes': 'go.memstats.buck_hash_sys_bytes',
    'go_memstats_frees': 'go.memstats.frees',
    'go_memstats_gc_sys_bytes': 'go.memstats.gc_sys_bytes',
    'go_memstats_heap_alloc_bytes': 'go.memstats.heap.alloc_bytes',
    'go_memstats_heap_idle_bytes': 'go.memstats.heap.idle_bytes',
    'go_memstats_heap_inuse_bytes': 'go.memstats.heap.inuse_bytes',
    'go_memstats_heap_objects': 'go.memstats.heap.objects',
    'go_memstats_heap_released_bytes': 'go.memstats.heap.released_bytes',
    'go_memstats_heap_sys_bytes': 'go.memstats.heap.sys_bytes',
    'go_memstats_last_gc_time_seconds': 'go.memstats.last_gc_time_seconds',
    'go_memstats_lookups': 'go.memstats.lookups',
    'go_memstats_mallocs': 'go.memstats.mallocs',
    'go_memstats_mcache_inuse_bytes': 'go.memstats.mcache.inuse_bytes',
    'go_memstats_mcache_sys_bytes': 'go.memstats.mcache.sys_bytes',
    'go_memstats_mspan_inuse_bytes': 'go.memstats.mspan.inuse_bytes',
    'go_memstats_mspan_sys_bytes': 'go.memstats.mspan.sys_bytes',
    'go_memstats_next_gc_bytes': 'go.memstats.next_gc_bytes',
    'go_memstats_other_sys_bytes': 'go.memstats.other_sys_bytes',
    'go_memstats_stack_inuse_bytes': 'go.memstats.stack.inuse_bytes',
    'go_memstats_stack_sys_bytes': 'go.memstats.stack.sys_bytes',
    'go_memstats_sys_bytes': 'go.memstats.sys_bytes',
    'go_threads': 'go.threads',
    'graph_search_cnt': 'graph_search_cnt',
    'hnsw_bitset_ratio': 'hnsw.bitset_ratio',
    'hnsw_search_hops': 'hnsw.search_hops',
    'internal_core_search_latency': 'internal.core_search_latency',
    'internal_mmap_allocated_space_bytes': 'internal.mmap.allocated_space_bytes',
    'internal_mmap_in_used_space_bytes': 'internal.mmap.in_used_space_bytes',
    'internal_storage_kv_size': 'internal.storage.kv_size',
    'internal_storage_load_duration': 'internal.storage.load_duration',
    'internal_storage_op_count': 'internal.storage.op',
    'internal_storage_request_latency': 'internal.storage.request_latency',
    'io_cnt': 'io_cnt',
    'ivf_search_cnt': 'ivf_search_cnt',
    'load_latency': 'load_latency',
    'process_cpu_seconds': 'process.cpu_seconds',
    'process_max_fds': 'process.max_fds',
    'process_open_fds': 'process.open_fds',
    'process_resident_memory_bytes': 'process.resident_memory_bytes',
    'process_start_time_seconds': {'name': 'process.start_time_seconds', 'type': 'time_elapsed'},
    'process_virtual_memory_bytes': 'process.virtual_memory.bytes',
    'process_virtual_memory_max_bytes': 'process.virtual_memory.max_bytes',
    'quant_compute_cnt': 'quant.compute_cnt',
    'queue_latency': 'queue.latency',
    'range_search_latency': 'range_search_latency',
    'raw_compute_cnt': 'raw_compute_cnt',
    're_search_cnt': 're_search_cnt',
    'search_latency': 'search.latency',
    'search_topk': 'search.topk',
}

RENAME_LABELS_MAP = {
    'version': 'milvus_version',
}
