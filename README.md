# 🔐 Setup Git — GitHub SSH Key Manager

> Ứng dụng giao diện đồ hoạ (GUI) giúp tạo SSH key, sao chép lên clipboard và kiểm tra kết nối GitHub nhanh chóng.

---

## ✨ Tính năng

- Tạo SSH key `ed25519` tự động theo email GitHub
- Hiển thị public key để dán trực tiếp vào GitHub
- Copy public key lên clipboard chỉ bằng 1 click
- Kiểm tra kết nối SSH tới GitHub (tự động xác nhận fingerprint lần đầu)

---

## 🖥️ Giao diện

```
┌──────────────────────────────────────┐
│         GitHub SSH Setup             │
│                                      │
│  GitHub Email: [____________________]│
│                                      │
│       [Generate SSH Key]             │
│                                      │
│  Public Key (Paste this to GitHub):  │
│  [                                  ]│
│  [      Copy to Clipboard       ]    │
│                                      │
│  After adding to GitHub, test:       │
│       [Test Connection]              │
│                                      │
│  Status: Ready                       │
└──────────────────────────────────────┘
```

---

## 📋 Yêu cầu

| Yêu cầu | Phiên bản tối thiểu |
|--------|-------------------|
| Python | 3.8+ |
| OpenSSH | Đã cài sẵn trên Windows 10/11 |
| tkinter | Đi kèm theo Python |

---

## 🚀 Hướng dẫn cài đặt & chạy

### 1. Clone repository

```bash
git clone git@github.com:tranthinhembedded/setup-git.git
cd setup-git
```

### 2. (Tuỳ chọn) Cài dependencies

```bash
pip install -r requirements.txt
```

> `requirements.txt` chứa `pyinstaller` — dùng khi muốn đóng gói thành file `.exe`.

### 3. Chạy ứng dụng

```bash
python setupGit.py
```

---

## 📦 Đóng gói thành file `.exe` (Windows)

```bash
pip install pyinstaller
pyinstaller --onefile --windowed setupGit.py
```

File `.exe` sẽ xuất hiện trong thư mục `dist/`.

---

## 🔧 Cách sử dụng

1. **Nhập email GitHub** của bạn vào ô input.
2. Bấm **"Generate SSH Key"** → key `~/.ssh/id_ed25519` sẽ được tạo.
3. **Copy public key** bằng nút "Copy to Clipboard".
4. Vào **GitHub → Settings → SSH and GPG keys → New SSH key** → paste key vào.
5. Bấm **"Test Connection"** để kiểm tra kết nối.
6. Thông báo `successfully authenticated` = thành công! 🎉

---

## 📁 Cấu trúc dự án

```
setup-git/
├── setupGit.py        # Source code chính
├── requirements.txt   # Dependencies (pyinstaller)
└── README.md          # Tài liệu này
```

---

## 👤 Tác giả

**tranthinhembedded**  
📧 GitHub: [github.com/tranthinhembedded](https://github.com/tranthinhembedded)

---

## 📄 License

MIT License — Tự do sử dụng, chỉnh sửa và phân phối.
