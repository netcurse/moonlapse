# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: packets.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rpackets.proto\x12\x0f\x61pp.net.packets\"1\n\x0bLoginPacket\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"4\n\x0eRegisterPacket\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"+\n\nChatPacket\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1c\n\nDenyPacket\x12\x0e\n\x06reason\x18\x01 \x01(\t\"\x1a\n\x08OkPacket\x12\x0e\n\x06reason\x18\x01 \x01(\t\"\x11\n\x0fHeartbeatPacket\"\xae\x02\n\x06Packet\x12-\n\x05login\x18\x01 \x01(\x0b\x32\x1c.app.net.packets.LoginPacketH\x00\x12\x33\n\x08register\x18\x02 \x01(\x0b\x32\x1f.app.net.packets.RegisterPacketH\x00\x12+\n\x04\x63hat\x18\x03 \x01(\x0b\x32\x1b.app.net.packets.ChatPacketH\x00\x12+\n\x04\x64\x65ny\x18\x04 \x01(\x0b\x32\x1b.app.net.packets.DenyPacketH\x00\x12\'\n\x02ok\x18\x05 \x01(\x0b\x32\x19.app.net.packets.OkPacketH\x00\x12\x35\n\theartbeat\x18\x06 \x01(\x0b\x32 .app.net.packets.HeartbeatPacketH\x00\x42\x06\n\x04typeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'packets_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_LOGINPACKET']._serialized_start=34
  _globals['_LOGINPACKET']._serialized_end=83
  _globals['_REGISTERPACKET']._serialized_start=85
  _globals['_REGISTERPACKET']._serialized_end=137
  _globals['_CHATPACKET']._serialized_start=139
  _globals['_CHATPACKET']._serialized_end=182
  _globals['_DENYPACKET']._serialized_start=184
  _globals['_DENYPACKET']._serialized_end=212
  _globals['_OKPACKET']._serialized_start=214
  _globals['_OKPACKET']._serialized_end=240
  _globals['_HEARTBEATPACKET']._serialized_start=242
  _globals['_HEARTBEATPACKET']._serialized_end=259
  _globals['_PACKET']._serialized_start=262
  _globals['_PACKET']._serialized_end=564
# @@protoc_insertion_point(module_scope)
