import React from 'react';
import './App.css';
import { Input, Label } from 'reactstrap';

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
        var id;
        var calories;
        let opti = [];
        if(menu.length>0){
            for(var i=0;i<menu.length;i++){
                food = menu[i].name;
                calories = menu[i].calories;
                id = menu[i].id;
                opti.push(<option value ={calories}>{food}</option>)
            }
            return opti;
        }
        return <option>Select A Category</option>
    }

    render(){
        return(
        <div>
        <Label class='block' for="selectedType">Menu Items</Label>
            <Input type="select" multiple class = 'select' id="selectedType" size = {5} onChange={this.props.handleChange}>
                <this.editMenu foods={this.props.foods}/>
            </Input>
        </div>
        );
    }
}

export default Menu;