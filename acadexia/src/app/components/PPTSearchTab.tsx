import { Input } from "@chakra-ui/react";
import { useState } from "react";

export default function PowerPointSearch() {
  const [searchTerm, setSearchTerm] = useState("");

  return (
    <Input
      placeholder="Search PowerPoints..."
      value={searchTerm}
      onChange={(e) => setSearchTerm(e.target.value)}
    />
  );
}
