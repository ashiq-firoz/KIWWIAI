"use client";

import { motion } from "framer-motion";
import React from "react";
import { AuroraBackground } from "./ui/aurora-background";
import Link from "next/link";
import { FaArrowUpLong } from "react-icons/fa6";

export function Hero() {

  return (
    <AuroraBackground>
      <motion.div
        initial={{ opacity: 0.0, y: 40 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{
          delay: 0.1,
          duration: 0.8,
          ease: "easeInOut",
        }}
        className="relative flex flex-col gap-4 items-center justify-center px-4"
      >
        <div className="flex flex-col md:flex-row justify-between w-screen mx-3">
          <div className="flex flex-col gap-7 w-1/2 px-36 text-white mx-auto text-wrap">
            <h4 className="text-[2.4rem] font-semibold">Lorem ipsum dolor sit amet consectetur </h4>
            <p className="text-[1.1rem]">Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorem quisquam natus facilis nostrum non accusantium nihil, excepturi vitae beatae reprehenderit numquam sapiente corrupti. Saepe atque aperiam fugit itaque dignissimos harum.</p>
            <button className="rounded-3xl bg-blue-500 text-center align-middle font-bold w-1/4 p-3">
              <Link href="chat">Get Kiwwi+</Link>
              
            </button>
          </div>

          <div className="w-1/2  px-10
          ">
            <form className="flex p-4 border bg-white text-black  rounded-2xl border-gray-300 dark:border-gray-600  focus:outline-none focus:ring-2">
              <input
                type="text"
                className="flex-1 bg-white outline-none"
                placeholder='Message Kiwwi'

              />
              <button
                type="submit"
                className=" text-black bg-white  rounded-full"
              >
                Generate
              </button>
            </form>
          </div>
        </div>
      </motion.div>
    </AuroraBackground>
  );
}

