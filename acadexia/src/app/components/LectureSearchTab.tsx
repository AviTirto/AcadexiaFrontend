"use client";

import { Input } from "@chakra-ui/react";
import { useState } from "react";

export default function LectureSearch() {
  const [searchTerm, setSearchTerm] = useState("");

  return (
    <Input
      placeholder="Search lectures..."
      value={searchTerm}
      onChange={(e) => setSearchTerm(e.target.value)}
      variant="subtle"
    />
  );
}
