import React, { createContext, useState, useContext } from 'react';

// Create a context
const Econ301Context = createContext();

// Create a provider component
export function Econ301Provider({ children }) {
  const [dummyState, setDummyState] = useState("This is a dummy state");

  return (
    <AppContext.Provider value={{ dummyState, setDummyState }}>
      {children}
    </AppContext.Provider>
  );
}