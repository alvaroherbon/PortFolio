import React, { useState } from 'react';
import TinderCard from 'react-tinder-card';

import "./TinderCards.css";

function TinderCards() {

    const [people, setPeople] = useState([
        {
        name: 'Elon Musk',
        url: "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Elon_Musk_Royal_Society_%28crop1%29.jpg/220px-Elon_Musk_Royal_Society_%28crop1%29.jpg",}
        , 
        {
        name: 'Jeff Bezos',
        url: "https://cdn.forbes.com.mx/2020/08/Jeff-Bezos-amazon-acciones-e1633495515652-640x360.jpg",}
        ,
    ]);


    const swiped = (direction, nameToDelete) => {
        console.log("removing: " + nameToDelete);
        //setLastDirection(direction); 
    };

    const outOfFrame = (name) => {
        console.log("removing: " + name);
    };

  return (
  <div className = "tinderCards">
      <div className = "tinderCards__cardContainer">
      {people.map((person) => (
          <TinderCard
              className = "swipe"
              key = {person.name}
              preventSwipe = {['up', 'down']}
              onSwipe = {(dir) => swiped(dir, person.name)}
              onCardLeftScreen = {() => outOfFrame(person.name)}
              >
              <div
                style = {{backgroundImage: `url(${person.url})`}}
                width = "500px"
                height = "500px"
                s
                className = "card"
              >
                  <h3>{person.name}</h3>
              </div>

          </TinderCard>
        )) }
      </div>
  </div>);
 
}

export default TinderCards;
