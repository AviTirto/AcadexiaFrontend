import { Box } from "@chakra-ui/react";
import SearchTabs from "./components/SearchTabs";

export default function Home() {
  return (
    <Box p={4} maxW="600px" mx="auto">
      <SearchTabs />
    </Box>
  );
}
