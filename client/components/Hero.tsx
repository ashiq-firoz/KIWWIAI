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


            <button className="relative inline-flex h-12 w-1/3 overflow-hidden rounded-full p-[1px] hover:outline-none hover:ring-2 hover:ring-slate-400 hover:ring-offset-2 hover:ring-offset-slate-50">
              <span className="absolute inset-[-1000%] animate-[spin_2s_linear_infinite] bg-[conic-gradient(from_90deg_at_50%_50%,#E2CBFF_0%,#393BB2_50%,#E2CBFF_100%)]" />
              <span className="inline-flex h-full w-full cursor-pointer items-center justify-center rounded-full bg-slate-950 px-3 py-1 text-sm font-medium text-white backdrop-blur-3xl">
                <Link href="\chat">Get Kiwwi+</Link>
              </span>
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

