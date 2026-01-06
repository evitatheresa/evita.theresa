# Layanan Administrasi Desa - Progressive Web App

## Deskripsi
Progressive Web App (PWA) untuk sistem layanan administrasi desa yang memungkinkan warga mengajukan berbagai surat keterangan dan dokumen administrasi secara online.

## Fitur PWA

### ✨ Fitur Utama
- **Installable**: Dapat diinstall di perangkat mobile dan desktop seperti aplikasi native
- **Offline Mode**: Tetap berfungsi tanpa koneksi internet menggunakan Service Worker
- **Responsive**: Tampilan optimal di semua ukuran layar
- **Fast Loading**: Caching untuk performa maksimal
- **Auto Update**: Pembaruan otomatis saat ada versi baru

### 📱 Portal Warga
- Pengajuan Surat Keterangan Domisili
- Pengajuan Surat Keterangan Keluarga
- Pengajuan Surat Pengantar KTP
- Pengajuan Surat Keterangan Usaha
- Pengajuan Surat Keterangan Tidak Mampu (SKTM)
- Riwayat pengajuan dengan status real-time
- Penyimpanan data lokal untuk akses offline

### ⚙️ Portal Administrator
- Dashboard statistik pengajuan
- Manajemen status pengajuan (Menunggu, Diproses, Selesai)
- Filter dan pencarian pengajuan
- Export data ke format JSON
- Hapus data pengajuan

## Struktur File

```
evita.theresa/
├── index.html              # Landing page utama
├── manifest.json           # Web App Manifest
├── sw.js                   # Service Worker untuk offline mode
├── admin/
│   └── index.html         # Portal administrator
├── home/
│   └── index.html         # Portal warga
├── style/
│   ├── css.css            # Stylesheet utama
│   └── js.js              # JavaScript utilities
└── icons/
    ├── icon-192x192.png   # Icon PWA 192x192
    └── icon-512x512.png   # Icon PWA 512x512
```

## Instalasi PWA

### Untuk Pengguna Mobile (Android/iOS)

#### Android (Chrome):
1. Buka website di Chrome browser
2. Tap menu (⋮) di pojok kanan atas
3. Pilih "Install app" atau "Add to Home screen"
4. Ikuti instruksi instalasi

#### iOS (Safari):
1. Buka website di Safari browser
2. Tap tombol Share (kotak dengan panah ke atas)
3. Scroll dan pilih "Add to Home Screen"
4. Tap "Add"

### Untuk Desktop (Windows/Mac/Linux)

#### Chrome/Edge:
1. Buka website di browser
2. Klik icon install (⊕) di address bar
3. Atau klik menu (⋮) → "Install Layanan Administrasi Desa"
4. Klik "Install"

## Teknologi yang Digunakan

- **HTML5**: Struktur aplikasi
- **CSS3**: Styling dengan modern gradient dan animasi
- **JavaScript (Vanilla)**: Logika aplikasi dan PWA functionality
- **Service Worker**: Offline caching dan background sync
- **LocalStorage**: Penyimpanan data lokal
- **Web App Manifest**: Metadata untuk PWA

## Persyaratan PWA

✅ **Checklist PWA**:
- [x] HTTPS (atau localhost untuk development)
- [x] Service Worker terdaftar
- [x] Web App Manifest dengan icons
- [x] Responsive design
- [x] Fast loading (< 3s)
- [x] Offline functionality
- [x] Installable prompt
- [x] Mobile-friendly

## Cara Menggunakan

### Untuk Warga:
1. Akses aplikasi melalui browser atau PWA yang terinstall
2. Klik "Portal Warga" di halaman utama
3. Pilih jenis layanan yang dibutuhkan
4. Isi formulir pengajuan
5. Klik "Kirim Pengajuan"
6. Pantau status di "Riwayat Pengajuan"

### Untuk Administrator:
1. Akses aplikasi melalui browser atau PWA yang terinstall
2. Klik "Portal Admin" di halaman utama
3. Lihat dashboard statistik
4. Kelola pengajuan dengan mengubah status
5. Export atau hapus data sesuai kebutuhan

## Fitur Offline

Aplikasi ini dapat berfungsi dalam mode offline dengan fitur:
- Cache halaman utama dan asset
- Penyimpanan data pengajuan di LocalStorage
- Indikator status koneksi online/offline
- Sync otomatis saat kembali online

## Development

### Menjalankan Lokal:
```bash
# Dengan PHP built-in server
php -S localhost:8000

# Atau dengan Python
python -m http.server 8000

# Atau dengan Node.js
npx http-server -p 8000
```

Akses: `http://localhost:8000`

### Testing PWA:
1. Buka Chrome DevTools (F12)
2. Tab "Application" → "Manifest"
3. Tab "Application" → "Service Workers"
4. Tab "Lighthouse" → Generate report untuk PWA score

## Browser Support

- ✅ Chrome/Edge 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Opera 76+

## Keamanan

- Data disimpan lokal di browser pengguna
- Tidak ada transmisi data ke server (standalone mode)
- HTTPS diperlukan untuk production deployment
- Service Worker hanya bekerja di secure context

## Lisensi

© 2026 Layanan Administrasi Desa

## Kontributor

Dikembangkan untuk memudahkan akses layanan administrasi desa kepada masyarakat.

---

**Progressive Web App** - Akses Mudah, Kapan Saja, Di Mana Saja! 🚀
