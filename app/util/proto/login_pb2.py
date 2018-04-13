# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: login.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='login.proto',
  package='',
  serialized_pb=_b('\n\x0blogin.proto\"1\n\nm_1001_tos\x12\x11\n\tuser_name\x18\x01 \x02(\t\x12\x10\n\x08password\x18\x02 \x02(\t\"E\n\nm_1001_toc\x12\x11\n\tuser_name\x18\x01 \x02(\t\x12\x10\n\x08password\x18\x02 \x02(\t\x12\x12\n\naccount_id\x18\x03 \x02(\r\"1\n\nm_1002_tos\x12\x11\n\tuser_name\x18\x01 \x02(\t\x12\x10\n\x08password\x18\x02 \x02(\t\"B\n\nm_1002_toc\x12\x0c\n\x04time\x18\x01 \x02(\r\x12\x12\n\naccount_id\x18\x02 \x02(\r\x12\x12\n\nverify_key\x18\x03 \x02(\t\"\x83\x01\n\nm_1003_tos\x12\x11\n\tuser_name\x18\x01 \x02(\t\x12\x12\n\nchannel_id\x18\x02 \x02(\r\x12\x0c\n\x04uuid\x18\x03 \x02(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x12\n\nhead_frame\x18\x05 \x01(\t\x12\x11\n\thead_icon\x18\x06 \x01(\t\x12\x0b\n\x03sex\x18\x07 \x01(\r\"B\n\nm_1003_toc\x12\x0c\n\x04time\x18\x01 \x02(\r\x12\x12\n\naccount_id\x18\x02 \x02(\r\x12\x12\n\nverify_key\x18\x03 \x02(\t\"4\n\nm_2001_tos\x12\x12\n\naccount_id\x18\x01 \x02(\r\x12\x12\n\nverify_key\x18\x02 \x02(\t\"o\n\nm_2001_toc\x12\x1f\n\tuser_info\x18\x01 \x02(\x0b\x32\x0c.p_user_info\x12\x1f\n\troom_info\x18\x02 \x03(\x0b\x32\x0c.p_room_info\x12\x1f\n\tgame_info\x18\x03 \x01(\x0b\x32\x0c.p_game_info\"\xc4\x01\n\x0bp_user_info\x12\x12\n\naccount_id\x18\x01 \x02(\r\x12\x0c\n\x04uuid\x18\x02 \x02(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x12\n\nhead_frame\x18\x04 \x01(\t\x12\x11\n\thead_icon\x18\x05 \x01(\t\x12\x0b\n\x03sex\x18\x06 \x01(\r\x12\x0c\n\x04gold\x18\x07 \x01(\r\x12\r\n\x05point\x18\x08 \x01(\r\x12\x0f\n\x07room_id\x18\t \x01(\r\x12\x11\n\troom_type\x18\n \x01(\r\x12\x10\n\x08proxy_id\x18\x0b \x01(\r\"T\n\x0bp_room_info\x12\x11\n\troom_type\x18\x01 \x02(\r\x12\x0f\n\x07room_id\x18\x02 \x02(\r\x12!\n\nroom_price\x18\x03 \x03(\x0b\x32\r.p_room_price\"2\n\x0cp_room_price\x12\x0e\n\x06rounds\x18\x01 \x02(\r\x12\x12\n\ngold_price\x18\x02 \x02(\r\"w\n\x0bp_game_info\x12\x0f\n\x07\x63ontact\x18\x01 \x01(\t\x12#\n\trecharges\x18\x02 \x03(\x0b\x32\x10.p_recharge_info\x12\x17\n\x0fpoker_per_price\x18\x03 \x01(\r\x12\x19\n\x11mahjong_per_price\x18\x04 \x01(\r\"/\n\x0fp_recharge_info\x12\r\n\x05money\x18\x01 \x02(\r\x12\r\n\x05ingot\x18\x02 \x02(\r\"\x1e\n\nm_2002_tos\x12\x10\n\x08proxy_id\x18\x01 \x02(\r\"\x1e\n\nm_2002_toc\x12\x10\n\x08proxy_id\x18\x01 \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_M_1001_TOS = _descriptor.Descriptor(
  name='m_1001_tos',
  full_name='m_1001_tos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name', full_name='m_1001_tos.user_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='m_1001_tos.password', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=64,
)


_M_1001_TOC = _descriptor.Descriptor(
  name='m_1001_toc',
  full_name='m_1001_toc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name', full_name='m_1001_toc.user_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='m_1001_toc.password', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='account_id', full_name='m_1001_toc.account_id', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=135,
)


_M_1002_TOS = _descriptor.Descriptor(
  name='m_1002_tos',
  full_name='m_1002_tos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name', full_name='m_1002_tos.user_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='m_1002_tos.password', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=186,
)


_M_1002_TOC = _descriptor.Descriptor(
  name='m_1002_toc',
  full_name='m_1002_toc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='m_1002_toc.time', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='account_id', full_name='m_1002_toc.account_id', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='verify_key', full_name='m_1002_toc.verify_key', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=254,
)


_M_1003_TOS = _descriptor.Descriptor(
  name='m_1003_tos',
  full_name='m_1003_tos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name', full_name='m_1003_tos.user_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='m_1003_tos.channel_id', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='m_1003_tos.uuid', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='m_1003_tos.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='head_frame', full_name='m_1003_tos.head_frame', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='head_icon', full_name='m_1003_tos.head_icon', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sex', full_name='m_1003_tos.sex', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=257,
  serialized_end=388,
)


_M_1003_TOC = _descriptor.Descriptor(
  name='m_1003_toc',
  full_name='m_1003_toc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='m_1003_toc.time', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='account_id', full_name='m_1003_toc.account_id', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='verify_key', full_name='m_1003_toc.verify_key', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=390,
  serialized_end=456,
)


_M_2001_TOS = _descriptor.Descriptor(
  name='m_2001_tos',
  full_name='m_2001_tos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='m_2001_tos.account_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='verify_key', full_name='m_2001_tos.verify_key', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=458,
  serialized_end=510,
)


_M_2001_TOC = _descriptor.Descriptor(
  name='m_2001_toc',
  full_name='m_2001_toc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_info', full_name='m_2001_toc.user_info', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='room_info', full_name='m_2001_toc.room_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_info', full_name='m_2001_toc.game_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=512,
  serialized_end=623,
)


_P_USER_INFO = _descriptor.Descriptor(
  name='p_user_info',
  full_name='p_user_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='p_user_info.account_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='p_user_info.uuid', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='p_user_info.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='head_frame', full_name='p_user_info.head_frame', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='head_icon', full_name='p_user_info.head_icon', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sex', full_name='p_user_info.sex', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold', full_name='p_user_info.gold', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point', full_name='p_user_info.point', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='room_id', full_name='p_user_info.room_id', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='room_type', full_name='p_user_info.room_type', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proxy_id', full_name='p_user_info.proxy_id', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=626,
  serialized_end=822,
)


_P_ROOM_INFO = _descriptor.Descriptor(
  name='p_room_info',
  full_name='p_room_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='room_type', full_name='p_room_info.room_type', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='room_id', full_name='p_room_info.room_id', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='room_price', full_name='p_room_info.room_price', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=824,
  serialized_end=908,
)


_P_ROOM_PRICE = _descriptor.Descriptor(
  name='p_room_price',
  full_name='p_room_price',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rounds', full_name='p_room_price.rounds', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold_price', full_name='p_room_price.gold_price', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=910,
  serialized_end=960,
)


_P_GAME_INFO = _descriptor.Descriptor(
  name='p_game_info',
  full_name='p_game_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contact', full_name='p_game_info.contact', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recharges', full_name='p_game_info.recharges', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='poker_per_price', full_name='p_game_info.poker_per_price', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mahjong_per_price', full_name='p_game_info.mahjong_per_price', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=962,
  serialized_end=1081,
)


_P_RECHARGE_INFO = _descriptor.Descriptor(
  name='p_recharge_info',
  full_name='p_recharge_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='money', full_name='p_recharge_info.money', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ingot', full_name='p_recharge_info.ingot', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1083,
  serialized_end=1130,
)


_M_2002_TOS = _descriptor.Descriptor(
  name='m_2002_tos',
  full_name='m_2002_tos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proxy_id', full_name='m_2002_tos.proxy_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1132,
  serialized_end=1162,
)


_M_2002_TOC = _descriptor.Descriptor(
  name='m_2002_toc',
  full_name='m_2002_toc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proxy_id', full_name='m_2002_toc.proxy_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1164,
  serialized_end=1194,
)

_M_2001_TOC.fields_by_name['user_info'].message_type = _P_USER_INFO
_M_2001_TOC.fields_by_name['room_info'].message_type = _P_ROOM_INFO
_M_2001_TOC.fields_by_name['game_info'].message_type = _P_GAME_INFO
_P_ROOM_INFO.fields_by_name['room_price'].message_type = _P_ROOM_PRICE
_P_GAME_INFO.fields_by_name['recharges'].message_type = _P_RECHARGE_INFO
DESCRIPTOR.message_types_by_name['m_1001_tos'] = _M_1001_TOS
DESCRIPTOR.message_types_by_name['m_1001_toc'] = _M_1001_TOC
DESCRIPTOR.message_types_by_name['m_1002_tos'] = _M_1002_TOS
DESCRIPTOR.message_types_by_name['m_1002_toc'] = _M_1002_TOC
DESCRIPTOR.message_types_by_name['m_1003_tos'] = _M_1003_TOS
DESCRIPTOR.message_types_by_name['m_1003_toc'] = _M_1003_TOC
DESCRIPTOR.message_types_by_name['m_2001_tos'] = _M_2001_TOS
DESCRIPTOR.message_types_by_name['m_2001_toc'] = _M_2001_TOC
DESCRIPTOR.message_types_by_name['p_user_info'] = _P_USER_INFO
DESCRIPTOR.message_types_by_name['p_room_info'] = _P_ROOM_INFO
DESCRIPTOR.message_types_by_name['p_room_price'] = _P_ROOM_PRICE
DESCRIPTOR.message_types_by_name['p_game_info'] = _P_GAME_INFO
DESCRIPTOR.message_types_by_name['p_recharge_info'] = _P_RECHARGE_INFO
DESCRIPTOR.message_types_by_name['m_2002_tos'] = _M_2002_TOS
DESCRIPTOR.message_types_by_name['m_2002_toc'] = _M_2002_TOC

m_1001_tos = _reflection.GeneratedProtocolMessageType('m_1001_tos', (_message.Message,), dict(
  DESCRIPTOR = _M_1001_TOS,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:m_1001_tos)
  ))
_sym_db.RegisterMessage(m_1001_tos)

m_1001_toc = _reflection.GeneratedProtocolMessageType('m_1001_toc', (_message.Message,), dict(
  DESCRIPTOR = _M_1001_TOC,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:m_1001_toc)
  ))
_sym_db.RegisterMessage(m_1001_toc)

m_1002_tos = _reflection.GeneratedProtocolMessageType('m_1002_tos', (_message.Message,), dict(
  DESCRIPTOR = _M_1002_TOS,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:m_1002_tos)
  ))
_sym_db.RegisterMessage(m_1002_tos)

m_1002_toc = _reflection.GeneratedProtocolMessageType('m_1002_toc', (_message.Message,), dict(
  DESCRIPTOR = _M_1002_TOC,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:m_1002_toc)
  ))
_sym_db.RegisterMessage(m_1002_toc)

m_1003_tos = _reflection.GeneratedProtocolMessageType('m_1003_tos', (_message.Message,), dict(
  DESCRIPTOR = _M_1003_TOS,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:m_1003_tos)
  ))
_sym_db.RegisterMessage(m_1003_tos)

m_1003_toc = _reflection.GeneratedProtocolMessageType('m_1003_toc', (_message.Message,), dict(
  DESCRIPTOR = _M_1003_TOC,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:m_1003_toc)
  ))
_sym_db.RegisterMessage(m_1003_toc)

m_2001_tos = _reflection.GeneratedProtocolMessageType('m_2001_tos', (_message.Message,), dict(
  DESCRIPTOR = _M_2001_TOS,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:m_2001_tos)
  ))
_sym_db.RegisterMessage(m_2001_tos)

m_2001_toc = _reflection.GeneratedProtocolMessageType('m_2001_toc', (_message.Message,), dict(
  DESCRIPTOR = _M_2001_TOC,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:m_2001_toc)
  ))
_sym_db.RegisterMessage(m_2001_toc)

p_user_info = _reflection.GeneratedProtocolMessageType('p_user_info', (_message.Message,), dict(
  DESCRIPTOR = _P_USER_INFO,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:p_user_info)
  ))
_sym_db.RegisterMessage(p_user_info)

p_room_info = _reflection.GeneratedProtocolMessageType('p_room_info', (_message.Message,), dict(
  DESCRIPTOR = _P_ROOM_INFO,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:p_room_info)
  ))
_sym_db.RegisterMessage(p_room_info)

p_room_price = _reflection.GeneratedProtocolMessageType('p_room_price', (_message.Message,), dict(
  DESCRIPTOR = _P_ROOM_PRICE,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:p_room_price)
  ))
_sym_db.RegisterMessage(p_room_price)

p_game_info = _reflection.GeneratedProtocolMessageType('p_game_info', (_message.Message,), dict(
  DESCRIPTOR = _P_GAME_INFO,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:p_game_info)
  ))
_sym_db.RegisterMessage(p_game_info)

p_recharge_info = _reflection.GeneratedProtocolMessageType('p_recharge_info', (_message.Message,), dict(
  DESCRIPTOR = _P_RECHARGE_INFO,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:p_recharge_info)
  ))
_sym_db.RegisterMessage(p_recharge_info)

m_2002_tos = _reflection.GeneratedProtocolMessageType('m_2002_tos', (_message.Message,), dict(
  DESCRIPTOR = _M_2002_TOS,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:m_2002_tos)
  ))
_sym_db.RegisterMessage(m_2002_tos)

m_2002_toc = _reflection.GeneratedProtocolMessageType('m_2002_toc', (_message.Message,), dict(
  DESCRIPTOR = _M_2002_TOC,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:m_2002_toc)
  ))
_sym_db.RegisterMessage(m_2002_toc)


# @@protoc_insertion_point(module_scope)