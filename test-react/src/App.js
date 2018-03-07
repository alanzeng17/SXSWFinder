import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

export class App extends React.Component {
  render() {
    return (
      <div className="App">

      </div>
    );
  }
}
export class Body extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div className ='body'>
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">MedPack</h1>
        </header>
        <h1>Is This Medication Covered By My Insurance?</h1>
        <form method = "post" action = "">
        <table>
        <tr class = 'insurance'>
          <td>
              <label> Medical Insurance:
              <select name = "rating">
                  <option selected = "selected"> Blue Cross Blue Shield</option>
            <option> eHealth </option>
            <option> Humana </option>
          </select>
              </label>
            </td>
        </tr>
        <tr class = 'problem'>
          <td>
              <label> Choose your illness or medical problem:
              <select name = "rating">
                  <option selected = "selected"> Cold</option>
            <option> Fever </option>
            <option> Strep Throat </option>
            <option> Flue </option>
          </select>
              </label>
            </td>
          
        </tr>
        <tr class = 'buttons'>
          <td>
            <input type = "submit" value = "Enter" />
            <input type = "reset" value = "Clear" />
          </td>
        </tr>
        
        </table>
        </form>
      </div>

    );
  }
}

//export default Body;