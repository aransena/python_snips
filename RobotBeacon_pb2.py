# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RobotBeacon.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import Time_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='RobotBeacon.proto',
  package='roah_rsbb_msgs',
  serialized_pb='\n\x11RobotBeacon.proto\x12\x0eroah_rsbb_msgs\x1a\nTime.proto\"\x80\x01\n\x0bRobotBeacon\x12\x11\n\tteam_name\x18\x01 \x02(\t\x12\x12\n\nrobot_name\x18\x02 \x02(\t\x12\"\n\x04time\x18\x03 \x02(\x0b\x32\x14.roah_rsbb_msgs.Time\"&\n\x08\x43ompType\x12\x0c\n\x07\x43OMP_ID\x10\x8a\x34\x12\x0c\n\x08MSG_TYPE\x10\x1e\x42-\n\x18\x65u.rockin.roah_rsbb_msgsB\x11RobotBeaconProtos')



_ROBOTBEACON_COMPTYPE = _descriptor.EnumDescriptor(
  name='CompType',
  full_name='roah_rsbb_msgs.RobotBeacon.CompType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COMP_ID', index=0, number=6666,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSG_TYPE', index=1, number=30,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=140,
  serialized_end=178,
)


_ROBOTBEACON = _descriptor.Descriptor(
  name='RobotBeacon',
  full_name='roah_rsbb_msgs.RobotBeacon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='team_name', full_name='roah_rsbb_msgs.RobotBeacon.team_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='robot_name', full_name='roah_rsbb_msgs.RobotBeacon.robot_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='roah_rsbb_msgs.RobotBeacon.time', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ROBOTBEACON_COMPTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=50,
  serialized_end=178,
)

_ROBOTBEACON.fields_by_name['time'].message_type = Time_pb2._TIME
_ROBOTBEACON_COMPTYPE.containing_type = _ROBOTBEACON;
DESCRIPTOR.message_types_by_name['RobotBeacon'] = _ROBOTBEACON

class RobotBeacon(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROBOTBEACON

  # @@protoc_insertion_point(class_scope:roah_rsbb_msgs.RobotBeacon)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\030eu.rockin.roah_rsbb_msgsB\021RobotBeaconProtos')
# @@protoc_insertion_point(module_scope)