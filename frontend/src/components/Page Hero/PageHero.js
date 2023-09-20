import './PageHero.scss';
import { useEffect, useState } from 'react';
import AnimatedLetter from '../AnimatedLetter';

const PageHero = () => {
    const [letterClass, setLetterClass] = useState('text-animate');
    const nameArray = ['Word',',', ' ', 'the', ' ','Word', ' ', 'was', ' ', 'with', ' ', 'God', ',', ' ', 'and', ' ', 'the', ' ', 'Word', ' ', 'was', ' ','God', '.']

    useEffect(() => {
        const timeoutId = setTimeout(() => {
            setLetterClass('text-animate-hover')
        }, 4000)
        return () => clearTimeout(timeoutId)
    }, [])


  return (
    <div className='heroContainer home-page'>
        <div className='text-zone'>
            <h1>
                <span className={letterClass}>In </span>
                <span className={`${letterClass} _12`}>the </span>
                <span className={`${letterClass} _13`}>begining </span>
                <span className={`${letterClass} _14`}>was </span>
                <span className={`${letterClass} _14`}>the</span>
            <AnimatedLetter letterClass={letterClass} strArray={nameArray} index={15} />
            </h1>
        </div>
    </div>
  )
}

export default PageHero;