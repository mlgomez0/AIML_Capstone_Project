import { BrowserRouter as Router, Route, Routes as Switch } from 'react-router-dom'
import App from './App'
import  Welcome from './Welcome'
export const Routes = () => {
    return (
        <Router>
            <Switch>
                <Route path="/" element={<Welcome />} />
                <Route path="/home" element={<App />} />
            </Switch>

        </Router>
    )

}