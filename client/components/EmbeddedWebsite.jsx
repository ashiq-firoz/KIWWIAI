'use client';

import { useState, useRef } from 'react';


export default function IframePage() {
  const [iframeSrc, setIframeSrc] = useState('https://example.com/');
  const iframeRef = useRef(null);

  return (
    <div className="h-full">
        <iframe
          ref={iframeRef}
          src={iframeSrc}
          width="100%"
          height="600px"
          className="border-none"
          title="Embedded Website"
        ></iframe>
    </div>
  );
}
