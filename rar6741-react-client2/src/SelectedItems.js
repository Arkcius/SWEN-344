import React from 'react';
import './App.css';

class SelectedItems extends React.Component{
    
    editMenu(selecteds){
        var selectedItems = selecteds.selecteds
        var cur;
        let opti = [];

        if(selectedItems.length>0){
            for(var i =0; i<selectedItems.length;i++){
                cur = selectedItems[i];
                opti.push(<option value={cur}>{cur}</option>)
            }
            return opti
        }
        return<></>
    }

    render(){
        return(
        <div>
            <label class='block' for="selectedItems">Selected Items</label>
            <select class='select' id="selectedItems" size={5} onChange={this.props.handleChange}>
                <this.editMenu selecteds={this.props.foods}/>
            </select>
            <p id="calories" class="block">Total Calories: {this.props.totalCal}</p>
        </div>
        );
    }
}

export default SelectedItems;