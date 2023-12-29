import React from 'react';
import './App.css';
import Nutrikit from './Nutirkit';

function Food(){
    return(
        <div>
            <Nutrikit 
            proteins={[{'food' : 'steak', 'calories' : 300},
            {'food' : 'ground beef', 'calories' : 200},
            {'food' : 'chicken', 'calories' : 100},
            {'food' : 'fish', 'calories' : 80},
            {'food' : 'soy', 'calories' : 50}]}
            fruits={[{'food' : 'orange', 'calories' : 300},
            {'food' : 'banana', 'calories' : 200},
            {'food' : 'pineapple', 'calories' : 100},
            {'food' : 'grapes', 'calories' : 80},
            {'food' : 'blueberries', 'calories' : 50}]}
            vegetables={[{'food' : 'romaine', 'calories' : 30},
            {'food' : 'green beans', 'calories' : 40},
            {'food' : 'squash', 'calories' : 100},
            {'food' : 'spinach', 'calories' : 50},
            {'food' : 'kale', 'calories' : 10}]}
            dairy={[{'food' : 'milk', 'calories' : 300},
            {'food' : 'yogurt', 'calories' : 200},
            {'food' : 'cheddar cheese', 'calories' : 200},
            {'food' : 'skim milk', 'calories' : 100},
            {'food' : 'cottage cheese', 'calories' : 80}]}
            grains={[ {'food' : 'bread', 'calories' : 200},
            {'food' : 'bagel', 'calories' : 300},
            {'food' : 'pita', 'calories' : 250},
            {'food' : 'naan', 'calories' : 210},
            {'food' : 'tortilla', 'calories' : 120}]}
            />
        </div>
    )
}

export default Food;