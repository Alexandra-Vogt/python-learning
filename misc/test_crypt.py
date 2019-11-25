#!/usr/bin/env python3

import crypt

password = "hunter2"
message = "My password is *******."

encrypted_message = crypt.encrypt(message, password)
decrypted_message = crypt.decrypt(encrypted_message, password)
assert message == decrypted_message
