import React from 'react';
import { Progress } from 'reactstrap';
import './App.css';

const ProgressBar = (props) => {

    var goalCal = props.goal;

    const calculateCalPercent = () => {
        let percent = props.totalCal / goalCal;
        percent = percent * 100;
        return percent;
    }

    const getProgressBar = () => {
        if(props.totalCal < goalCal){
        return <Progress animated value={calculateCalPercent()}>{props.totalCal}/{goalCal}</Progress>
        }else if(props.totalCal === goalCal){
            return <Progress animated color="success" value={calculateCalPercent()}>{props.totalCal}/{goalCal}</Progress>
        }else{
            return <Progress animated color="danger" value={calculateCalPercent()}>{props.totalCal}/{goalCal}</Progress>
        }
    }

    

    return (

        <div>
            {getProgressBar()}
        </div>

        
    );
};

export default ProgressBar;
