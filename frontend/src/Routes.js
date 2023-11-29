import { BrowserRouter as Router, Route, Routes as Switch } from 'react-router-dom'
import App from './App'
import  Welcome from './Welcome'
import Header from "./header";
import Footer from "./footer";
export const Routes = () => {
    return (
        <Router>
            <Header />
            <Switch>
                <Route path="/" element={<Welcome />} />
                <Route path="/home" element={<App />} />
            </Switch>
            <Footer />
        </Router>
    )

}