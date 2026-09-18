/*
 * Limpeza de legado PWA.
 * Mantido temporariamente para desregistrar versões antigas do Service Worker
 * e remover o cache "microconda-shell-*". O Studio atual não registra PWA.
 */
self.addEventListener("install", event => {
  event.waitUntil(self.skipWaiting());
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
