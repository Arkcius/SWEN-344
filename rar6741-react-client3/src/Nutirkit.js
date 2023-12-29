import React from 'react';
import Menu from './Menu';
import SelectedItems from './SelectedItems';
import EditButton from './EditButton';
import FoodType from './FoodType';
import GoalCalorie from './GoalCalorie';
import Label from './Label';
import FoodUpdate from './FoodUpdate';
import ProgressBar from './ProgressBar';

class Nutrikit extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            foodtype: '',
            selected: [],
            selectedCal: [],
            selectedItemCalories: '',
            selectedItemName: '',
            selectedItem: '',
            add: true,
            goalCal: 2000,
        };

        this.handleChangeType = this.handleChangeType.bind(this);
        this.handleChangeMenu = this.handleChangeMenu.bind(this);
        this.handleClick = this.handleClick.bind(this);
        this.handleChangeSelected = this.handleChangeSelected.bind(this);

        this.addHundred = this.addHundred.bind(this);
        this.remHundred = this.remHundred.bind(this);

        this.handleUpdates = this.handleUpdates.bind(this);
    }
    handleChangeType(event){
        this.setState({
            foodtype: event.target.value
        });
    }

    handleChangeMenu(event){
        this.setState({
            selectedItemCalories: event.target.value,
            selectedItemName: event.target.options[event.target.selectedIndex].text,
            add: true
        });
    }

    handleClick(event){
        if(this.state.add){
            if(this.state.foodtype !== ''&&this.state.selectedItemName!==''){
                let allItems = this.state.selected;
                allItems.push(this.state.selectedItemName);
                let allCal = this.state.selectedCal;
                allCal.push(this.state.selectedItemCalories);
                console.log(this.state.selectedCal);
                console.log(allCal)
                this.setState({
                    selected: allItems,
                    selectedCal: allCal
                });
            }
        }

        else{
            let allItems = this.state.selected;
            var index = allItems.indexOf(this.state.selectedItem);
            allItems.splice(index,1);
            let allCal = this.state.selectedCal;
            allCal.splice(index,1);

            this.setState({
                selected: allItems,
                selectedCal: allCal
            });
        }
    }

    handleChangeSelected(event){
        this.setState({
            selectedItem: event.target.value,
            add: false
        });
    }

    getMenu(props){
        let foodt =[];
        if(this.state.foodtype === 'Protein'){
            foodt = this.props.proteins;
        }else if(this.state.foodtype === 'Fruits'){
            foodt = this.props.fruits;
        }else if(this.state.foodtype === 'Vegetables'){
            foodt = this.props.vegetables;
        }else if(this.state.foodtype === 'Dairy'){
            foodt = this.props.dairy;
        }else if(this.state.foodtype === 'Grains'){
            foodt = this.props.grains;
        }

        if(foodt[0] !== null){
            return foodt
        }
        return [];
    }

    getTotalCalories(){
        let calCount = 0;
        for(var i=0; i<this.state.selectedCal.length; i++){
            calCount = calCount + parseInt(this.state.selectedCal[i]);
        }
        return calCount;
    }

    remHundred(){
        let temp = this.state.goalCal - 100
        if(temp < 0){
            temp =0;
        }
        this.setState({
            goalCal: temp
        })
    }

    addHundred(){
        let temp = this.state.goalCal + 100
        this.setState({
            goalCal: temp
        })
    }

    getNutrition(props){
        if(this.state.selectedItemName !== ' '){
            for(const key of Object.entries(this.props)){
                for(const food of Object.entries(key[1])){
                    if(this.state.selectedItemName === food[1].food){
                        return food[1]
                    }
                }
            }
        }
        return ""
    }

    getNutritionSelected(props){
        let totalF =0;
        let satF =0;
        let transF =0;
        let prot =0;
        let carbs = 0;

        if(this.state.selected.length !== 0){
            for(var i=0; i< this.state.selected.length;i++){
                for(const key of Object.entries(this.props)){
                    for(const food of Object.entries(key[1])){
                        if(this.state.selected[i] === food[1].food){
                            totalF = totalF + food[1].totalFat;
                            satF = satF + food[1].saturatedFat;
                            transF = transF + food[1].transFat;
                            prot = prot + food[1].protein;
                            carbs = carbs + food[1].carbohydrate;
                        }
                    }
                }
            }
        }
        var foodsNu = {
            'totalFat' : totalF,
            'saturatedFat' : satF,
            'transFat' : transF,
            'protein' : prot,
            'carbohydrate': carbs
        }
        return foodsNu
    }


    getLabel(){
        let menuNu = this.getNutrition();
        let seleNu = this.getNutritionSelected();
        return <Label menuSelection={menuNu} selectedFood={seleNu} totalCal = {this.getTotalCalories()}/>
    }

    handleUpdates(event){
        const values = event.target.value
        var valuesSplit = values.split(",")
        var foodname = valuesSplit[0];
        var type = valuesSplit[1];
        var data = valuesSplit[2];

        
            for(const key of Object.entries(this.props)){
                for(const food of Object.entries(key[1])){
                    if(foodname === food[1].food){
                        if(type === "name"){
                            food[1].name = data;
                        }else if(type === "calories"){
                            food[1].calories = data;
                        }else if(type === "totalFat"){
                            food[1].totalFat = data;
                        }else if(type === "saturatedFat"){
                            food[1].saturatedFat = data;
                        }else if(type === "transFat"){
                            food[1].transFat = data;
                        }else if(type === "protein"){
                            food[1].protein = data;
                        }else if(type === "carbohydrate"){
                            food[1].carbohydrate = data;
                        }
                    }
                }
            }
            
        return ""
    }

    render(){
        return(
            <body class="text-bg-light p-3">
            <h1 class = "head1">Nutrikit Food Planner</h1>
            <h3 class = "head3">Nutrikit allows you to select your groceries, and track your nutritional progress (good or bad)</h3>
            <div class = "main">
                <div class = "container">
                    <div class= "row justify-content-around">
                        <div class = "col-md-auto">
                            <FoodType handleChange={this.handleChangeType}/>
                        </div>
                        <div class = "col-md-auto">
                            <Menu handleChange={this.handleChangeMenu} foods={this.getMenu()}/>
                        </div>
                        <div class = "col-md-auto">
                            <EditButton handleChange={this.handleClick} buttonType={this.state.add}/>
                        </div>
                        <div class = "col-md-auto">
                            <SelectedItems handleChange={this.handleChangeSelected} foods={this.state.selected} totalCal = {this.getTotalCalories()}/>
                        </div>
                    </div>
                    <div class = "row justify-content-center">
                        <div class ="col-md-auto">
                            {this.getLabel()}
                        </div>
                    </div>
                    <div class="row"><br></br></div>
                    <div class="row"><br></br></div>
                    <div class="row justify-content-center">
                        <div class="col-md-auto">
                            <GoalCalorie handleRemHundred={this.remHundred} handleAddHundred={this.addHundred} goal={this.state.goalCal}/>
                        </div>
                    </div>
                    <div class="row justify-content-center">
                        <div class="col">
                        <ProgressBar totalCal={this.getTotalCalories()} goal={this.state.goalCal}/>
                        </div>
                    </div>
                    <div class="row"><br></br></div>
                    <div class="row justify-content-center" >Must Reselect Food For Effect</div>
                    <div class="row justify-content-center">
                        <div class="col-md-auto">
                            <FoodUpdate handleUpdate={this.handleUpdates}/>
                        </div>
                    </div>
                </div>
            </div>
            </body>
        );
    }
}

export default Nutrikit