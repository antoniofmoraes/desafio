import React from 'react';
import './HomeHeader.css';
import avatar from '../assets/avatar.png';
import logo from '../assets/brand-insights@3x.svg';
import { MdAdd } from "react-icons/md";
import { Link } from "react-router-dom";


const HomeHeader = () => {
    return(
        <div className='Header'>
            <div className='HeaderIcons'>
                <div className='Logo'>
                    <img src={logo}></img>
                </div>
                <div className="Avatar">
                    <img src={avatar} alt="Avatar"/>
                </div>
                <div className="AddButton">
                    <Link to="/criarInsight">
                        <MdAdd color='#ED4D77' size='24px'></MdAdd>
                    </Link>
                </div>
            </div>
            <h2 className='Text Hello'>
            Olá, Antonio!
            </h2>
            <h2 className='Text Email'>
            antonio.f.f.moraes@gmail.com
            </h2>
        </div>
    );
};

export default HomeHeader;

