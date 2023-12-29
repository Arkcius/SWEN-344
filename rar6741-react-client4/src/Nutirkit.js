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
            update: false,
            dataN: '',
            type: '',
            foodname: ''
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
                    if(this.state.selectedItemName === food[1].name){
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
                        if(this.state.selected[i] === food[1].name){
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

        this.setState({
            dataN: data,
            type: type,
            foodname: foodname,
            update: true
        });
        console.log(this.state.update)
            
    }

    componentDidMount(){
        this.init();
    }
    init = () => {
        if(this.state.update){

        const formData = new FormData();
        formData.append('foodname', this.state.foodname);
        formData.append('data', this.state.dataN);
        formData.append('type', this.state.type)
        console.log("update plz")
        fetch('http://localhost:5000/food', {
            method: 'PUT',
            body: formData
        });

        this.setState({
            update : false
        });
        }
        fetch('http://localhost:5000/food?category=proteins')
        .then((response) =>
            {
                if(response.status === 200)
                {
                    return(response.json()) ;
                }else{
                    return ([ ["status ", response.status]]);
                }
            }
        )
        .then((jsonOutput) =>
            {
                while(this.props.proteins.length>0){
                this.props.proteins.pop();
                }
                for(var i = 0; i < 5; i++){
                    this.props.proteins.push(jsonOutput[i])
                } 
            }
        )
        .catch(error =>{
            console.log("no API");
        })

        fetch('http://localhost:5000/food?category=fruits')
        .then(
            (response) =>
            {
                if(response.status === 200)
                {
                    return(response.json()) ;
                }else{
                    return ([ ["status ", response.status]]);
                }
            }
        )
        .then((jsonOutput) =>
            {
                while(this.props.fruits.length>0){
                    this.props.fruits.pop();
                    }
                for(var i = 0; i < 5; i++){
                    this.props.fruits.push(jsonOutput[i])
                } 
            }
        )
        .catch(error =>{
            console.log("no API");
        })

        fetch('http://localhost:5000/food?category=vegetables')
        .then(
            (response) =>
            {
                if(response.status === 200)
                {
                    return(response.json()) ;
                }else{
                    return ([ ["status ", response.status]]);
                }
            }
        )
        .then((jsonOutput) =>
            {
                while(this.props.vegetables.length>0){
                    this.props.vegetables.pop();
                    }
                for(var i = 0; i < 5; i++){
                    this.props.vegetables.push(jsonOutput[i])
                } 
            }
        )
        .catch(error =>{
            console.log("no API");
        })

        fetch('http://localhost:5000/food?category=grains')
        .then(
            (response) =>
            {
                if(response.status === 200)
                {
                    return(response.json()) ;
                }else{
                    return ([ ["status ", response.status]]);
                }
            }
        )
        .then((jsonOutput) =>
            {
                while(this.props.grains.length>0){
                    this.props.grains.pop();
                    }
                for(var i = 0; i < 5; i++){
                    this.props.grains.push(jsonOutput[i])
                } 
            }
        )
        .catch(error =>{
            console.log("no API");
        })

        fetch('http://localhost:5000/food?category=dairy')
        .then(
            (response) =>
            {
                if(response.status === 200)
                {
                    return(response.json()) ;
                }else{
                    return ([ ["status ", response.status]]);
                }
            }
        )
        .then((jsonOutput) =>
            {
                while(this.props.dairy.length>0){
                    this.props.dairy.pop();
                    }
                for(var i = 0; i < 5; i++){
                    this.props.dairy.push(jsonOutput[i])
                } 
            }
        )
        .catch(error =>{
            console.log("no API");
        })
    }

    componentDidUpdate(){
        if(this.state.update){

            const formData = new FormData();
        formData.append('foodname', this.state.foodname);
        formData.append('data', this.state.dataN);
        formData.append('type', this.state.type)

            fetch('http://localhost:5000/food', {
                method: 'PUT',
                body: formData
            }).then(response => response.json())
            .then((json) => {
                console.log("updated")
                console.log(this.props.proteins)
             })
            .catch(error => {
                console.log("no updated")
            });

            this.setState({
                update : false
            });
            this.init();
            this.init();
        }
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