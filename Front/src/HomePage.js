import React, { useState, useEffect } from 'react';
import './CreateInsight.css';
import HomeHeader from './components/HomeHeader';
import Card from './components/Card';
import { MdMoreHoriz, MdSearch } from "react-icons/md";
import axios from 'axios';

const HomePage = () => {

    const [cardList, setCardList] = useState([]);
    const [search, setSearch] = useState('');

    useEffect(() => {
        // Atualiza o titulo do documento usando a API do browser
        return axios.get('http://127.0.0.1:8000/cards').then(res => {
            setCardList(res.data);
        })
        .catch(err => {
            console.log(err);
            console.log(err.stack);
        });
    },[]);

    const handleSearch = () => {
        return axios.get('http://127.0.0.1:8000/cards?tags='+search.trim()).then(res => {
            setCardList(res.data);
        })
        .catch(err => {
            console.log(err);
            console.log(err.stack);
        });
    }

    return(
        <div className="HomePage">
          <HomeHeader/>
          <div className="Body">
            <h1>Feed de <b>Insights</b></h1>
            {cardList.map(card =>
                <Card cardData={card}/>
            )}
            <MdMoreHoriz className="MoreButton"/>
            <p className="TouchMessage">Toque para exibir mais layouts</p>
            <div className="InputSearch">
              <input onChange={(event) => setSearch(event.target.value)} type="text"/>
              <MdSearch onClick={() => handleSearch()} size='24px' opacity='0.64'/>
            </div>
          </div>
        </div>
    );
};

export default HomePage;