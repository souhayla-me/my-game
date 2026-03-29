import React from 'react';
import { Kitchen } from './components/Kitchen';
import { Customer } from './components/Customer';
import { Vendor } from './components/Vendor';

const App = () => {
    return (
        <div>
            <Kitchen />
            <Customer />
            <Vendor />
        </div>
    );
};

export default App;