import './index.scss';

const AnimatedLetter = ({letterClass, strArray, index}) => {
  return (
    <span>
        {
            strArray.map((char, i) => (
                <span key={char + i} className={`${letterClass} _${i + index} isolated`}>
                    {char}
                </span>
            ))
        }
    </span>
  )
}

export default AnimatedLetter