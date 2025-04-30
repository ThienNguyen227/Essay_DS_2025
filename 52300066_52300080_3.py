import rsa
import time
import matplotlib.pyplot as plt

# Sinh cặp khóa RSA (2048 bits)
(public_key, private_key) = rsa.newkeys(2048)

# Phần 1: Kiểm tra mã hóa và giải mã với tin nhắn mẫu
sample_messages = [
    "Hello",
    "Test RSA",
    "This is a longer message to check RSA encryption",
    "A" * 300  # Thông điệp dài hơn 245 bytes (300 ký tự)
]
print("Kiểm tra mã hóa và giải mã với tin nhắn mẫu:")
for msg in sample_messages:
    # Chuyển tin nhắn thành bytes
    message = msg.encode('utf8')
    
    # Hiển thị thông điệp gốc kèm độ dài
    print(f"Thông điệp gốc: {msg} (độ dài: {len(message)} bytes)")
    
    # Giới hạn độ dài tối đa theo độ lớn khóa RSA
    max_length = 245  # Với khóa 2048 bits
    if len(message) > max_length:
        print(f"Thông điệp quá dài ({len(message)} bytes), chỉ mã hóa {max_length} bytes đầu tiên.")
        message = message[:max_length]
    
    # Mã hóa
    ciphertext = rsa.encrypt(message, public_key)
    print(f"Thông điệp mã hóa: {ciphertext.hex()}")
    
    # Giải mã
    decrypted_message = rsa.decrypt(ciphertext, private_key).decode('utf8')
    print(f"Thông điệp giải mã: {decrypted_message}")
    print(f"Xác minh: {decrypted_message == msg[:max_length].encode('utf8').decode('utf8')}\n")

# Phần 2: Đo thời gian mã hóa và giải mã với các độ dài thông điệp khác nhau
message_lengths = [10, 50, 100, 150, 200, 240]
encryption_times = []
decryption_times = []

print("Đo thời gian mã hóa và giải mã:")
for length in message_lengths:
    # Tạo thông điệp mẫu với độ dài tương ứng
    message = ("a" * length).encode('utf8')
    
    # Giới hạn độ dài tối đa
    if len(message) > max_length:
        message = message[:max_length]
    
    # Đo thời gian mã hóa
    start_encrypt = time.time()
    ciphertext = rsa.encrypt(message, public_key)
    end_encrypt = time.time()
    encryption_times.append(end_encrypt - start_encrypt)
    
    # Đo thời gian giải mã
    start_decrypt = time.time()
    decrypted_message = rsa.decrypt(ciphertext, private_key)
    end_decrypt = time.time()
    decryption_times.append(end_decrypt - start_decrypt)
    
    print(f"Độ dài {length}: Mã hóa = {encryption_times[-1]:.4f}s, Giải mã = {decryption_times[-1]:.4f}s")

# Phần 3: Vẽ biểu đồ
plt.plot(message_lengths, encryption_times, label='Mã hóa', marker='o')
plt.plot(message_lengths, decryption_times, label='Giải mã', marker='o')
plt.xlabel('Độ dài thông điệp (số ký tự)')
plt.ylabel('Thời gian (giây)')
plt.title('Thời gian mã hóa và giải mã theo độ dài thông điệp (RSA)')
plt.legend()
plt.grid(True)

# Lưu biểu đồ trước khi hiển thị
plt.show()