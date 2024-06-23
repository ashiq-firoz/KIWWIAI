import Chat from '@/components/Chat'
import React from 'react'
import { useSession } from 'next-auth/react'
const page = () => {

  return (
    <div>
      <Chat/>
    </div>
  )
}

export default page
