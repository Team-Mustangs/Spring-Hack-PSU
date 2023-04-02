import ReactDOM from 'react-dom';
import styles from './globals.css';
import RootLayout from './layout';
import Link from 'next/link';

export default function homepage() {
    return ( <
        RootLayout >
        <
        div >
        <
        h1 > Welcome to Banking Reimagined < /h1> <
        p className = 'blue font' > Making banking accessible
        for everyone < /p> <
        /div> <
        div >
        <
        /div> <
        img src = "banking.jpg"
        alt = "Bank" / >

        <
        div className = 'image-text nfont' >
        <
        div className = 'modal' >
        <
        div > Our website facilitates communication between banking support services and people with deaf and dumb disabilities through American Sign Language(ASL) and AI.We are committed to making banking support services accessible to everyone. < /div> <
        /div> <
        Link href = '/ASL to English/src/inference_classifier.py' >
        <
        button class = "button-35"
        role = "button" > Get Started < /button> <
        /Link> <
        /div>

        <
        div >
        <
        footer className = 'footer-contain' >
        <
        img className = "img2"
        src = "M&T.png"
        alt = "M&T" / > < img className = 'img2'
        src = "c1.png"
        alt = "c1" / >
        <
        div > @2023 Collaborated with M & T Tech and Capital One < /div> <
        /footer> <
        /div>


        <
        /RootLayout>
    );
}