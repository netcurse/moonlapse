import bcrypt
from sqlalchemy.exc import SQLAlchemyError

from app.models import User
from .protostate import ProtoState
from app.net import create_deny_packet, create_ok_packet, LoginPacket, RegisterPacket

class EntryState(ProtoState):
    async def handle_login_packet(self, packet: LoginPacket):
        with self.proto.SessionFactory() as session:
            # if the user exists
            user = session.query(User).filter(User.username == packet.username).first()
            if not user:
                deny_packet = create_deny_packet("User does not exist")
                await self.proto.send_packet(deny_packet)
                return
            
            # if the password is correct
            if not bcrypt.checkpw(packet.password.encode(), user.password):
                deny_packet = create_deny_packet("Incorrect password")
                await self.proto.send_packet(deny_packet)
                return
            
            self.proto.set_state("Play")
            ok_packet = create_ok_packet("Logged in successfully")
            await self.proto.send_packet(ok_packet)

    
    async def handle_register_packet(self, packet: RegisterPacket):
        with self.proto.SessionFactory() as session:
            try:
                # if the username already exists
                if session.query(User).filter(User.username == packet.username).first():
                    deny_packet = create_deny_packet("Username already taken")
                    await self.proto.send_packet(deny_packet)
                    return
                
                # if not, create a new user and commit the transaction
                hashpw = bcrypt.hashpw(packet.password.encode(), bcrypt.gensalt())
                user = User(username=packet.username, password=hashpw)
                session.add(user)
                session.commit()
                ok_packet = create_ok_packet("Registered successfully")
                await self.proto.send_packet(ok_packet)

            except Exception as e:
                session.rollback()
                deny_packet = create_deny_packet("Error registering user")
                await self.proto.send_packet(deny_packet)
