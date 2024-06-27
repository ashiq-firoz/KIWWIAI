"use client"

import { useState, useEffect } from 'react';
import {MdDarkMode , MdLightMode } from "react-icons/md";
import { FaArrowUpLong } from "react-icons/fa6";
import { readRoot, login, selectFramework, addPage, viewPage } from '../app/api/service/route';

import ChatNav from "./ChatNav";


export default function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [darkMode, setDarkMode] = useState(true);

  const sendMessage = async (e) => {
    e.preventDefault();
    if (input.trim() !== '') {
      setMessages([...messages, { text: input, sender: 'User' }]);
      setInput('');}
    try {
      const response = await addPage('This is a test page', 'TestPage');
      console.log(response);
    } catch (error) {
      console.error('Error adding page:', error);
    }
  };


  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);

  return (
    <div className='flex h-screen dark:bg-gray-900 bg-gray-100'>
      <ChatNav/>
      <div className="m-auto w-full max-w-xl bg-white dark:bg-gray-900 rounded-lg shadow-lg">
        

        <div className="flex flex-col h-96 overflow-y-auto p-4 dark:bg-gray-800 dark:text-white">
          {messages.map((message, index) => (
            <div
              key={index}
              className={`mb-2 p-2  rounded-2xl ${
                message.sender === 'User'
                  ? 'bg-gray-200 dark:bg-gray-600 text-black dark:text-white self-end'
                  : 'bg-gray-200 dark:bg-gray-700 self-start'
              }`}
            >
              {message.text}
            </div>
          ))}
        </div>
        <form className="flex p-4 border-t border-gray-200 dark:border-gray-700" onSubmit={sendMessage}>
          <input
            type="text"
            className="flex-1 px-4 py-2 border bg-white text-black dark:text-white dark:bg-gray-800 border-gray-300 dark:border-gray-600 rounded-l-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            value={input}
            placeholder='Message Kiwwi'
            onChange={(e) => setInput(e.target.value)}
          />
          <button
            type="submit"
            disabled={input.title}
            className="px-3 py-2  text-white dark:text-black dark:bg-white bg-black   rounded-full"
          >
            <FaArrowUpLong />
          </button>
        </form>
      </div>
    </div>
  );
}
