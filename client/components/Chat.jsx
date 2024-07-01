"use client"

import { useState, useEffect } from 'react';
import { MdDarkMode, MdLightMode } from "react-icons/md";
import { FaArrowUpLong } from "react-icons/fa6";
import { readRoot, login, selectFramework, addPage, viewPage } from '../app/api/service/route';

import ChatNav from "./ChatNav";
import EmbeddedWebsite from "./EmbeddedWebsite";
import FolderSidebar from "./FolderSidebar"
import PromptInput from "./PromptInput"



export default function Chat() {
  const [darkMode, setDarkMode] = useState(true);
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);

  return (
    <div className="flex flex-col">
      <ChatNav />
      <div className="flex">
      <FolderSidebar />
      <div className="flex-1 flex flex-col">

        <EmbeddedWebsite />
        <PromptInput />
        </div>
      </div>
    </div>

  );
}
