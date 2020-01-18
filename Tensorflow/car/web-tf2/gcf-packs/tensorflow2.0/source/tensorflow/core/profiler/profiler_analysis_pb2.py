# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/profiler/profiler_analysis.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.profiler import profiler_service_pb2 as tensorflow_dot_core_dot_profiler_dot_profiler__service__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/profiler/profiler_analysis.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n0tensorflow/core/profiler/profiler_analysis.proto\x12\ntensorflow\x1a/tensorflow/core/profiler/profiler_service.proto\"\x83\x01\n\x18NewProfileSessionRequest\x12+\n\x07request\x18\x01 \x01(\x0b\x32\x1a.tensorflow.ProfileRequest\x12\x17\n\x0frepository_root\x18\x02 \x01(\t\x12\r\n\x05hosts\x18\x03 \x03(\t\x12\x12\n\nsession_id\x18\x04 \x01(\t\"G\n\x19NewProfileSessionResponse\x12\x15\n\rerror_message\x18\x01 \x01(\t\x12\x13\n\x0b\x65mpty_trace\x18\x02 \x01(\x08\"=\n\"EnumProfileSessionsAndToolsRequest\x12\x17\n\x0frepository_root\x18\x01 \x01(\t\"A\n\x12ProfileSessionInfo\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x17\n\x0f\x61vailable_tools\x18\x02 \x03(\t\"n\n#EnumProfileSessionsAndToolsResponse\x12\x15\n\rerror_message\x18\x01 \x01(\t\x12\x30\n\x08sessions\x18\x02 \x03(\x0b\x32\x1e.tensorflow.ProfileSessionInfo\"\xec\x01\n\x19ProfileSessionDataRequest\x12\x17\n\x0frepository_root\x18\x01 \x01(\t\x12\x12\n\nsession_id\x18\x02 \x01(\t\x12\x11\n\thost_name\x18\x05 \x01(\t\x12\x11\n\ttool_name\x18\x03 \x01(\t\x12I\n\nparameters\x18\x04 \x03(\x0b\x32\x35.tensorflow.ProfileSessionDataRequest.ParametersEntry\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"Z\n\x1aProfileSessionDataResponse\x12\x15\n\rerror_message\x18\x01 \x01(\t\x12\x15\n\routput_format\x18\x02 \x01(\t\x12\x0e\n\x06output\x18\x03 \x01(\x0c\x32\xc8\x02\n\x0fProfileAnalysis\x12[\n\nNewSession\x12$.tensorflow.NewProfileSessionRequest\x1a%.tensorflow.NewProfileSessionResponse\"\x00\x12q\n\x0c\x45numSessions\x12..tensorflow.EnumProfileSessionsAndToolsRequest\x1a/.tensorflow.EnumProfileSessionsAndToolsResponse\"\x00\x12\x65\n\x12GetSessionToolData\x12%.tensorflow.ProfileSessionDataRequest\x1a&.tensorflow.ProfileSessionDataResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[tensorflow_dot_core_dot_profiler_dot_profiler__service__pb2.DESCRIPTOR,])




_NEWPROFILESESSIONREQUEST = _descriptor.Descriptor(
  name='NewProfileSessionRequest',
  full_name='tensorflow.NewProfileSessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='tensorflow.NewProfileSessionRequest.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repository_root', full_name='tensorflow.NewProfileSessionRequest.repository_root', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hosts', full_name='tensorflow.NewProfileSessionRequest.hosts', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='tensorflow.NewProfileSessionRequest.session_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=245,
)


_NEWPROFILESESSIONRESPONSE = _descriptor.Descriptor(
  name='NewProfileSessionResponse',
  full_name='tensorflow.NewProfileSessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_message', full_name='tensorflow.NewProfileSessionResponse.error_message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='empty_trace', full_name='tensorflow.NewProfileSessionResponse.empty_trace', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=247,
  serialized_end=318,
)


_ENUMPROFILESESSIONSANDTOOLSREQUEST = _descriptor.Descriptor(
  name='EnumProfileSessionsAndToolsRequest',
  full_name='tensorflow.EnumProfileSessionsAndToolsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repository_root', full_name='tensorflow.EnumProfileSessionsAndToolsRequest.repository_root', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=320,
  serialized_end=381,
)


_PROFILESESSIONINFO = _descriptor.Descriptor(
  name='ProfileSessionInfo',
  full_name='tensorflow.ProfileSessionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='tensorflow.ProfileSessionInfo.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='available_tools', full_name='tensorflow.ProfileSessionInfo.available_tools', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=383,
  serialized_end=448,
)


_ENUMPROFILESESSIONSANDTOOLSRESPONSE = _descriptor.Descriptor(
  name='EnumProfileSessionsAndToolsResponse',
  full_name='tensorflow.EnumProfileSessionsAndToolsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_message', full_name='tensorflow.EnumProfileSessionsAndToolsResponse.error_message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sessions', full_name='tensorflow.EnumProfileSessionsAndToolsResponse.sessions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=450,
  serialized_end=560,
)


_PROFILESESSIONDATAREQUEST_PARAMETERSENTRY = _descriptor.Descriptor(
  name='ParametersEntry',
  full_name='tensorflow.ProfileSessionDataRequest.ParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.ProfileSessionDataRequest.ParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.ProfileSessionDataRequest.ParametersEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=750,
  serialized_end=799,
)

_PROFILESESSIONDATAREQUEST = _descriptor.Descriptor(
  name='ProfileSessionDataRequest',
  full_name='tensorflow.ProfileSessionDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repository_root', full_name='tensorflow.ProfileSessionDataRequest.repository_root', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='tensorflow.ProfileSessionDataRequest.session_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host_name', full_name='tensorflow.ProfileSessionDataRequest.host_name', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tool_name', full_name='tensorflow.ProfileSessionDataRequest.tool_name', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='tensorflow.ProfileSessionDataRequest.parameters', index=4,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PROFILESESSIONDATAREQUEST_PARAMETERSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=563,
  serialized_end=799,
)


_PROFILESESSIONDATARESPONSE = _descriptor.Descriptor(
  name='ProfileSessionDataResponse',
  full_name='tensorflow.ProfileSessionDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_message', full_name='tensorflow.ProfileSessionDataResponse.error_message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_format', full_name='tensorflow.ProfileSessionDataResponse.output_format', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output', full_name='tensorflow.ProfileSessionDataResponse.output', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=801,
  serialized_end=891,
)

_NEWPROFILESESSIONREQUEST.fields_by_name['request'].message_type = tensorflow_dot_core_dot_profiler_dot_profiler__service__pb2._PROFILEREQUEST
_ENUMPROFILESESSIONSANDTOOLSRESPONSE.fields_by_name['sessions'].message_type = _PROFILESESSIONINFO
_PROFILESESSIONDATAREQUEST_PARAMETERSENTRY.containing_type = _PROFILESESSIONDATAREQUEST
_PROFILESESSIONDATAREQUEST.fields_by_name['parameters'].message_type = _PROFILESESSIONDATAREQUEST_PARAMETERSENTRY
DESCRIPTOR.message_types_by_name['NewProfileSessionRequest'] = _NEWPROFILESESSIONREQUEST
DESCRIPTOR.message_types_by_name['NewProfileSessionResponse'] = _NEWPROFILESESSIONRESPONSE
DESCRIPTOR.message_types_by_name['EnumProfileSessionsAndToolsRequest'] = _ENUMPROFILESESSIONSANDTOOLSREQUEST
DESCRIPTOR.message_types_by_name['ProfileSessionInfo'] = _PROFILESESSIONINFO
DESCRIPTOR.message_types_by_name['EnumProfileSessionsAndToolsResponse'] = _ENUMPROFILESESSIONSANDTOOLSRESPONSE
DESCRIPTOR.message_types_by_name['ProfileSessionDataRequest'] = _PROFILESESSIONDATAREQUEST
DESCRIPTOR.message_types_by_name['ProfileSessionDataResponse'] = _PROFILESESSIONDATARESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NewProfileSessionRequest = _reflection.GeneratedProtocolMessageType('NewProfileSessionRequest', (_message.Message,), dict(
  DESCRIPTOR = _NEWPROFILESESSIONREQUEST,
  __module__ = 'tensorflow.core.profiler.profiler_analysis_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.NewProfileSessionRequest)
  ))
_sym_db.RegisterMessage(NewProfileSessionRequest)

NewProfileSessionResponse = _reflection.GeneratedProtocolMessageType('NewProfileSessionResponse', (_message.Message,), dict(
  DESCRIPTOR = _NEWPROFILESESSIONRESPONSE,
  __module__ = 'tensorflow.core.profiler.profiler_analysis_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.NewProfileSessionResponse)
  ))
_sym_db.RegisterMessage(NewProfileSessionResponse)

EnumProfileSessionsAndToolsRequest = _reflection.GeneratedProtocolMessageType('EnumProfileSessionsAndToolsRequest', (_message.Message,), dict(
  DESCRIPTOR = _ENUMPROFILESESSIONSANDTOOLSREQUEST,
  __module__ = 'tensorflow.core.profiler.profiler_analysis_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.EnumProfileSessionsAndToolsRequest)
  ))
_sym_db.RegisterMessage(EnumProfileSessionsAndToolsRequest)

ProfileSessionInfo = _reflection.GeneratedProtocolMessageType('ProfileSessionInfo', (_message.Message,), dict(
  DESCRIPTOR = _PROFILESESSIONINFO,
  __module__ = 'tensorflow.core.profiler.profiler_analysis_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.ProfileSessionInfo)
  ))
_sym_db.RegisterMessage(ProfileSessionInfo)

EnumProfileSessionsAndToolsResponse = _reflection.GeneratedProtocolMessageType('EnumProfileSessionsAndToolsResponse', (_message.Message,), dict(
  DESCRIPTOR = _ENUMPROFILESESSIONSANDTOOLSRESPONSE,
  __module__ = 'tensorflow.core.profiler.profiler_analysis_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.EnumProfileSessionsAndToolsResponse)
  ))
_sym_db.RegisterMessage(EnumProfileSessionsAndToolsResponse)

ProfileSessionDataRequest = _reflection.GeneratedProtocolMessageType('ProfileSessionDataRequest', (_message.Message,), dict(

  ParametersEntry = _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), dict(
    DESCRIPTOR = _PROFILESESSIONDATAREQUEST_PARAMETERSENTRY,
    __module__ = 'tensorflow.core.profiler.profiler_analysis_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.ProfileSessionDataRequest.ParametersEntry)
    ))
  ,
  DESCRIPTOR = _PROFILESESSIONDATAREQUEST,
  __module__ = 'tensorflow.core.profiler.profiler_analysis_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.ProfileSessionDataRequest)
  ))
_sym_db.RegisterMessage(ProfileSessionDataRequest)
_sym_db.RegisterMessage(ProfileSessionDataRequest.ParametersEntry)

ProfileSessionDataResponse = _reflection.GeneratedProtocolMessageType('ProfileSessionDataResponse', (_message.Message,), dict(
  DESCRIPTOR = _PROFILESESSIONDATARESPONSE,
  __module__ = 'tensorflow.core.profiler.profiler_analysis_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.ProfileSessionDataResponse)
  ))
_sym_db.RegisterMessage(ProfileSessionDataResponse)


_PROFILESESSIONDATAREQUEST_PARAMETERSENTRY._options = None

_PROFILEANALYSIS = _descriptor.ServiceDescriptor(
  name='ProfileAnalysis',
  full_name='tensorflow.ProfileAnalysis',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=894,
  serialized_end=1222,
  methods=[
  _descriptor.MethodDescriptor(
    name='NewSession',
    full_name='tensorflow.ProfileAnalysis.NewSession',
    index=0,
    containing_service=None,
    input_type=_NEWPROFILESESSIONREQUEST,
    output_type=_NEWPROFILESESSIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='EnumSessions',
    full_name='tensorflow.ProfileAnalysis.EnumSessions',
    index=1,
    containing_service=None,
    input_type=_ENUMPROFILESESSIONSANDTOOLSREQUEST,
    output_type=_ENUMPROFILESESSIONSANDTOOLSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetSessionToolData',
    full_name='tensorflow.ProfileAnalysis.GetSessionToolData',
    index=2,
    containing_service=None,
    input_type=_PROFILESESSIONDATAREQUEST,
    output_type=_PROFILESESSIONDATARESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROFILEANALYSIS)

DESCRIPTOR.services_by_name['ProfileAnalysis'] = _PROFILEANALYSIS

# @@protoc_insertion_point(module_scope)