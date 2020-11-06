/**
 * @fileoverview
 * @enhanceable
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!

var jspb = require('google-protobuf');
var goog = jspb;
var global = Function('return this')();

var google_api_annotations_pb = require('../../../google/api/annotations_pb.js');
goog.exportSymbol('proto.api.EnqueueDeviceQueueActilityItemRequest', null, global);
goog.exportSymbol('proto.api.EnqueueDeviceQueueActilityItemResponse', null, global);

/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.api.EnqueueDeviceQueueActilityItemRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.api.EnqueueDeviceQueueActilityItemRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.api.EnqueueDeviceQueueActilityItemRequest.displayName = 'proto.api.EnqueueDeviceQueueActilityItemRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.api.EnqueueDeviceQueueActilityItemRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.api.EnqueueDeviceQueueActilityItemRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.api.EnqueueDeviceQueueActilityItemRequest} msg The msg instance to transform.
 * @return {!Object}
 */
proto.api.EnqueueDeviceQueueActilityItemRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    devEui: msg.getDevEui(),
    confirmDownlink: msg.getConfirmDownlink(),
    flushDownlinkQueue: msg.getFlushDownlinkQueue(),
    payloadHex: msg.getPayloadHex(),
    targetPorts: msg.getTargetPorts()
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.api.EnqueueDeviceQueueActilityItemRequest}
 */
proto.api.EnqueueDeviceQueueActilityItemRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.api.EnqueueDeviceQueueActilityItemRequest;
  return proto.api.EnqueueDeviceQueueActilityItemRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.api.EnqueueDeviceQueueActilityItemRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.api.EnqueueDeviceQueueActilityItemRequest}
 */
proto.api.EnqueueDeviceQueueActilityItemRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setDevEui(value);
      break;
    case 2:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setConfirmDownlink(value);
      break;
    case 3:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setFlushDownlinkQueue(value);
      break;
    case 4:
      var value = /** @type {string} */ (reader.readString());
      msg.setPayloadHex(value);
      break;
    case 5:
      var value = /** @type {string} */ (reader.readString());
      msg.setTargetPorts(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Class method variant: serializes the given message to binary data
 * (in protobuf wire format), writing to the given BinaryWriter.
 * @param {!proto.api.EnqueueDeviceQueueActilityItemRequest} message
 * @param {!jspb.BinaryWriter} writer
 */
proto.api.EnqueueDeviceQueueActilityItemRequest.serializeBinaryToWriter = function(message, writer) {
  message.serializeBinaryToWriter(writer);
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.api.EnqueueDeviceQueueActilityItemRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  this.serializeBinaryToWriter(writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the message to binary data (in protobuf wire format),
 * writing to the given BinaryWriter.
 * @param {!jspb.BinaryWriter} writer
 */
proto.api.EnqueueDeviceQueueActilityItemRequest.prototype.serializeBinaryToWriter = function (writer) {
  var f = undefined;
  f = this.getDevEui();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = this.getConfirmDownlink();
  if (f) {
    writer.writeBool(
      2,
      f
    );
  }
  f = this.getFlushDownlinkQueue();
  if (f) {
    writer.writeBool(
      3,
      f
    );
  }
  f = this.getPayloadHex();
  if (f.length > 0) {
    writer.writeString(
      4,
      f
    );
  }
  f = this.getTargetPorts();
  if (f.length > 0) {
    writer.writeString(
      5,
      f
    );
  }
};


/**
 * Creates a deep clone of this proto. No data is shared with the original.
 * @return {!proto.api.EnqueueDeviceQueueActilityItemRequest} The clone.
 */
proto.api.EnqueueDeviceQueueActilityItemRequest.prototype.cloneMessage = function() {
  return /** @type {!proto.api.EnqueueDeviceQueueActilityItemRequest} */ (jspb.Message.cloneMessage(this));
};


/**
 * optional string dev_eui = 1;
 * @return {string}
 */
proto.api.EnqueueDeviceQueueActilityItemRequest.prototype.getDevEui = function() {
  return /** @type {string} */ (jspb.Message.getFieldProto3(this, 1, ""));
};


/** @param {string} value  */
proto.api.EnqueueDeviceQueueActilityItemRequest.prototype.setDevEui = function(value) {
  jspb.Message.setField(this, 1, value);
};


/**
 * optional bool confirm_downlink = 2;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.api.EnqueueDeviceQueueActilityItemRequest.prototype.getConfirmDownlink = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldProto3(this, 2, false));
};


/** @param {boolean} value  */
proto.api.EnqueueDeviceQueueActilityItemRequest.prototype.setConfirmDownlink = function(value) {
  jspb.Message.setField(this, 2, value);
};


/**
 * optional bool flush_downlink_queue = 3;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.api.EnqueueDeviceQueueActilityItemRequest.prototype.getFlushDownlinkQueue = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldProto3(this, 3, false));
};


/** @param {boolean} value  */
proto.api.EnqueueDeviceQueueActilityItemRequest.prototype.setFlushDownlinkQueue = function(value) {
  jspb.Message.setField(this, 3, value);
};


/**
 * optional string payload_hex = 4;
 * @return {string}
 */
proto.api.EnqueueDeviceQueueActilityItemRequest.prototype.getPayloadHex = function() {
  return /** @type {string} */ (jspb.Message.getFieldProto3(this, 4, ""));
};


/** @param {string} value  */
proto.api.EnqueueDeviceQueueActilityItemRequest.prototype.setPayloadHex = function(value) {
  jspb.Message.setField(this, 4, value);
};


/**
 * optional string target_ports = 5;
 * @return {string}
 */
proto.api.EnqueueDeviceQueueActilityItemRequest.prototype.getTargetPorts = function() {
  return /** @type {string} */ (jspb.Message.getFieldProto3(this, 5, ""));
};


/** @param {string} value  */
proto.api.EnqueueDeviceQueueActilityItemRequest.prototype.setTargetPorts = function(value) {
  jspb.Message.setField(this, 5, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.api.EnqueueDeviceQueueActilityItemResponse = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.api.EnqueueDeviceQueueActilityItemResponse, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.api.EnqueueDeviceQueueActilityItemResponse.displayName = 'proto.api.EnqueueDeviceQueueActilityItemResponse';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.api.EnqueueDeviceQueueActilityItemResponse.prototype.toObject = function(opt_includeInstance) {
  return proto.api.EnqueueDeviceQueueActilityItemResponse.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.api.EnqueueDeviceQueueActilityItemResponse} msg The msg instance to transform.
 * @return {!Object}
 */
proto.api.EnqueueDeviceQueueActilityItemResponse.toObject = function(includeInstance, msg) {
  var f, obj = {
    confirmDownlink: msg.getConfirmDownlink(),
    flushDownlinkQueue: msg.getFlushDownlinkQueue(),
    payloadHex: msg.getPayloadHex(),
    targetPorts: msg.getTargetPorts(),
    status: msg.getStatus()
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.api.EnqueueDeviceQueueActilityItemResponse}
 */
proto.api.EnqueueDeviceQueueActilityItemResponse.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.api.EnqueueDeviceQueueActilityItemResponse;
  return proto.api.EnqueueDeviceQueueActilityItemResponse.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.api.EnqueueDeviceQueueActilityItemResponse} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.api.EnqueueDeviceQueueActilityItemResponse}
 */
proto.api.EnqueueDeviceQueueActilityItemResponse.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setConfirmDownlink(value);
      break;
    case 2:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setFlushDownlinkQueue(value);
      break;
    case 3:
      var value = /** @type {string} */ (reader.readString());
      msg.setPayloadHex(value);
      break;
    case 4:
      var value = /** @type {string} */ (reader.readString());
      msg.setTargetPorts(value);
      break;
    case 5:
      var value = /** @type {string} */ (reader.readString());
      msg.setStatus(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Class method variant: serializes the given message to binary data
 * (in protobuf wire format), writing to the given BinaryWriter.
 * @param {!proto.api.EnqueueDeviceQueueActilityItemResponse} message
 * @param {!jspb.BinaryWriter} writer
 */
proto.api.EnqueueDeviceQueueActilityItemResponse.serializeBinaryToWriter = function(message, writer) {
  message.serializeBinaryToWriter(writer);
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.api.EnqueueDeviceQueueActilityItemResponse.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  this.serializeBinaryToWriter(writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the message to binary data (in protobuf wire format),
 * writing to the given BinaryWriter.
 * @param {!jspb.BinaryWriter} writer
 */
proto.api.EnqueueDeviceQueueActilityItemResponse.prototype.serializeBinaryToWriter = function (writer) {
  var f = undefined;
  f = this.getConfirmDownlink();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
  f = this.getFlushDownlinkQueue();
  if (f) {
    writer.writeBool(
      2,
      f
    );
  }
  f = this.getPayloadHex();
  if (f.length > 0) {
    writer.writeString(
      3,
      f
    );
  }
  f = this.getTargetPorts();
  if (f.length > 0) {
    writer.writeString(
      4,
      f
    );
  }
  f = this.getStatus();
  if (f.length > 0) {
    writer.writeString(
      5,
      f
    );
  }
};


/**
 * Creates a deep clone of this proto. No data is shared with the original.
 * @return {!proto.api.EnqueueDeviceQueueActilityItemResponse} The clone.
 */
proto.api.EnqueueDeviceQueueActilityItemResponse.prototype.cloneMessage = function() {
  return /** @type {!proto.api.EnqueueDeviceQueueActilityItemResponse} */ (jspb.Message.cloneMessage(this));
};


/**
 * optional bool confirm_downlink = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.api.EnqueueDeviceQueueActilityItemResponse.prototype.getConfirmDownlink = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldProto3(this, 1, false));
};


/** @param {boolean} value  */
proto.api.EnqueueDeviceQueueActilityItemResponse.prototype.setConfirmDownlink = function(value) {
  jspb.Message.setField(this, 1, value);
};


/**
 * optional bool flush_downlink_queue = 2;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.api.EnqueueDeviceQueueActilityItemResponse.prototype.getFlushDownlinkQueue = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldProto3(this, 2, false));
};


/** @param {boolean} value  */
proto.api.EnqueueDeviceQueueActilityItemResponse.prototype.setFlushDownlinkQueue = function(value) {
  jspb.Message.setField(this, 2, value);
};


/**
 * optional string payload_hex = 3;
 * @return {string}
 */
proto.api.EnqueueDeviceQueueActilityItemResponse.prototype.getPayloadHex = function() {
  return /** @type {string} */ (jspb.Message.getFieldProto3(this, 3, ""));
};


/** @param {string} value  */
proto.api.EnqueueDeviceQueueActilityItemResponse.prototype.setPayloadHex = function(value) {
  jspb.Message.setField(this, 3, value);
};


/**
 * optional string target_ports = 4;
 * @return {string}
 */
proto.api.EnqueueDeviceQueueActilityItemResponse.prototype.getTargetPorts = function() {
  return /** @type {string} */ (jspb.Message.getFieldProto3(this, 4, ""));
};


/** @param {string} value  */
proto.api.EnqueueDeviceQueueActilityItemResponse.prototype.setTargetPorts = function(value) {
  jspb.Message.setField(this, 4, value);
};


/**
 * optional string status = 5;
 * @return {string}
 */
proto.api.EnqueueDeviceQueueActilityItemResponse.prototype.getStatus = function() {
  return /** @type {string} */ (jspb.Message.getFieldProto3(this, 5, ""));
};


/** @param {string} value  */
proto.api.EnqueueDeviceQueueActilityItemResponse.prototype.setStatus = function(value) {
  jspb.Message.setField(this, 5, value);
};


goog.object.extend(exports, proto.api);
