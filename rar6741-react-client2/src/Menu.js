import React from 'react';
import './App.css';

class Menu extends React.Component{
    constructor(props){
        super(props);
        this.state = {value:''};
    }

    adder(calories, food){
        return(
            <option value={calories}>{food}</option>
        )
    }

    editMenu(foods){
        var menu = foods.foods;
        var food;
        var calories;
        let opti = [];
        if(menu.length>0){
            for(var i=0;i<menu.length;i++){
                food = menu[i].food;
                calories = menu[i].calories;
                opti.push(<option value ={calories}>{food}</option>)
            }
            return opti;
        }
        return <option>Select A Category</option>
    }

    render(){
        return(
        <div>
        <label class='block' for="selectedType">Menu Items</label>
            <select class = 'select' id="selectedType" size = {5} onChange={this.props.handleChange}>
                <this.editMenu foods={this.props.foods}/>
            </select>
        </div>
        );
    }
}

export default Menu;