import { Tabs, TabsContent, TabsList2, TabsTrigger2 } from "@/components/ui/tabs"
import { SearchBar } from "@/components/searchbar"
import { Clip } from "@/components/clip"
import { useState } from "react"
import { fetchClips, postFeedback } from "./api"

interface ClipRes {
  embed_link: string,
  start_time: string,
  end_time: string,
  explanation: string
}

function App() {
  const [openTab, setOpenTab] = useState("clips")
  const [ clips, setClips ] = useState<ClipRes[]>([])
  const [ clipLikes, setClipLikes ] = useState<number>(0)
  const [ clipDislikes, setClipDislikes ] = useState<number>(0)

  const clipSearch = async (prevQuery: string, query: string) => {
    console.log("clipSearch called")
    if (prevQuery){
      setClipLikes(0)
      setClipDislikes(0)
      await postFeedback(prevQuery, clipLikes, clipDislikes, clips.length)
    }
    const res = await fetchClips(query)
    console.log(res)
    setClips(res)

  } 
  
  const slideSearch = (query: string) => {
    const res = fetchClips(query)
    console.log(res)
  }  

  const addLike = () => {
    setClipLikes(prevLikes => prevLikes + 1)
  }

  const addDislike = () => {
    setClipDislikes(prevDislikes => prevDislikes + 1)
  }

  return (
    <div style={{padding: "20rem"}} className="flex flex-col items-center justify-center w-full">
      <h1 className="text-2xl font-bold mb-4">{ openTab === "clips" ? "Econ 301 Lecture Clip Search" : "Econ 301 PPT Slide Search"}</h1>
      <Tabs defaultValue="account" className="w-full" onValueChange={setOpenTab}>
        <TabsList2>
          <TabsTrigger2 value="clips">Lecture Clip Search</TabsTrigger2>
          <TabsTrigger2 value="slides">PPT Slide Search</TabsTrigger2>
        </TabsList2>
        <TabsContent value="clips">
          <SearchBar placeholder="Find me clips about..." onSearch={clipSearch}/>
          {
            clips.map(
              (clip, index) => {
                return <Clip key={clip.embed_link + index} embedLink = {clip.embed_link} startTime = {clip.start_time} endTime= {clip.end_time} explanation = {clip.explanation} addLike={addLike} addDislike={addDislike}/>
              }
            )
          }
        </TabsContent>
        <TabsContent value="slides">
          <SearchBar placeholder="Find me slides about..." onSearch={fetchClips}/>
        </TabsContent>
      </Tabs>
    </div>
  )
}

export default App
