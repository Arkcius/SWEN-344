import React from 'react';
import './App.css';

class FoodType extends React.Component{
    constructor(props){
        super(props);
        this.state = {value: ''}
    }

    render(){
        return(
            <div>
                <label class = 'block' for='foodtype'>Food Types</label>
                <select id="foodtype" onChange={this.props.handleChange}>
                    <option value = "Blank" selected disabled hidden>Blank</option>
                    <option value="Protein">Protein</option>
                    <option value="Fruits">Fruits</option>
                    <option value="Vegetables">Vegetables</option>
                    <option value="Dairy">Dairy</option>
                    <option value="Grains">Grains</option>
            </select>
        </div>
        );
    }
}

export default FoodType