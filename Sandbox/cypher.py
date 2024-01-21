
class CaesarCypher:

    CHARSET = 'ABCDEFGHIJKLMNOPQRSTUWVXYZ0123456789'
    DEFAULT_ENCODING = 'utf8'

    def __init__(self, shift = 3):
        self._shift = shift

    @staticmethod
    def rotate_value(value, shift, lower, upper):
        if lower <= value <= upper:
            return lower + (value - lower + shift) % (upper - lower + 1)
        else:
            return value

    def shift_value(c, shift, lower, upper):
        try:
            index = CaesarCypher.CHARSET.find(c)
            shifted_index = (index + shift) % len(CaesarCypher.CHARSET)
            return CaesarCypher.CHARSET[shifted_index]
        except:
            return c


    @staticmethod
    def rotate_all_bytes(lob, shift, lower, upper):
        return bytes(CaesarCypher.rotate_value(c, shift, lower, upper) for c in lob)

    def encrypt(self, message, encoding = DEFAULT_ENCODING):
        lob = bytes(message, encoding = encoding)
        encrypted = self.rotate_all_bytes(lob, self._shift, ord('a'), ord('z'))
        encrypted = self.rotate_all_bytes(encrypted, self._shift, ord('A'), ord('Z'))
        return encrypted

    def decrypt(self, encrypted, encoding = DEFAULT_ENCODING):
        try:
            lob = bytes(encrypted, encoding=encoding)
        except:
            lob = encrypted
        decrypted = self.rotate_all_bytes(lob, -self._shift, ord('A'), ord('Z'))
        decrypted = self.rotate_all_bytes(decrypted, -self._shift, ord('a'), ord('z'))
        return str(decrypted, encoding = encoding)


# ----------------------------------------------------------------------

if __name__ == '__main__':

    cypher = CaesarCypher(10)

    message = 'Tommorow D-Day'

    encrypted = cypher.encrypt(message)
    print(encrypted)

    decrypted = cypher.decrypt(encrypted)
    print(decrypted)