<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#FF9800">
    <title>Portal Admin - Administrasi Desa</title>
    <link rel="manifest" href="/manifest.json">
    <link rel="stylesheet" href="/style/css.css">
</head>
<body>
    <div class="container">
        <header class="admin-header">
            <h1>Portal Administrator</h1>
            <p class="subtitle">Panel Manajemen Layanan Administrasi Desa</p>
        </header>
        
        <main>
            <div id="connectionStatus" style="display: none; padding: 15px; text-align: center; font-weight: bold;"></div>
            
            <div class="welcome-section">
                <h2>Dashboard Administrator</h2>
                <p>Kelola pengajuan dan layanan administrasi desa</p>
            </div>
            
            <div class="dashboard">
                <div class="stat-card">
                    <h3 id="totalSubmissions">0</h3>
                    <p>Total Pengajuan</p>
                </div>
                
                <div class="stat-card">
                    <h3 id="pendingSubmissions">0</h3>
                    <p>Menunggu Proses</p>
                </div>
                
                <div class="stat-card">
                    <h3 id="processedSubmissions">0</h3>
                    <p>Diproses</p>
                </div>
                
                <div class="stat-card">
                    <h3 id="completedSubmissions">0</h3>
                    <p>Selesai</p>
                </div>
            </div>
            
            <div style="margin-top: 40px;">
                <h2>Daftar Pengajuan</h2>
                <div style="margin: 20px 0;">
                    <button onclick="filterSubmissions('all')" class="btn btn-primary">Semua</button>
                    <button onclick="filterSubmissions('Menunggu Proses')" class="btn btn-secondary">Menunggu</button>
                    <button onclick="filterSubmissions('Diproses')" class="btn btn-secondary">Diproses</button>
                    <button onclick="filterSubmissions('Selesai')" class="btn btn-secondary">Selesai</button>
                </div>
                <div id="submissionsList"></div>
            </div>
            
            <div style="margin-top: 30px; padding: 20px; background: #f8f9fa; border-radius: 10px;">
                <h3>Aksi Cepat</h3>
                <div style="margin-top: 15px;">
                    <button onclick="exportData()" class="btn btn-primary">📥 Export Data</button>
                    <button onclick="clearAllData()" class="btn btn-dismiss">🗑️ Hapus Semua Data</button>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 30px;">
                <a href="/" class="btn btn-secondary">Kembali ke Beranda</a>
            </div>
        </main>
        
        <footer>
            <p>&copy; 2026 Layanan Administrasi Desa - Panel Administrator</p>
        </footer>
    </div>
    
    <script src="/style/js.js"></script>
    <script>
        let currentFilter = 'all';
        
        function loadDashboard() {
            const submissions = AppStorage.load('submissions') || [];
            
            document.getElementById('totalSubmissions').textContent = submissions.length;
            document.getElementById('pendingSubmissions').textContent = 
                submissions.filter(s => s.status === 'Menunggu Proses').length;
            document.getElementById('processedSubmissions').textContent = 
                submissions.filter(s => s.status === 'Diproses').length;
            document.getElementById('completedSubmissions').textContent = 
                submissions.filter(s => s.status === 'Selesai').length;
            
            displaySubmissions(submissions);
        }
        
        function displaySubmissions(submissions) {
            const list = document.getElementById('submissionsList');
            
            if (submissions.length === 0) {
                list.innerHTML = '<p style="text-align: center; color: #999; padding: 20px;">Tidak ada pengajuan</p>';
                return;
            }
            
            let filtered = currentFilter === 'all' ? submissions : 
                          submissions.filter(s => s.status === currentFilter);
            
            list.innerHTML = filtered.map((item, index) => {
                const statusColors = {
                    'Menunggu Proses': '#FF9800',
                    'Diproses': '#2196F3',
                    'Selesai': '#4CAF50'
                };
                
                return `
                    <div class="service-item" style="margin-bottom: 20px;">
                        <div style="display: flex; justify-content: space-between; align-items: start; flex-wrap: wrap; gap: 15px;">
                            <div style="flex: 1; min-width: 250px;">
                                <h4>${item.service.toUpperCase()}</h4>
                                <p><strong>Nama:</strong> ${item.nama}</p>
                                <p><strong>NIK:</strong> ${item.nik}</p>
                                <p><strong>Alamat:</strong> ${item.alamat}</p>
                                <p><strong>Telepon:</strong> ${item.telepon}</p>
                                <p><strong>Keperluan:</strong> ${item.keperluan}</p>
                                <p><strong>Tanggal Pengajuan:</strong> ${formatDate(item.tanggal)}</p>
                                <p><strong>Status:</strong> <span style="color: ${statusColors[item.status]}; font-weight: bold;">${item.status}</span></p>
                            </div>
                            <div style="display: flex; flex-direction: column; gap: 10px;">
                                <select onchange="updateStatus(${index}, this.value)" class="form-control" style="padding: 8px; border-radius: 5px; border: 2px solid #e0e0e0;">
                                    <option value="Menunggu Proses" ${item.status === 'Menunggu Proses' ? 'selected' : ''}>Menunggu Proses</option>
                                    <option value="Diproses" ${item.status === 'Diproses' ? 'selected' : ''}>Diproses</option>
                                    <option value="Selesai" ${item.status === 'Selesai' ? 'selected' : ''}>Selesai</option>
                                </select>
                                <button onclick="deleteSubmission(${index})" class="btn btn-dismiss" style="font-size: 0.9em; padding: 8px 15px;">Hapus</button>
                            </div>
                        </div>
                    </div>
                `;
            }).reverse().join('');
        }
        
        function updateStatus(index, newStatus) {
            let submissions = AppStorage.load('submissions') || [];
            submissions[index].status = newStatus;
            AppStorage.save('submissions', submissions);
            loadDashboard();
        }
        
        function deleteSubmission(index) {
            if (confirm('Yakin ingin menghapus pengajuan ini?')) {
                let submissions = AppStorage.load('submissions') || [];
                submissions.splice(index, 1);
                AppStorage.save('submissions', submissions);
                loadDashboard();
            }
        }
        
        function filterSubmissions(filter) {
            currentFilter = filter;
            loadDashboard();
        }
        
        function exportData() {
            const submissions = AppStorage.load('submissions') || [];
            if (submissions.length === 0) {
                alert('Tidak ada data untuk di-export');
                return;
            }
            
            const dataStr = JSON.stringify(submissions, null, 2);
            const dataBlob = new Blob([dataStr], { type: 'application/json' });
            const url = URL.createObjectURL(dataBlob);
            const link = document.createElement('a');
            link.href = url;
            link.download = `pengajuan-desa-${new Date().toISOString().split('T')[0]}.json`;
            link.click();
            URL.revokeObjectURL(url);
        }
        
        function clearAllData() {
            if (confirm('⚠️ PERINGATAN!\n\nIni akan menghapus SEMUA data pengajuan.\nApakah Anda yakin?')) {
                if (confirm('Konfirmasi sekali lagi: Hapus semua data?')) {
                    AppStorage.remove('submissions');
                    loadDashboard();
                    alert('✅ Semua data berhasil dihapus');
                }
            }
        }
        
        // Load dashboard on page load
        document.addEventListener('DOMContentLoaded', loadDashboard);
        
        // Auto-refresh every 30 seconds
        setInterval(loadDashboard, 30000);
    </script>
</body>
</html>
