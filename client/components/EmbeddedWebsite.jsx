'use client';

import { useState, useEffect, useRef } from 'react';

export default function IframePage() {
  const [iframeSrc, setIframeSrc] = useState('/proxy?src=https://www.techwithkunal.com');
  const iframeRef = useRef(null);

  useEffect(() => {
    const handleMessage = (event) => {
      if (event.origin !== window.location.origin) return;
      if (event.data.type === 'navigate') {
        setIframeSrc(`/proxy?src=${encodeURIComponent(event.data.url)}`);
      }
    };

    window.addEventListener('message', handleMessage);
    return () => {
      window.removeEventListener('message', handleMessage);
    };
  }, []);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Embedded Website</h1>
      <div className="border border-gray-300 rounded-lg overflow-hidden">
        <iframe
          ref={iframeRef}
          src={iframeSrc}
          width="100%"
          height="600px"
          className="border-none"
          title="Embedded Website"
        ></iframe>
      </div>
    </div>
  );
}
