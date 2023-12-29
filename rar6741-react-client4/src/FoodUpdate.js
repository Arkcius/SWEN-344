import React from 'react';
import { Row, Col, Button, Label, Input, FormGroup } from 'reactstrap';
import './App.css';

class FoodUpdate extends React.Component{
    constructor(props){
        super(props);

        this.state = {
            field: 'name',
            food: '',
            data: ''
        };

        this.handleField = this.handleField.bind(this);
        this.handleFood = this.handleFood.bind(this);
        this.handleData = this.handleData.bind(this);
    }

    handleField(event){
        this.setState({
            field: event.target.value
        });
    }

    handleFood(event){
        this.setState({
            food: event.target.value
        });
    }

    handleData(event){
        this.setState({
            data: event.target.value
        });
    }

    render(){
        return(
            <Row xs="4">
                <Col xs="auto">
                    <FormGroup>
                        <Label for="FoodName">
                            Food
                        </Label>
                        <Input id="FoodName" value={this.state.food} onChange={this.handleFood} placeholder="Input Food Name"/>
                    </FormGroup>
                </Col>

                <Col xs="auto">
                    <Label for ="Category">Category</Label>
                    <br></br>
                    <Input id="Category" type="select" value={this.state.field} onChange={this.handleField}>
                        <option>name</option>
                        <option>calories</option>
                        <option>totalFat</option>
                        <option>saturatedFat</option>
                        <option>transFat</option>
                        <option>protein</option>
                        <option>carbohydrate</option>
                    </Input>
                </Col>

                <Col xs="auto">
                    <FormGroup>
                        <Label for="Data">
                            Data
                        </Label>
                        <Input id="Data" value={this.state.data} onChange={this.handleData} placeholder="Input Data"/>
                    </FormGroup>
                </Col>

                <Col xs="auto">
                    <br></br>
                    <Button type="button" value={[this.state.food, this.state.field, this.state.data]} onClick={this.props.handleUpdate}>Submit</Button>
                </Col>
            </Row>
        );
    }
}


export default FoodUpdate;
