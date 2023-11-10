import logging

class ProtocolLoggerAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        protocol_ident = self.extra.get('ident', 'Unknown')
        protostate_name = self.extra.get('protostate', 'None').__class__.__name__
        return f"[{protocol_ident}][{protostate_name}] {msg}", kwargs
