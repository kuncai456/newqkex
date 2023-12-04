import rsa

# 生成RSA密钥对
(public_key, private_key) = rsa.newkeys(1024)


print(public_key)
print(private_key)
# 要加密的明文
message = b'Hello, World!'

# 使用公钥进行加密
encrypted_message = rsa.encrypt(message, public_key)

# 输出加密后的密文
print("加密后的密文:", encrypted_message)

# 使用私钥进行解密
decrypted_message = rsa.decrypt(encrypted_message, private_key)

# 输出解密后的明文
print("解密后的明文:", decrypted_message)