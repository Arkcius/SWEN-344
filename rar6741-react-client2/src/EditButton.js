import React from 'react';
import './App.css';


const EditButton = (props) => {
    
    const getBut = () => {
        if(props.buttonType){
            return <button type="button" id="buttonchanger" onClick={props.handleChange}>{'>>'}</button>
        }else{
            return <button type="button" id="buttonchanger" onClick={props.handleChange}>{'<<'}</button>
        }
    }

    return (
        <div>
            {getBut()}{' '}
        </div>
    );
}



export default EditButton;