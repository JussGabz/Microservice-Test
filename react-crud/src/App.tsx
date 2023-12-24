import React from 'react';
import logo from './logo.svg';
import './App.css';
import Products from './admin/Products';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Main from './main/Main';
import ProductsCreate from './admin/ProductsCreate';

function App() {
  return (
    <div className="App">          
            <BrowserRouter>
              <Routes>
                <Route path='/' Component={Main}/>
                <Route path='/admin/products' Component={Products}/>
                <Route path='/admin/products/create' Component={ProductsCreate}/>
              </Routes>
            </BrowserRouter>
    </div>
);
}

export default App;
