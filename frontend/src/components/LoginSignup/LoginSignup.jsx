import { useState } from "react";

function LoginSignup() {
  const [action, setAction] = useState("Sign Up");
  return (
    <div className="bg-gradient-to-b from-white to-slate-400 min-h-screen">
      <div className="border-2 border-slate-500">
        <h1 className="text-center">{action}</h1>
      </div>
    </div>
  );
}

export default LoginSignup;
