import React from 'react';
import Menu from './Menu';
import SelectedItems from './SelectedItems';
import EditButton from './EditButton';
import FoodType from './FoodType';

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
        };

        this.handleChangeType = this.handleChangeType.bind(this);
        this.handleChangeMenu = this.handleChangeMenu.bind(this);
        this.handleClick = this.handleClick.bind(this);
        this.handleChangeSelected = this.handleChangeSelected.bind(this);
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


    render(){
        return(
            <body>
            <h1 class = "head1">Nutrikit Food Planner</h1>
            <h3 class = "head3">Nutrikit allows you to select your groceries, and track your nutritional progress (good or bad)</h3>
            <div class = "main">
                <div>
                    <FoodType handleChange={this.handleChangeType}/>
                </div>
                <div>
                    <Menu handleChange={this.handleChangeMenu} foods={this.getMenu()}/>
                </div>
                <div>
                    <EditButton handleChange={this.handleClick} buttonType={this.state.add}/>
                </div>
                <div>
                    <SelectedItems handleChange={this.handleChangeSelected} foods={this.state.selected} totalCal = {this.getTotalCalories()}/>
                </div>
            </div>
            </body>
        );
    }
}

export default Nutrikit