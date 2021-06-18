import React from 'react';
import './Tag.css';

const Tag = ({name}) => {
    return(
        <div className="Tag">
            <p>{name}</p>
        </div>
    );
};

export default Tag;