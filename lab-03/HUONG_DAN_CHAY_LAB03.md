# 🎯 HƯỚNG DẪN CHI TIẾT CHẠY LAB 03 - ĐÃ KIỂM TRA

## 📋 MỤC LỤC
- [PHẦN 1: Chuẩn bị môi trường](#phần-1-chuẩn-bị-môi-trường)
- [PHẦN 2: Cài đặt thư viện](#phần-2-cài-đặt-thư-viện)
- [PHẦN 3: Caesar Cipher](#phần-3-caesar-cipher)
- [PHẦN 4: RSA Cipher](#phần-4-rsa-cipher)
- [PHẦN 5: ECC Cipher](#phần-5-ecc-cipher)
- [PHẦN 6: Chạy ứng dụng](#phần-6-chạy-ứng-dụng)

---

## 🎯 PHẦN 1: CHUẨN BỊ MÔI TRƯỜNG

### Bước 1.1: Kiểm tra Python
```bash
python --version
```
Kết quả mong đợi: Python 3.8 hoặc cao hơn

### Bước 1.2: Kiểm tra cấu trúc thư mục
Đảm bảo cấu trúc sau đã tồn tại:
```
lab-03/
├── ui/
├── cipher/
│   ├── rsa/
│   │   ├── keys/
│   │   ├── __init__.py
│   │   └── rsa_cipher.py
│   └── ecc/
│       ├── keys/
│       ├── __init__.py
│       └── ecc_cipher.py
├── api.py
├── caesar_cipher.py
├── rsa_cipher.py
├── ecc_cipher.py
└── requirements.txt
```

**✅ Code đã có sẵn các file cipher, chỉ cần chạy!**

---

## 🎯 PHẦN 2: CÀI ĐẶT THƯ VIỆN

### Bước 2.1: Kiểm tra requirements.txt
File `requirements.txt` đã có sẵn với nội dung:
```
PyQt5
requests
Flask==2.3.2
rsa==4.9
ecdsa
```

### Bước 2.2: Cài đặt thư viện
```bash
cd lab-03
pip install -r requirements.txt
```

Kết quả thành công:
```
Successfully installed PyQt5-... Flask-2.3.2 rsa-4.9 ecdsa-...
```

### Bước 2.3: Copy Platform Plugins (Nếu chưa có)

**Tìm thư mục PyQt5:**
```bash
python -c "import PyQt5; import os; print(os.path.dirname(PyQt5.__file__))"
```

**Copy từ:**
```
<Python>\Lib\site-packages\PyQt5\Qt5\plugins\platforms\
```

**Paste vào:**
```
lab-03\platforms\
```

Các file cần có: `qwindows.dll`, `qminimal.dll`, `qoffscreen.dll`

**⚠️ LƯU Ý:** Nếu thư mục `platforms` đã có file, KHÔNG CẦN copy lại!

---

## 🎯 PHẦN 3: CAESAR CIPHER

### ✅ File đã có sẵn:
- `ui/caesar.ui` - Giao diện
- `ui/caesar.py` - Code UI được generate
- `caesar_cipher.py` - Backend application

### Kiểm tra widget names trong caesar.py:
```python
# Widget names THỰC TẾ (không phải tên trong hướng dẫn)
self.lineEdit      # Plain text input
self.textEdit      # Key input
self.lineEdit_2    # Cipher text output
self.pushButton    # Encrypt button
self.pushButton_2  # Decrypt button
```

### ⚠️ Nếu cần sửa lại UI:

**Nếu bạn muốn tạo lại UI với Qt Designer:**

1. Mở Qt Designer
2. Main Window → Create
3. Đặt **objectName** cho các widget:
   - Plain Text Edit → `txt_plain_text`
   - Line Edit (Key) → `txt_key`
   - Plain Text Edit (Cipher) → `txt_cipher_text`
   - Button Encrypt → `btn_encrypt`
   - Button Decrypt → `btn_decrypt`

4. Lưu: `ui/caesar.ui`

5. Chuyển đổi:
```bash
pyuic5 -x ./ui/caesar.ui -o ./ui/caesar.py
```

6. Thêm vào **ĐẦU FILE** `ui/caesar.py`:
```python
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"
```

7. Sửa file `caesar_cipher.py` để match với tên widget mới

**✅ Code hiện tại ĐÃ ĐÚNG, không cần làm lại!**

---

## 🎯 PHẦN 4: RSA CIPHER

### ✅ File đã có sẵn:
- `cipher/rsa/rsa_cipher.py` - RSA implementation
- `cipher/rsa/__init__.py` - Module init
- `ui/rsa.ui` - Giao diện RSA
- `ui/rsa.py` - Code UI
- `rsa_cipher.py` - Backend application

### Kiểm tra widget names trong rsa.py:
```python
self.txt_message      # Message input
self.cmb_key_type     # ComboBox: public/private
self.txt_result       # Encrypted/Decrypted result
self.txt_signature    # Signature display
self.btn_gen_keys     # Generate keys button
self.btn_encrypt      # Encrypt button
self.btn_decrypt      # Decrypt button
self.btn_sign         # Sign button
self.btn_verify       # Verify button
```

**✅ Code đã đúng, không cần sửa!**

---

## �� PHẦN 5: ECC CIPHER

### ✅ File đã có sẵn:
- `cipher/ecc/ecc_cipher.py` - ECC implementation
- `cipher/ecc/__init__.py` - Module init
- `ui/ecc.ui` - Giao diện ECC
- `ui/ecc.py` - Code UI
- `ecc_cipher.py` - Backend application

### Kiểm tra widget names trong ecc.py:
```python
self.txt_info         # Information/Message input
self.txt_sign         # Signature display
self.btn_gen_keys     # Generate keys button
self.btn_sign         # Sign button
self.btn_verify       # Verify button
```

**✅ Code đã đúng, không cần sửa!**

---

## 🎯 PHẦN 6: CHẠY ỨNG DỤNG

### ⚠️ LƯU Ý QUAN TRỌNG:
**API của lab-03 KHÁC với lab-02!**
- Lab-02 API: Chỉ có Caesar cipher
- Lab-03 API: Có Caesar + RSA + ECC

**Phải chạy API từ thư mục lab-03, KHÔNG PHẢI lab-02!**

---

### 🚀 Cách 1: Chạy Caesar Cipher

#### Terminal 1 - Start API Server:
```bash
cd lab-03
python api.py
```

**Kết quả thấy:**
```
 * Serving Flask app 'api'
 * Running on http://127.0.0.1:5000
```

**⚠️ KHÔNG TẮT TERMINAL NÀY!**

#### Terminal 2 - Run Caesar App:
```bash
cd lab-03
python caesar_cipher.py
```

#### Test Caesar:
1. Nhập Plain Text: `hello world`
2. Nhập Key: `3`
3. Click **Encrypt** → Thấy popup "Encrypted Successfully"
4. Cipher Text hiện: `khoor zruog`
5. Click **Decrypt** → Thấy popup "Decrypted Successfully"
6. Plain Text trở lại: `hello world`

---

### 🚀 Cách 2: Chạy RSA Cipher

#### Terminal 1 - API Server (giữ nguyên hoặc restart):
```bash
cd lab-03
python api.py
```

#### Terminal 2 - Run RSA App:
```bash
cd lab-03
python rsa_cipher.py
```

#### Test RSA:
1. Click **Generate Keys** → Popup "Keys generated successfully"
2. Nhập Message: `Hello RSA`
3. Chọn Key Type: `public`
4. Click **Encrypt** → Thấy encrypted message (hex)
5. Chọn Key Type: `private`
6. Click **Decrypt** → Message gốc hiện lại
7. Nhập Message để sign → Click **Sign**
8. Click **Verify** → Thấy "Verified Successfully"

---

### 🚀 Cách 3: Chạy ECC Cipher

#### Terminal 1 - API Server (giữ nguyên):
```bash
cd lab-03
python api.py
```

#### Terminal 2 - Run ECC App:
```bash
cd lab-03
python ecc_cipher.py
```

#### Test ECC:
1. Click **Generate Keys** → Popup "Keys generated successfully"
2. Nhập Information: `hutech mtt doan nguyen`
3. Click **Sign** → Signature hiện ra
4. Click **Verify** → Thấy "Verified Successfully"
5. Thử đổi message hoặc signature → Click **Verify** → "Verified Fail"

---

## ✅ CHECKLIST KIỂM TRA CUỐI CÙNG

### Môi trường:
- [ ] Python 3.8+ đã cài
- [ ] Các thư viện đã cài (`pip list` có PyQt5, Flask, rsa, ecdsa)
- [ ] Thư mục `platforms/` có file `.dll` (Windows) hoặc `.so` (Linux)

### Cấu trúc file:
- [ ] File `api.py` có trong `lab-03/`
- [ ] Thư mục `cipher/rsa/` và `cipher/ecc/` có `__init__.py`
- [ ] File `caesar_cipher.py`, `rsa_cipher.py`, `ecc_cipher.py` có trong `lab-03/`
- [ ] Thư mục `ui/` có các file `.py` và `.ui`

### Chạy thử:
- [ ] API server chạy được (`python api.py`)
- [ ] Caesar app chạy được và encrypt/decrypt thành công
- [ ] RSA app chạy được, generate keys thành công
- [ ] RSA encrypt/decrypt hoạt động
- [ ] RSA sign/verify hoạt động
- [ ] ECC app chạy được, generate keys thành công
- [ ] ECC sign/verify hoạt động

---

## 🔧 XỬ LÝ LỖI THƯỜNG GẶP

### Lỗi 1: `ModuleNotFoundError: No module named 'cipher'`
**Nguyên nhân:** Chưa có file `__init__.py` trong thư mục cipher

**Giải pháp:**
```bash
# Tạo file __init__.py (file rỗng)
cd lab-03/cipher/rsa
type nul > __init__.py  # Windows
# hoặc
touch __init__.py       # Linux/Mac

cd ../ecc
type nul > __init__.py  # Windows
```

### Lỗi 2: `AttributeError: 'Ui_MainWindow' object has no attribute 'btn_encrypt'`
**Nguyên nhân:** Tên widget trong UI không khớp với code

**Giải pháp:**
1. Mở file `ui/caesar.py` hoặc `ui/rsa.py`
2. Tìm dòng `self.pushButton = QtWidgets.QPushButton(...)`
3. Xem tên thực tế của widget
4. Sửa file `caesar_cipher.py` hoặc `rsa_cipher.py` cho khớp

### Lỗi 3: `requests.exceptions.ConnectionError`
**Nguyên nhân:** API server chưa chạy

**Giải pháp:**
```bash
# Terminal 1
cd lab-03
python api.py
```

### Lỗi 4: `FileNotFoundError: cipher/rsa/keys/publicKey.pem`
**Nguyên nhân:** Chưa generate keys

**Giải pháp:**
- Click nút **Generate Keys** trong app trước khi encrypt/decrypt/sign/verify

---

## 📌 GHI CHÚ QUAN TRỌNG

1. **API Server phải chạy TRƯỚC desktop app**
2. **API của lab-03 ≠ API của lab-02**
3. **Phải generate keys TRƯỚC KHI sử dụng RSA/ECC**
4. **Widget names phải KHỚP giữa UI và code**
5. **File `__init__.py` có 2 dấu gạch dưới `__` trước và sau**

---

**✅ Hướng dẫn này đã được kiểm tra với code thực tế!**
