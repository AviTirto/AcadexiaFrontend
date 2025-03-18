import { Tab, Tabs } from "react-bootstrap"

export default function SearchPage(){
    return (
        <div>
            <Tabs
                variant="underline"
                fill
                className="border-red-500 border-b-2"
            >
                <Tab 
                    eventKey="clips"
                    title={<span className="bg-inherit text-red-500">Lecture Clip Search</span>}
                >
                    <p>Lecture Clip Search</p>
                </Tab>
                <Tab 
                    eventKey="ppts" 
                    title={<span className="bg-inherit text-red-500">PPT Clip Search</span>}
                >
                    <p>PPT Clip Search</p>
                </Tab>
            </Tabs>
        </div>
    )
}