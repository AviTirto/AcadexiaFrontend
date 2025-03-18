import { HashRouter, Route, Routes } from 'react-router-dom'
import SearchPage from './SearchPage' // Adjust the path as necessary

export default function Router(){
    return (
        <HashRouter>
            <Routes>
                <Route path="/" element={<SearchPage/>}></Route>
            </Routes>
        </HashRouter>
    )
}