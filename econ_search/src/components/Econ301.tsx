import { Outlet } from 'react-router-dom';
import { useState } from 'react';
import Econ301Context from '../contexts/Econ301Context'

export default function Econ301(){
    const [likes, setLikes] = useState<number>(0);

    return (
        <div>
            <Econ301Context.Provider value={likes}>
                <Outlet />
            </Econ301Context.Provider>
        </div>
    )
}