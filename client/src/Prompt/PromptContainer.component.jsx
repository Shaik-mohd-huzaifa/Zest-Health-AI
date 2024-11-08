import { useSelector } from "react-redux"
import { Prompt } from "../components/Prompt/Prompt.component"
import "./PromptContainer.Styles.scss"
import { PromptSelector } from "../store/prompt/prompt.selector"
import { useRef, useEffect } from "react"

export const PromptContainer = () => {
    const promptContainerRef = useRef(null)
    const Prompts = useSelector(PromptSelector)

    useEffect(() => {
        // Scroll to the bottom of the container whenever userPrompts change
        if (promptContainerRef.current) {
          promptContainerRef.current.scrollTop =
            promptContainerRef.current.scrollHeight;
        }
      }, [Prompts]);
    return (
        <div ref={promptContainerRef} className="prompt-container">
            {
                Prompts.map((prompt, index) => {
                    const promptClass = index % 2 == 0 ? "left-Prompt" : "Right-Prompt"

                    return (
                        <Prompt key={index} prompt={prompt} type={promptClass}/>
                    )
                })
            }
        </div>
    )
}