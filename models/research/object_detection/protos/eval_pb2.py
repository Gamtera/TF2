# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/eval.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"object_detection/protos/eval.proto\x12\x17object_detection.protos\"\xdf\n\n\nEvalConfig\x12\x15\n\nbatch_size\x18\x19 \x01(\r:\x01\x31\x12\x1e\n\x12num_visualizations\x18\x01 \x01(\r:\x02\x31\x30\x12\x1e\n\x0cnum_examples\x18\x02 \x01(\r:\x04\x35\x30\x30\x30\x42\x02\x18\x01\x12\x1f\n\x12\x65val_interval_secs\x18\x03 \x01(\r:\x03\x33\x30\x30\x12\x18\n\tmax_evals\x18\x04 \x01(\r:\x01\x30\x42\x02\x18\x01\x12\x19\n\nsave_graph\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\"\n\x18visualization_export_dir\x18\x06 \x01(\t:\x00\x12\x15\n\x0b\x65val_master\x18\x07 \x01(\t:\x00\x12\x13\n\x0bmetrics_set\x18\x08 \x03(\t\x12J\n\x14parameterized_metric\x18\x1f \x03(\x0b\x32,.object_detection.protos.ParameterizedMetric\x12\x15\n\x0b\x65xport_path\x18\t \x01(\t:\x00\x12!\n\x12ignore_groundtruth\x18\n \x01(\x08:\x05\x66\x61lse\x12\"\n\x13use_moving_averages\x18\x0b \x01(\x08:\x05\x66\x61lse\x12\"\n\x13\x65val_instance_masks\x18\x0c \x01(\x08:\x05\x66\x61lse\x12 \n\x13min_score_threshold\x18\r \x01(\x02:\x03\x30.5\x12&\n\x1amax_num_boxes_to_visualize\x18\x0e \x01(\x05:\x02\x32\x30\x12\x1a\n\x0bskip_scores\x18\x0f \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x0bskip_labels\x18\x10 \x01(\x08:\x05\x66\x61lse\x12*\n\x1bvisualize_groundtruth_boxes\x18\x11 \x01(\x08:\x05\x66\x61lse\x12\x32\n#groundtruth_box_visualization_color\x18\x12 \x01(\t:\x05\x62lack\x12\x35\n&keep_image_id_for_visualization_export\x18\x13 \x01(\x08:\x05\x66\x61lse\x12$\n\x16retain_original_images\x18\x17 \x01(\x08:\x04true\x12+\n\x1cinclude_metrics_per_category\x18\x18 \x01(\x08:\x05\x66\x61lse\x12\'\n\x18\x61ll_metrics_per_category\x18# \x01(\x08:\x05\x66\x61lse\x12R\n\x10super_categories\x18\" \x03(\x0b\x32\x38.object_detection.protos.EvalConfig.SuperCategoriesEntry\x12\x1d\n\x12recall_lower_bound\x18\x1a \x01(\x02:\x01\x30\x12\x1d\n\x12recall_upper_bound\x18\x1b \x01(\x02:\x01\x31\x12\x38\n)retain_original_image_additional_channels\x18\x1c \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x0f\x66orce_no_resize\x18\x1d \x01(\x08:\x05\x66\x61lse\x12%\n\x16use_dummy_loss_in_eval\x18\x1e \x01(\x08:\x05\x66\x61lse\x12<\n\rkeypoint_edge\x18  \x03(\x0b\x32%.object_detection.protos.KeypointEdge\x12\x33\n$skip_predictions_for_unlabeled_class\x18! \x01(\x08:\x05\x66\x61lse\x12\x33\n%image_classes_field_map_empty_to_ones\x18$ \x01(\x08:\x04true\x1a\x36\n\x14SuperCategoriesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"|\n\x13ParameterizedMetric\x12M\n\x15\x63oco_keypoint_metrics\x18\x01 \x01(\x0b\x32,.object_detection.protos.CocoKeypointMetricsH\x00\x42\x16\n\x14parameterized_metric\"\xd3\x01\n\x13\x43ocoKeypointMetrics\x12\x13\n\x0b\x63lass_label\x18\x01 \x01(\t\x12i\n\x18keypoint_label_to_sigmas\x18\x02 \x03(\x0b\x32G.object_detection.protos.CocoKeypointMetrics.KeypointLabelToSigmasEntry\x1a<\n\x1aKeypointLabelToSigmasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\"*\n\x0cKeypointEdge\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x05')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'object_detection.protos.eval_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EVALCONFIG_SUPERCATEGORIESENTRY']._options = None
  _globals['_EVALCONFIG_SUPERCATEGORIESENTRY']._serialized_options = b'8\001'
  _globals['_EVALCONFIG'].fields_by_name['num_examples']._options = None
  _globals['_EVALCONFIG'].fields_by_name['num_examples']._serialized_options = b'\030\001'
  _globals['_EVALCONFIG'].fields_by_name['max_evals']._options = None
  _globals['_EVALCONFIG'].fields_by_name['max_evals']._serialized_options = b'\030\001'
  _globals['_COCOKEYPOINTMETRICS_KEYPOINTLABELTOSIGMASENTRY']._options = None
  _globals['_COCOKEYPOINTMETRICS_KEYPOINTLABELTOSIGMASENTRY']._serialized_options = b'8\001'
  _globals['_EVALCONFIG']._serialized_start=64
  _globals['_EVALCONFIG']._serialized_end=1439
  _globals['_EVALCONFIG_SUPERCATEGORIESENTRY']._serialized_start=1385
  _globals['_EVALCONFIG_SUPERCATEGORIESENTRY']._serialized_end=1439
  _globals['_PARAMETERIZEDMETRIC']._serialized_start=1441
  _globals['_PARAMETERIZEDMETRIC']._serialized_end=1565
  _globals['_COCOKEYPOINTMETRICS']._serialized_start=1568
  _globals['_COCOKEYPOINTMETRICS']._serialized_end=1779
  _globals['_COCOKEYPOINTMETRICS_KEYPOINTLABELTOSIGMASENTRY']._serialized_start=1719
  _globals['_COCOKEYPOINTMETRICS_KEYPOINTLABELTOSIGMASENTRY']._serialized_end=1779
  _globals['_KEYPOINTEDGE']._serialized_start=1781
  _globals['_KEYPOINTEDGE']._serialized_end=1823
# @@protoc_insertion_point(module_scope)
