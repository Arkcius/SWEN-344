import React from 'react';
import './App.css';
import { Button, Row, Col, Alert } from 'reactstrap';

const GoalCalorie = (props) => {

    return (
        <Row xs="5">
            <Col xs="auto">
                <Button color="primary" onClick={props.handleRemHundred} active>-100</Button>
            </Col>
            <Col xs="auto">
                Total Calorie Goal:
                <Alert color="dark">{props.goal}</Alert>
            </Col>
            <Col xs="auto">
                <Button color="primary" onClick={props.handleAddHundred} active>+100</Button>
            </Col>
        </Row>
    );
}




export default GoalCalorie;