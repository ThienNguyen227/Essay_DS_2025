import rsa
import time
import matplotlib.pyplot as plt

# Sinh cặp khóa RSA (2048 bits)
(public_key, private_key) = rsa.newkeys(2048)

# Danh sách độ dài thông điệp cần thử nghiệm
message_lengths = [10, 50, 100, 150, 200, 240]

# Các danh sách lưu thời gian mã hóa và giải mã
encryption_times = []
decryption_times = []

# Vòng lặp thử nghiệm với các độ dài thông điệp khác nhau
for length in message_lengths:
    # Tạo thông điệp mẫu với độ dài tương ứng
    message = ("a" * length).encode('utf8')
    
    # Giới hạn độ dài tối đa theo độ lớn khóa RSA
    max_length = 245  # Với khóa 2048 bits
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

# Vẽ biểu đồ thể hiện thời gian mã hóa và giải mã
plt.plot(message_lengths, encryption_times, label='Mã hóa', marker='o')
plt.plot(message_lengths, decryption_times, label='Giải mã', marker='o')
plt.xlabel('Độ dài thông điệp (số ký tự)')
plt.ylabel('Thời gian (giây)')
plt.title('Thời gian mã hóa và giải mã theo độ dài thông điệp (RSA)')
plt.legend()
plt.grid(True)
plt.show()
