import React from 'react';
import './App.css';
import Nutrikit from './Nutirkit';

function Food(){
    return(
        <div>
            <Nutrikit proteins={[]} fruits={[]} vegetables={[]} dairy={[]} grains={[]}/>
        </div>
    )
}

export default Food;