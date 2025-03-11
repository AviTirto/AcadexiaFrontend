import {
  Accordion2,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion"

import { Button } from "@/components/ui/button"
import { useState } from "react"

interface ClipProps {
  embedLink: string,
  startTime: string,
  endTime: string,
  explanation: string,
  addLike: () => (void),
  addDislike: () => (void)
}

export function Clip(props: ClipProps) {
    const handleLike = () => {
      props.addLike()
      setFeedback(true)
    }

    const handleDislike = () => {
      props.addDislike()
      setFeedback(true)
    }

    const [feedback, setFeedback] = useState(false)
    return(
        <Accordion2 type="single" collapsible>
            <AccordionItem value="item-1">
              <AccordionTrigger>{`${props.startTime} - ${props.endTime}`}</AccordionTrigger>
              <AccordionContent>
                <div dangerouslySetInnerHTML={{__html: props.embedLink}}></div>
                <br/>
                <p>
                  {props.explanation}
                </p>
                {
                  feedback ? 
                  <p>Thank you for the feedback!</p>
                  :
                  (
                    <div className="flex">
                      <Button onClick={handleLike}>👍</Button>
                      <Button onClick={handleDislike}>👎</Button>
                    </div>
                  )
                }
              </AccordionContent>
            </AccordionItem>
        </Accordion2>
    )
}