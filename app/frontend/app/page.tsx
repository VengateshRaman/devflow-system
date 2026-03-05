"use client";
import { memo, useState } from "react";

const Child = memo(function Child() {
  console.log("Child Rendered");
  return <div className="mt-4">I am child</div>;
});

export default function Home() {
  console.log("Parent Rendered");

  const [count, setCount] = useState(0);

  return (
    <main className="p-10">
      <h1 className="text-2xl font-bold">Parent → Child Test</h1>
      <p className="mt-4">Count: {count}</p>
      <button
        onClick={() => setCount(count + 1)}
        className="mt-4 bg-black text-white px-4 py-2 rounded"
      >
        Increment
      </button>

      <Child />
    </main>
  );
}
