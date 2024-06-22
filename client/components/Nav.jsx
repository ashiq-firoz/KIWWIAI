'use client'
import Link from 'next/link'
import Image from 'next/image'
import { useState, useEffect } from 'react'
import { signIn, signOut, getProviders, useSession } from 'next-auth/react'
const Nav = () => {
    const [ providers, setProviders]= useState(null)
    const [toggleDropdown, setToggleDropDown] = useState(false);
    const {data : session} = useSession()
    
    useEffect(() => {
        const setUpProviders = async () => {
            const response = await getProviders();
            setProviders(response);
        }
        setUpProviders()
    },[])
    const handleToggleDropDown = () => {
        setToggleDropDown((prev) => !prev);
    };
    
    return (
        <nav className='flex top-4 fixed justify-between inset-x-0 z-10 px-5'>

            <Link href='/' className='flex gap-2 items-center flex-center'>
                <Image
                    src='/logo.svg'
                    alt='S'
                    width={40}
                    height={40}
                    className='object-contain'
                    />
                <p className='max-sm:hidden font-satoshi font-semibold text-lg text-white tracking-wide;'>KIWWI AI</p>
            </Link>

            {/* desktop view*/}
            <div className='sm:flex hidden'>
                {session?.user ?
                    <div className='flex gap-3 md:gap-5'>
                        <button type='button' onClick={signOut} className='rounded-full border border-white bg-transparent py-1.5 px-5 text-white transition-all hover:bg-white hover:text-black text-center text-sm font-inter flex items-center justify-center'>
                            Sign Out
                        </button>
                        <Link href={'/profile'}>
                            <Image src={session?.user.image} alt='profile' className='rounded-full' width={35} height={35} />
                        </Link>
                    </div>
                    :
                    <>
                        {providers && Object.values(providers).map((provider) => (
                            <button type='button' key={provider.name} onClick={()=>signIn(provider.id)} className='rounded-full border border-white bg-white py-1.5 px-5 text-black transition-all hover:bg-white hover:text-black text-center text-sm font-inter flex items-center justify-center'>
                                Sign In
                            </button>

                        ))}
                    </>
                }
            </div>
            <div className='sm:hidden flex relative'>
                {session?.user?
                <div className='flex'>
                    <Image src={session?.user.image} alt='profile' width={30} height={30} className='rounded-full' onClick={handleToggleDropDown}/>

                    {toggleDropdown &&
                    <div className='absolute right-0 top-full mt-3 w-full p-5 rounded-lg bg-black min-w-[210px] flex flex-col gap-2 justify-end items-end'>
                        <Link href={'/'} className='text-sm font-inter text-gray-700 hover:text-gray-500 font-medium' onClick={()=>setToggleDropDown(false)}>My Profile</Link>
                        <Link href={'/'} className='text-sm font-inter text-gray-700 hover:text-gray-500 font-medium' 
                        onClick={()=>{
                            setToggleDropDown(false);
                        signOut();
                        }}>Sign Out</Link>
                    </div>}
                </div>
                :
                <>
                    {providers && Object.values(providers).map((provider) => (
                        <button type='button' key={provider.name} onClick={()=>signIn(provider.id)} className='rounded-full border border-white bg-white py-1.5 px-5 text-black transition-all hover:bg-black hover:text-white text-center text-sm font-inter flex items-center justify-center'>
                                Sign In
                            </button>
                        ))}
                </>}
            </div>
        </nav>
    )
}

export default Nav