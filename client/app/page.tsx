import Image from "next/image";
import Nav from "@/components/Nav";
import { Hero } from "@/components/Hero";

export default function Home() {
  return (
    <main className="relative bg-black-100 flex justify-center items-center flex-col overflow-hidden mx-auto">
      <div className="w-full">
    <Nav/>
    <Hero/>
    
    </div>
    </main>
  );
}
