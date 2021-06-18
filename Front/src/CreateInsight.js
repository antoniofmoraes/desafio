import React, { useState } from 'react';
import './CreateInsight.css';
import { MdArrowBack } from "react-icons/md";
import { Link } from "react-router-dom";
import axios from 'axios';

const CreateInsight = () => {

    const [insight, setInsight] = useState('')
    const [tags, setTags] = useState('')

    const handleNewCard = () => {
        const unsub = axios.post(`http://127.0.0.1:8000/card/create?text=${insight}&tags=${tags}`)
        .then(res => {
            return res.data;
        })
        .catch(err => {
            console.log(err);
            console.log(err.stack);
        });

        return unsub;
    };

    return (
        <div className="CreateInsightPage">
            <div className="HeaderCreateInsight">
                <Link to="/">
                    <MdArrowBack size='24px' color='#ED4D77'/>
                </Link>
                <h1 className="PageTitleCreateInsight">
                    CRIAR<br/>
                    <b>INSIGHT</b>
                </h1>
                <div/>
            </div>
            <div className="BodyCreateInsight">
                <div className="FormCreateInsight">
                    <label>INSIGHT</label>
                    <input type="text" style={{height: '196px'}} onChange={(event) => setInsight(event.target.value)} value={insight}/>
                    <h6>Limite de caracteres: 400</h6>
                    <label>CATEGORIA</label>
                    <input type="text" style={{height: '32px'}} onChange={(event) => setTags(event.target.value)} value={tags}/>
                </div>
            </div>
            <input onClick={() => { handleNewCard(); setInsight(''); setTags('')}} className="ButtonCreateInsight" type="button" value="PUBLICAR"/>
        </div>
    );
};

export default CreateInsight;