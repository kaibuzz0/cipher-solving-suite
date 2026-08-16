/* Progressive Web App bootstrap. Keeps install functionality separate from the workspace UI. */
(() => {
  const head = document.head;

  if (!document.querySelector('link[rel="manifest"]')) {
    const manifest = document.createElement('link');
    manifest.rel = 'manifest';
    manifest.href = 'manifest.webmanifest';
    head.appendChild(manifest);
  }

  const ensureMeta = (name, content) => {
    if (document.querySelector(`meta[name="${name}"]`)) return;
    const meta = document.createElement('meta');
    meta.name = name;
    meta.content = content;
    head.appendChild(meta);
  };
  ensureMeta('mobile-web-app-capable', 'yes');
  ensureMeta('apple-mobile-web-app-capable', 'yes');
  ensureMeta('apple-mobile-web-app-status-bar-style', 'black-translucent');
  ensureMeta('apple-mobile-web-app-title', 'Cipher Suite');

  if (!document.querySelector('link[rel="apple-touch-icon"]')) {
    const icon = document.createElement('link');
    icon.rel = 'apple-touch-icon';
    icon.href = 'icons/app-icon-192.png';
    head.appendChild(icon);
  }

  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('service-worker.js', { scope: './' }).catch((error) => {
        console.warn('Cipher Suite service worker registration failed:', error);
      });
    });
  }

  let installPrompt = null;
  let installButton = null;

  const removeButton = () => {
    installButton?.remove();
    installButton = null;
  };

  const addInstallButton = () => {
    if (installButton || !installPrompt) return;
    const titleStatus = document.querySelector('.title-status');
    const titlebar = document.querySelector('.titlebar');
    if (!titlebar) return;

    installButton = document.createElement('button');
    installButton.type = 'button';
    installButton.textContent = '⊞ Install';
    installButton.title = 'Install Cipher Suite as an app';
    installButton.setAttribute('aria-label', 'Install Cipher Suite as an app');
    installButton.style.cssText = 'border:1px solid #3c3c3c;background:#252526;color:#d4d4d4;padding:3px 8px;font:11px "Segoe UI",sans-serif;cursor:pointer;margin-left:8px;white-space:nowrap';
    if (titleStatus) titlebar.insertBefore(installButton, titleStatus);
    else titlebar.appendChild(installButton);

    installButton.addEventListener('click', async () => {
      if (!installPrompt) return;
      installPrompt.prompt();
      await installPrompt.userChoice;
      installPrompt = null;
      removeButton();
    });
  };

  window.addEventListener('beforeinstallprompt', (event) => {
    event.preventDefault();
    installPrompt = event;
    addInstallButton();
  });

  window.addEventListener('appinstalled', () => {
    installPrompt = null;
    removeButton();
  });
})();
