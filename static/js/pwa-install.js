// PWA Installation Handler for BardSpeak
// Handles app installation prompt and service worker registration

let deferredPrompt;
let installButton;

// Register Service Worker
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/static/sw.js')
      .then((registration) => {
        console.log('✅ Service Worker registered:', registration.scope);
        
        // Check for updates
        registration.addEventListener('updatefound', () => {
          const newWorker = registration.installing;
          newWorker.addEventListener('statechange', () => {
            if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
              // New version available
              showUpdateNotification();
            }
          });
        });
      })
      .catch((error) => {
        console.error('❌ Service Worker registration failed:', error);
      });
  });
}

// Capture install prompt
window.addEventListener('beforeinstallprompt', (e) => {
  console.log('📱 Install prompt available');
  
  // Prevent default prompt
  e.preventDefault();
  
  // Store the event
  deferredPrompt = e;
  
  // Show custom install button
  showInstallButton();
});

// Show install button
function showInstallButton() {
  // Create install button if it doesn't exist
  if (!document.getElementById('pwa-install-btn')) {
    const installBtn = document.createElement('button');
    installBtn.id = 'pwa-install-btn';
    installBtn.className = 'btn btn-primary btn-lg';
    installBtn.innerHTML = '<i class="fas fa-download me-2"></i>Install App';
    installBtn.style.cssText = `
      position: fixed;
      bottom: 20px;
      right: 20px;
      z-index: 1000;
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
      animation: pulse 2s infinite;
    `;
    
    installBtn.addEventListener('click', installApp);
    document.body.appendChild(installBtn);
    installButton = installBtn;
  }
}

// Install app
async function installApp() {
  if (!deferredPrompt) {
    console.log('❌ No install prompt available');
    return;
  }
  
  // Show install prompt
  deferredPrompt.prompt();
  
  // Wait for user response
  const { outcome } = await deferredPrompt.userChoice;
  console.log(`📱 User response: ${outcome}`);
  
  if (outcome === 'accepted') {
    console.log('✅ App installed successfully');
    showSuccessMessage('App installed! You can now use BardSpeak offline.');
  } else {
    console.log('❌ App installation declined');
  }
  
  // Clear the prompt
  deferredPrompt = null;
  
  // Hide install button
  if (installButton) {
    installButton.remove();
  }
}

// App installed event
window.addEventListener('appinstalled', (e) => {
  console.log('✅ BardSpeak PWA installed');
  
  // Hide install button
  if (installButton) {
    installButton.remove();
  }
  
  // Show success message
  showSuccessMessage('Welcome to BardSpeak! The app is now installed on your device.');
  
  // Track installation (optional analytics)
  if (typeof gtag !== 'undefined') {
    gtag('event', 'pwa_install', {
      'event_category': 'engagement',
      'event_label': 'PWA Installation'
    });
  }
});

// Check if app is installed
function isAppInstalled() {
  // Check if running in standalone mode
  return window.matchMedia('(display-mode: standalone)').matches ||
         window.navigator.standalone === true;
}

// Show update notification
function showUpdateNotification() {
  const updateBanner = document.createElement('div');
  updateBanner.className = 'alert alert-info';
  updateBanner.style.cssText = `
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 9999;
    max-width: 90%;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
  `;
  updateBanner.innerHTML = `
    <i class="fas fa-sync-alt me-2"></i>
    <strong>Update Available!</strong> 
    <button class="btn btn-sm btn-primary ms-2" onclick="location.reload()">
      Update Now
    </button>
    <button class="btn btn-sm btn-secondary ms-1" onclick="this.parentElement.remove()">
      Later
    </button>
  `;
  
  document.body.appendChild(updateBanner);
  
  // Auto-remove after 10 seconds
  setTimeout(() => {
    if (updateBanner.parentElement) {
      updateBanner.remove();
    }
  }, 10000);
}

// Show success message
function showSuccessMessage(message) {
  const successBanner = document.createElement('div');
  successBanner.className = 'alert alert-success';
  successBanner.style.cssText = `
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 9999;
    max-width: 90%;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
  `;
  successBanner.innerHTML = `
    <i class="fas fa-check-circle me-2"></i>
    ${message}
  `;
  
  document.body.appendChild(successBanner);
  
  // Auto-remove after 5 seconds
  setTimeout(() => {
    successBanner.remove();
  }, 5000);
}

// Check online/offline status
window.addEventListener('online', () => {
  console.log('✅ Back online');
  showSuccessMessage('You are back online!');
  
  // Sync pending submissions
  if ('serviceWorker' in navigator && 'sync' in ServiceWorkerRegistration.prototype) {
    navigator.serviceWorker.ready.then((registration) => {
      return registration.sync.register('sync-submissions');
    });
  }
});

window.addEventListener('offline', () => {
  console.log('❌ Offline mode');
  showOfflineMessage();
});

function showOfflineMessage() {
  const offlineBanner = document.createElement('div');
  offlineBanner.className = 'alert alert-warning';
  offlineBanner.id = 'offline-banner';
  offlineBanner.style.cssText = `
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 9999;
    max-width: 90%;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
  `;
  offlineBanner.innerHTML = `
    <i class="fas fa-wifi-slash me-2"></i>
    <strong>Offline Mode</strong> - Some features may be limited.
  `;
  
  document.body.appendChild(offlineBanner);
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  // Check if already installed
  if (isAppInstalled()) {
    console.log('✅ Running as installed PWA');
  } else {
    console.log('📱 Running in browser - install prompt will appear');
  }
  
  // Check online status
  if (!navigator.onLine) {
    showOfflineMessage();
  }
});

// Add CSS animation for install button
const style = document.createElement('style');
style.textContent = `
  @keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
  }
`;
document.head.appendChild(style);

console.log('📱 PWA Install script loaded');
