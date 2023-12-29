import React from 'react';
import './App.css';
import Nutrikit from './Nutirkit';

function Food(){
    return(
        <div>
            <Nutrikit 
            proteins={[{"id": 0,
            "food": "steak",
            "category": "Proteins",
            "calories": 300,
            "totalFat": 5.73,
            "saturatedFat": 2.183,
            "transFat": 0.182,
            "protein": 29.44,
            "carbohydrate": 0.0
          },
            {
            "id": 1,
            "food": "ground beef",
            "category": "Proteins",
            "calories": 200,
            "totalFat": 13.1,
            "saturatedFat": 5.3,
            "transFat": 0.6,
            "protein": 15.18,
            "carbohydrate": 0.0
          },
           {
            "id": 2,
            "food": "chicken",
            "category": "Proteins",
            "calories": 100,
            "totalFat": 9.3,
            "saturatedFat": 2.5,
            "transFat": 0.1,
            "protein": 27.14,
            "carbohydrate": 0.0
          },
           {
            "id": 3,
            "food": "fish",
            "category": "Proteins",
            "calories": 80,
            "totalFat": 6.34,
            "saturatedFat": 1.0,
            "transFat": 0.0,
            "protein": 19.84,
            "carbohydrate": 0.0
          },
          {
            "id": 4,
            "food": "soy",
            "category": "Proteins",
            "calories": 50,
            "totalFat": 19.94,
            "saturatedFat": 2.884,
            "transFat": 0.0,
            "protein": 36.49,
            "carbohydrate": 30.16}]}

            fruits={[{
      "id": 5,
      "food": "orange",
      "category": "Fruits",
      "calories": 300,
      "totalFat": 0.12,
      "saturatedFat": 0.0,
      "transFat": 0.0,
      "protein": 0.94,
      "carbohydrate": 11.75
    },
    {
      "id": 6,
      "food": "banana",
      "category": "Fruits",
      "calories": 200,
      "totalFat": 0.33,
      "saturatedFat": 0.0,
      "transFat": 0.0,
      "protein": 1.09,
      "carbohydrate": 22.84
    },
    {
      "id": 7,
      "food": "pineapple",
      "category": "Fruits",
      "calories": 100,
      "totalFat": 0.12,
      "saturatedFat": 0.0,
      "transFat": 0.0,
      "protein": 0.54,
      "carbohydrate": 13.12
    },
    {
      "id": 8,
      "food": "grapes",
      "category": "Fruits",
      "calories": 80,
      "totalFat": 0.16,
      "saturatedFat": 0.0,
      "transFat": 0.0,
      "protein": 0.72,
      "carbohydrate": 18.1
    },
    {
      "id": 9,
      "food": "blueberries",
      "category": "Fruits",
      "calories": 50,
      "totalFat": 0.33,
      "saturatedFat": 0.0,
      "transFat": 0.0,
      "protein": 0.74,
      "carbohydrate": 14.49
    }]}
            vegetables={[{
                "id": 10,
                "food": "romaine",
                "category": "Vegetables",
                "calories": 30,
                "totalFat": 0.3,
                "saturatedFat": 0.0,
                "transFat": 0.0,
                "protein": 1.2,
                "carbohydrate": 3.3
              },
              {
                "id": 11,
                "food": "green beans",
                "category": "Vegetables",
                "calories": 40,
                "totalFat": 0.22,
                "saturatedFat": 0.0,
                "transFat": 0.0,
                "protein": 1.83,
                "carbohydrate": 6.97
              },
              {
                "id": 12,
                "food": "squash",
                "category": "Vegetables",
                "calories": 100,
                "totalFat": 0.2,
                "saturatedFat": 0.0,
                "transFat": 0.0,
                "protein": 1.2,
                "carbohydrate": 3.4
              },
              {
                "id": 13,
                "food": "spinach",
                "category": "Vegetables",
                "calories": 50,
                "totalFat": 0.4,
                "saturatedFat": 0.0,
                "transFat": 0.0,
                "protein": 2.9,
                "carbohydrate": 3.6
              },
              {
                "id": 14,
                "food": "kale",
                "category": "Vegetables",
                "calories": 10,
                "totalFat": 0.9,
                "saturatedFat": 0.0,
                "transFat": 0.0,
                "protein": 4.3,
                "carbohydrate": 8.8
              }]}

            dairy={[{
                "id": 15,
                "food": "milk",
                "category": "Dairy",
                "calories": 300,
                "totalFat": 3.9,
                "saturatedFat": 2.4,
                "transFat": 0.0,
                "protein": 3.2,
                "carbohydrate": 4.8
              },
              {
                "id": 16,
                "food": "yoghurt",
                "category": "Dairy",
                "calories": 200,
                "totalFat": 5.0,
                "saturatedFat": 0.0,
                "transFat": 0.0,
                "protein": 9.0,
                "carbohydrate": 3.98
              },
              {
                "id": 17,
                "food": "cheddar cheese",
                "category": "Dairy",
                "calories": 200,
                "totalFat": 9.0,
                "saturatedFat": 6.0,
                "transFat": 0.0,
                "protein": 7.0,
                "carbohydrate": 0.0
              },
              {
                "id": 18,
                "food": "skim milk",
                "category": "Dairy",
                "calories": 100,
                "totalFat": 0.2,
                "saturatedFat": 0.1,
                "transFat": 0.0,
                "protein": 8.3,
                "carbohydrate": 12.5
              },
               {
                "id": 19,
                "food": "cottage cheese",
                "category": "Dairy",
                "calories": 80,
                "totalFat": 4.3,
                "saturatedFat": 0.0,
                "transFat": 0.0,
                "protein": 11.12,
                "carbohydrate": 3.38
              }]}
            grains={[ {
                "id": 20,
                "food": "bread",
                "category": "Grains",
                "calories": 200,
                "totalFat": 1.1,
                "saturatedFat": 0.0,
                "transFat": 0.0,
                "protein": 4.0,
                "carbohydrate": 13.8
              },
               {
                "id": 21,
                "food": "bagel",
                "category": "Grains",
                "calories": 300,
                "totalFat": 1.7,
                "saturatedFat": 0.1,
                "transFat": 0.0,
                "protein": 13.8,
                "carbohydrate": 68
              },
               {
                "id": 22,
                "food": "pita",
                "category": "Grains",
                "calories": 250,
                "totalFat": 1.7,
                "saturatedFat": 0.3,
                "transFat": 0.0,
                "protein": 6.3,
                "carbohydrate": 35.2
              },
               {
                "id": 23,
                "food": "naan",
                "category": "Grains",
                "calories": 210,
                "totalFat": 3.3,
                "saturatedFat": 0.1,
                "transFat": 0.0,
                "protein": 2.7,
                "carbohydrate": 16.9
              },
               {
                "id": 24,
                "food": "tortilla",
                "category": "Grains",
                "calories": 120,
                "totalFat": 0.5,
                "saturatedFat": 0.1,
                "transFat": 0.0,
                "protein": 1.1,
                "carbohydrate": 8.5
              }]}
            />
        </div>
    )
}

export default Food;