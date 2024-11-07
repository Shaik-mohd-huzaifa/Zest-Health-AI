import { Link } from "react-router-dom"
import "./sideBar.styles.scss"
import { SlCalender } from "react-icons/sl";
import { BiSolidMessageSquareDots } from "react-icons/bi";





export const SideBar = () => {
    return (
        <div className="sidebar">
            <div className="header">
            <img src="/logo.jpg" alt="" />
<h2>Dyno Health AI</h2>
            </div>
            <ul>
                <li><SlCalender/><Link to="/dashboard">Appointments</Link></li>
                <li><BiSolidMessageSquareDots/>
<Link to="chat">Chat</Link></li>
</ul>
</div>
    )
} 
