// MicroConda não usa PWA/service worker.
// Este arquivo existe apenas para limpar instalações/cache antigos.
self.addEventListener("install", event => {
  self.skipWaiting();
});

self.addEventListener("activate", event => {
  event.waitUntil((async () => {
    try {
      const keys = await caches.keys();
      await Promise.all(
        keys
          .filter(key => key.startsWith("microconda-shell-"))
          .map(key => caches.delete(key))
      );
    } finally {
      await self.registration.unregister();
    }
  })());
});
