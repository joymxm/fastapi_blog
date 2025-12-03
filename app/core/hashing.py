
# from passlib.context import CryptContext

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# class Hasher():
#     @staticmethod
#     def verify_password(plain_password, hashed_password):
#         return pwd_context.verify(plain_password, hashed_password)

#     @staticmethod
#     def get_password_hash(password):
#         return pwd_context.hash(password)





import hashlib
import bcrypt

class Hasher:
    @staticmethod
    def _prepare_password(password: str) -> bytes:
        """
        Prepare password for bcrypt hashing.
        Bcrypt has a 72-byte limit, so we pre-hash longer passwords with SHA256.
        Returns bytes ready for bcrypt.
        """
        # Convert to bytes to check actual byte length
        password_bytes = password.encode('utf-8')
        
        # Bcrypt limit is 72 bytes
        if len(password_bytes) > 72:
            # Pre-hash with SHA256 to get a fixed 32-byte hash
            return hashlib.sha256(password_bytes).digest()
        
        return password_bytes
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Verify a plain text password against a hashed password.
        Handles passwords longer than 72 bytes by pre-hashing with SHA256.
        """
        try:
            # Prepare password (pre-hash if needed)
            prepared_password = Hasher._prepare_password(plain_password)
            
            # Verify using bcrypt
            # hashed_password is a string, so we need to encode it
            if isinstance(hashed_password, str):
                hashed_password = hashed_password.encode('utf-8')
            
            return bcrypt.checkpw(prepared_password, hashed_password)
        except (ValueError, TypeError, Exception):
            # If verification fails, try with original password (for backwards compatibility)
            try:
                original_bytes = plain_password.encode('utf-8')
                if isinstance(hashed_password, str):
                    hashed_password = hashed_password.encode('utf-8')
                return bcrypt.checkpw(original_bytes, hashed_password)
            except (ValueError, TypeError, Exception):
                return False
    
    @staticmethod
    def get_password_hash(password: str) -> str:
        """
        Hash a password using bcrypt.
        Handles passwords longer than 72 bytes by pre-hashing with SHA256.
        """
        # Prepare password (pre-hash if longer than 72 bytes)
        prepared_password = Hasher._prepare_password(password)
        
        # Generate salt and hash
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(prepared_password, salt)
        
        # Return as string
        return hashed.decode('utf-8')

