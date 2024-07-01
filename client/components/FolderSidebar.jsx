// components/FolderSidebar.tsx
import React, { useState } from 'react';
import { FaBars } from "react-icons/fa";

const FolderSidebar = () => {
  const [isOpen, setIsOpen] = useState(true); // Initially open

  const toggleSidebar = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className={`h-full bg-gray-200 p-4 ${isOpen ? 'w-64' : 'w-16'}`}>
      {/* Button to toggle sidebar */}
      
      <button
        className="text-black my-auto"
        onClick={toggleSidebar}
      > <FaBars />
      </button>
      {/* Placeholder for folder list */}
      {isOpen && (
        <>
          <p className="text-gray-600 mt-4">Folders</p>
          {/* Add your folder list component here */}
        </>
      )}
    </div>
  );
};

export default FolderSidebar;
