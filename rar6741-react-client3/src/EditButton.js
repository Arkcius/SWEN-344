import React from 'react';
import './App.css';
import {Button} from 'reactstrap';


const EditButton = (props) => {
    
    const getButAdd = () => {
        if(props.buttonType){
            return <Button color="success" onClick={props.handleChange} active>Add</Button>
        }else{
            return <Button color="dark" onClick={props.handleChange} disabled>Add</Button>
        }
    }

    const getButRem = () => {
        if(props.buttonType){
            return <Button color="dark" onClick={props.handleChange} disabled>Remove</Button>
        }else{
            return <Button color="success" onClick={props.handleChange} active>Remove</Button>
        }
    }


    return (
        <div>
            <br></br>
            {getButAdd()}{' '}
            <br></br>
            {getButRem()}{' '}
        </div>
    );
}



export default EditButton;