"use client";

import { useState, useEffect } from "react";

export default function Home() {
  console.log("component render");

  const [count, setCount] = useState(0);

  const increment = () => {
    setCount(count + 1);
  };

  useEffect(() => {
    console.log("effect mounted");

    return () => {
      console.log("cleanup");
    };
  }, []);

  return (
    <main className="p-10">
      <h1 className="text-2xl font-bold">Render Test</h1>
      <p className="mt-4">Count: {count}</p>
      <button
        onClick={increment}
        className="mt-4 bg-black text-white px-4 py-2 rounded"
      >
        Increment
      </button>
    </main>
  );
}
