import React from 'react';
import { Card, CardTitle, CardSubtitle, Row, Col, ListGroup, ListGroupItem } from 'reactstrap';

const Label = (props) => {

    //Based on a 2000 Calorie Diet
    let totalFatDV = 80;
    let calorieDV = 2000;
    let saturatedFatDV = 20;
    let transFatDV = 20;
    let proteinDV = 100;
    let carbohydrateDV = 100;

    const getPercentDV = (num) => {
        return 0.2 * num
    }

    const getDaily = (num, type, sd) => {
        if(type === "totalFat"){
            if(num < getPercentDV(totalFatDV) && sd === "single"){
                return "success"
            }else if(num < totalFatDV && sd === "daily"){
                return "success"
            }else{
                return "danger"
            }
        }else if(type === "saturatedFat"){
            if(num < getPercentDV(saturatedFatDV) && sd === "single"){
                return "success"
            }else if(num < saturatedFatDV && sd === "daily"){
                return "success"
            }else{
                return "danger"
            }
        }else if(type === "transFat"){
            if(num < getPercentDV(transFatDV) && sd === "single"){
                return "success"
            }else if(num < saturatedFatDV && sd === "daily"){
                return "success"
            }else{
                return "danger"
            }
        }else if(type === "protein"){
            if(num < getPercentDV(proteinDV) && sd === "single"){
                return "warning"
            }else if(num < proteinDV && sd === "daily"){
                return "warning"
            }else{
                return "success"
            }
        }else if(type === "carb"){
            if(num < getPercentDV(carbohydrateDV) && sd === "single"){
                return "success"
            }else if(num < carbohydrateDV && sd === "daily"){
                return "success"
            }else{
                return "danger"
            }
        }else if(type === "calories"){
            if(num < getPercentDV(calorieDV) && sd === "single"){
                return "success"
            }else if(num < calorieDV && sd === "daily"){
                return "success"
            }else{
                return "danger"
            }
        }
        
        
        
        
    }


    const getMenuInfo = () => {

        let food = "Menu Food Item";
        let calories = 0;
        let saturatedFat = 0;
        let transFat = 0;
        let totalfat = 0;
        let protein = 0;
        let carbohydrate = 0;

        if(props.menuSelection !== ""){
            food = props.menuSelection.food;
            calories = props.menuSelection.calories;
            totalfat = props.menuSelection.totalFat;
            saturatedFat = props.menuSelection.saturatedFat;
            transFat = props.menuSelection.transFat;
            protein = props.menuSelection.protein;
            carbohydrate = props.menuSelection.carbohydrate;
        }

        let toFColor = getDaily(totalfat, "totalFat", "single")
        let sFColor = getDaily(saturatedFat, "saturatedFat", "single")
        let trFColor = getDaily(transFat, "transFat", "single")
        let pColor = getDaily(protein, "protein", "single")
        let cbColor = getDaily(carbohydrate, "carb", "single")
        let caColor = getDaily(calories, "calories", "single")
        

        return  <Col sm="6" xs="auto">
                    <Card body inverse color={caColor}>
                        <CardTitle tag="h4">{food}</CardTitle>
                        <CardSubtitle tag="h5">Calories: {calories}</CardSubtitle>
                        <ListGroup flush>
                            <ListGroupItem color={toFColor}>Total Fat: {Number(totalfat).toFixed(2)}g</ListGroupItem>
                            <ListGroupItem color={sFColor}>Sat Fat: {Number(saturatedFat).toFixed(2)}g</ListGroupItem>
                            <ListGroupItem color={trFColor}>Trans Fat: {Number(transFat).toFixed(2)}g</ListGroupItem>
                            <ListGroupItem color={pColor}>Protein: {Number(protein).toFixed(2)}g</ListGroupItem>
                            <ListGroupItem color={cbColor}>Total Carbs: {Number(carbohydrate).toFixed(2)}g</ListGroupItem>
                        </ListGroup>
                    </Card>
                </Col>
    }





    const getSelectionInfo = () => {
        
        let calories = props.totalCal;
        let saturatedFat = props.selectedFood.saturatedFat;
        let transFat = props.selectedFood.transFat;
        let totalfat = props.selectedFood.totalFat;
        let protein = props.selectedFood.protein;
        let carbohydrate = props.selectedFood.carbohydrate;

        let toFColor = getDaily(totalfat, "totalFat", "daily")
        let sFColor = getDaily(saturatedFat, "saturatedFat", "daily")
        let trFColor = getDaily(transFat, "transFat", "daily")
        let pColor = getDaily(protein, "protein", "daily")
        let cbColor = getDaily(carbohydrate, "carb", "daily")
        let caColor = getDaily(calories, "calories", "daily")

        return  <Col sm="6" xs="auto">
                    <Card body inverse color={caColor}>
                        <CardTitle tag="h4">Daily</CardTitle>
                        <CardSubtitle tag="h5">Calories: {calories}</CardSubtitle>
                        <ListGroup flush>
                            <ListGroupItem color={toFColor}>Total Fat: {Number(totalfat).toFixed(2)}g</ListGroupItem>
                            <ListGroupItem color={sFColor}>Sat Fat: {Number(saturatedFat).toFixed(2)}g</ListGroupItem>
                            <ListGroupItem color={trFColor}>Trans Fat: {Number(transFat).toFixed(2)}g</ListGroupItem>
                            <ListGroupItem color={pColor}>Protein: {Number(protein).toFixed(2)}g</ListGroupItem>
                            <ListGroupItem color={cbColor}>Total Carbs: {Number(carbohydrate).toFixed(2)}g</ListGroupItem>
                        </ListGroup>
                    </Card>
                </Col>
    }



    return (
        <Row md="2">
            {getMenuInfo()}
            {getSelectionInfo()}
        </Row>
    );
};

export default Label;
