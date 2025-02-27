"use client";

import { Box, Flex, Tabs } from "@chakra-ui/react";
import LectureSearchTab from "@/app/components/LectureSearchTab";
import PPTSearchTab from "@/app/components/PPTSearchTab";
import React from "react"; // Import React for typing

interface TabItem {
  title: string;
  component: React.ReactNode; // More flexible than JSX.Element
}

const items: TabItem[] = [
  {
    title: "Lecture Search",
    component: <LectureSearchTab />,
  },
  {
    title: "PowerPoint Search",
    component: <PPTSearchTab />,
  },
];

const SearchTabs: React.FC = () => {
  return (
    <Flex minH="dvh">
      <Tabs.Root defaultValue="Lecture Search" width="full" variant="line">
        <Tabs.List>
          {items.map((item) => (
            <Tabs.Trigger key={item.title} value={item.title}>
              {item.title}
            </Tabs.Trigger>
          ))}
        </Tabs.List>
        <Box pos="relative" minH="200px" width="full">
          {items.map((item) => (
            <Tabs.Content
              key={item.title}
              value={item.title}
              position="absolute"
              inset="0"
              _open={{
                animationName: "fade-in, scale-in",
                animationDuration: "300ms",
              }}
              _closed={{
                animationName: "fade-out, scale-out",
                animationDuration: "120ms",
              }}
            >
              {item.component}
            </Tabs.Content>
          ))}
        </Box>
      </Tabs.Root>
    </Flex>
  );
};

export default SearchTabs;