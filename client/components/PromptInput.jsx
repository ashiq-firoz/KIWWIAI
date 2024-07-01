import React from 'react'
import { FaArrowUpLong } from "react-icons/fa6";
import { useState} from 'react';

const PromptInput = () => {
    
  const [input, setInput] = useState('');

  const sendMessage = async (e) => {
    e.preventDefault();
    if (input.trim() !== '') {
      setMessages([...messages, { text: input, sender: 'User' }]);
      setInput('');
    }
    try {
      const response = await addPage('This is a test page', 'TestPage');
      console.log(response);
    } catch (error) {
      console.error('Error adding page:', error);
    }
  };

  return (
    <div className='w-full m-2'>
    <form className="flex p-2 w-3/5 mx-auto border border-gray-300 bg-white dark:bg-gray-800 dark:border-gray-600 rounded-3xl" onSubmit={sendMessage}>
            <input
              type="text"
              className="flex-1 px-4 py-2 border  text-black dark:text-white dark:bg-gray-800 outline-none border-none"
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
  )
}

export default PromptInput
