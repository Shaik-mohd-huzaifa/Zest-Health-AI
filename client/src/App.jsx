import './App.css'
import {Route, Routes} from "react-router-dom"
import { HomePage } from './components/Home/Home.component'
import { Dashboard } from './components/Dashboard/Dashboard.component'
import { Appointments } from './components/Appointments/Appointments.components';
import { Chat } from './components/Chat/Chat.component';

const NotFound = () => <div>404 - Page Not Found</div>;

function App() {
  return (
    <Routes>
      <Route path='/' element={<HomePage/>}/>
      <Route path='dashboard' element={<Dashboard/>}>
      <Route index element={<Appointments/>}/>
      <Route path='appointments' element={<Appointments/>}/>
      <Route path='chat' element={<Chat/>}/>
      </Route>
      <Route path="*" element={<NotFound />} />
    </Routes>
  )
}

export default App
