import React, {useEffect, useState} from 'react';
import { MdCardMembership } from 'react-icons/md';
import './Card.css';
import Tag from './Tag';

const Card = ({ cardData }) => {
    const [tags, setTags] = useState([]);

    useEffect(() => {
        if (cardData.hasOwnProperty('tags') ) {
            setTags(cardData.tags);
        }
    }, []);

    return(
        <div className="Card">
            <p>{cardData.text}</p>
            <div className="Tags">
                {tags.map(tag => 
                    <Tag name={tag.trim()}/>
                )}
            </div>
        </div>
    );
};

export default Card;