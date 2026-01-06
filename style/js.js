// PWA utility functions and app functionality

// Check if app is running as PWA
function isPWA() {
    return window.matchMedia('(display-mode: standalone)').matches || 
           window.navigator.standalone === true;
}

// Show notification if supported
function showNotification(title, options) {
    if ('Notification' in window && Notification.permission === 'granted') {
        new Notification(title, options);
    }
}

// Request notification permission
function requestNotificationPermission() {
    if ('Notification' in window && Notification.permission === 'default') {
        Notification.requestPermission().then(permission => {
            if (permission === 'granted') {
                showNotification('Administrasi Desa', {
                    body: 'Notifikasi berhasil diaktifkan!',
                    icon: '/icons/icon-192x192.png'
                });
            }
        });
    }
}

// Update UI based on online/offline status
function updateConnectionStatus() {
    const isOnline = navigator.onLine;
    const statusBanner = document.getElementById('connectionStatus');
    
    if (statusBanner) {
        if (!isOnline) {
            statusBanner.style.display = 'block';
            statusBanner.textContent = '⚠️ Mode Offline - Data akan disinkronkan saat online';
            statusBanner.style.background = '#ff9800';
        } else {
            statusBanner.style.display = 'none';
        }
    }
}

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    // Check PWA status
    if (isPWA()) {
        console.log('Running as PWA');
    }
    
    // Update connection status
    updateConnectionStatus();
    
    // Listen for connection changes
    window.addEventListener('online', updateConnectionStatus);
    window.addEventListener('offline', updateConnectionStatus);
    
    // Add smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});

// Form validation helper
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return false;
    
    const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            input.style.borderColor = '#f44336';
        } else {
            input.style.borderColor = '#e0e0e0';
        }
    });
    
    return isValid;
}

// Local storage helper functions
const AppStorage = {
    save: (key, data) => {
        try {
            localStorage.setItem(key, JSON.stringify(data));
            return true;
        } catch (e) {
            console.error('Storage error:', e);
            return false;
        }
    },
    
    load: (key) => {
        try {
            const data = localStorage.getItem(key);
            return data ? JSON.parse(data) : null;
        } catch (e) {
            console.error('Storage error:', e);
            return null;
        }
    },
    
    remove: (key) => {
        try {
            localStorage.removeItem(key);
            return true;
        } catch (e) {
            console.error('Storage error:', e);
            return false;
        }
    }
};

// Show loading indicator
function showLoading() {
    const loader = document.createElement('div');
    loader.id = 'appLoader';
    loader.className = 'loading';
    loader.style.position = 'fixed';
    loader.style.top = '50%';
    loader.style.left = '50%';
    loader.style.transform = 'translate(-50%, -50%)';
    loader.style.zIndex = '9999';
    document.body.appendChild(loader);
}

// Hide loading indicator
function hideLoading() {
    const loader = document.getElementById('appLoader');
    if (loader) {
        loader.remove();
    }
}

// Format date to Indonesian format
function formatDate(date) {
    const options = { 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric',
        timeZone: 'Asia/Jakarta'
    };
    return new Date(date).toLocaleDateString('id-ID', options);
}

// Export functions for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        isPWA,
        showNotification,
        requestNotificationPermission,
        validateForm,
        AppStorage,
        showLoading,
        hideLoading,
        formatDate
    };
}
