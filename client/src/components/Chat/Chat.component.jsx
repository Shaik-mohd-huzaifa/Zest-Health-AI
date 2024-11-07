import { PromptContainer } from "../../Prompt/PromptContainer.component"
import PromptInput from "../Prompt Input/PromptInput.component"
import "./Chat.styles.scss"

export const Chat = () => {
    return (
        <div className="chat-container">
            <div className="prompt-container">
                <PromptContainer/>
            </div>
            <div className="input-container">
                
                <PromptInput/>
            </div>
        </div>
    )
}