'use client'
import Link from 'next/link'
import Image from 'next/image'
import { useState, useEffect } from 'react'
import { signOut, useSession } from 'next-auth/react'
import { MdDarkMode, MdLightMode } from "react-icons/md";

const ChatNav = () => {
    const [toggleDropdown, setToggleDropDown] = useState(false);
    const { data: session } = useSession()
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const [darkMode, setDarkMode] = useState(true);

    const sendMessage = (e) => {
        e.preventDefault();
        if (input.trim() !== '') {
            setMessages([...messages, { text: input, sender: 'User' }]);
            setInput('');
        }
    };

    useEffect(() => {
        if (darkMode) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
    }, [darkMode]);
    const handleToggleDropDown = () => {
        setToggleDropDown((prev) => !prev);
    };


    return (
        <nav className='flex py-2 fixed justify-between inset-x-0 z-10 px-5 bg-white dark:bg-gray-900'>

            <Link href='/' className='flex gap-2 items-center flex-center'>
                <Image
                    src='/logo.svg'
                    alt='S'
                    width={40}
                    height={40}
                    className='object-contain'
                />
                <p className='max-sm:hidden font-satoshi font-semibold text-lg text-black dark:text-white tracking-wide;'>KIWWI AI</p>
            </Link>

            {/* desktop view*/}
            <div className='sm:flex hidden'>
                <div className='flex gap-3 md:gap-5'>
                    <button
                        onClick={() => setDarkMode(!darkMode)}
                        className="px-4 py-2 rounded text-black dark:text-white"
                    >
                        {darkMode ? <MdLightMode /> : <MdDarkMode />}
                    </button>
                    <button type='button' onClick={signOut} className='rounded-full border border-black dark:border-white bg-transparent py-1.5 px-5 text-black dark:text-white transition-all hover:bg-gray-700 dark:hover:bg-white hover:text-white dark:hover:text-black text-center text-sm font-inter flex items-center justify-center'>
                        Sign Out
                    </button>
                    <Link href={'/profile'}>
                        <Image src={session?.user.image} alt='profile' className='rounded-full' width={35} height={35} />
                    </Link>
                </div>
            </div>
            <div className='sm:hidden flex relative'>
                <div className='flex'>
                    <Image src={session?.user.image} alt='profile' width={30} height={30} className='rounded-full' onClick={handleToggleDropDown} />

                    {toggleDropdown &&
                        <div className='absolute right-0 top-full mt-3 w-full p-5 rounded-lg bg-black min-w-[210px] flex flex-col gap-2 justify-end items-end'>
                            <button
                                onClick={() => setDarkMode(!darkMode)}
                                className="px-4 py-2 rounded text-black dark:text-white"
                            >
                                {darkMode ? <MdLightMode /> : <MdDarkMode />}
                            </button>
                            <Link href={'/'} className='text-sm font-inter text-gray-700 hover:text-gray-500 font-medium' onClick={() => setToggleDropDown(false)}>My Profile</Link>
                            <Link href={'/'} className='text-sm font-inter text-white dark:text-gray-700 hover:text-gray-500 font-medium'
                                onClick={() => {
                                    setToggleDropDown(false);
                                    signOut();
                                }}>Sign Out</Link>
                        </div>}
                </div>

            </div>
        </nav>
    )
}

export default ChatNav