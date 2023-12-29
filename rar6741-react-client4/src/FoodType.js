import React from 'react';
import './App.css';
import { Input,Label } from 'reactstrap';

class FoodType extends React.Component{
    constructor(props){
        super(props);
        this.state = {value: ''}
    }

    render(){
        return(
            <div>
                <Label class = 'block' for='foodtype'>Food Types</Label>
                <Input type="select" id="foodtype" onChange={this.props.handleChange}>
                    <option value = "Blank" selected disabled hidden>Blank</option>
                    <option value="Protein">Protein</option>
                    <option value="Fruits">Fruits</option>
                    <option value="Vegetables">Vegetables</option>
                    <option value="Dairy">Dairy</option>
                    <option value="Grains">Grains</option>
                </Input>
        </div>
        );
    }
}

export default FoodType